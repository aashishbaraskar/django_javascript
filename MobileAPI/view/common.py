import math, random
import traceback

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    renderer_classes,
    authentication_classes, permission_classes)

from MobileAPI.helper import UserProfileToJSON
from MobileAPI.serializers import LoginSerializer, RegistrationSerializer
from account.models import Profile


@csrf_exempt
@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def api_index(request):
    return Response({"message": "Mobile_API"})


@csrf_exempt
@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def generate_otp(request):
    # Declare a digits variable
    # which stores all digits
    digits = "0123456789"
    OTP = ""

    print('Request Data', request.data)
    try:
        try:
            Profile.objects.get(username=request.data['primary_contact'])
            result, message = "Failure", "Mobile No Already Exist."
        except Profile.DoesNotExist:
            # length of password can be chaged
            # by changing value in range
            for i in range(5):
                OTP += digits[math.floor(random.random() * 10)]
            result, message, OTP = "Success", "OTP Generated Successfully", OTP
    except Exception as exc:
        print('Exception For Generating OTP | generate_otp', exc)
        print('exception ', str(traceback.print_exc()))
        result, message = "Failure", "Give Valid Data"
    return Response({
        "result": result,
        "message": message,
        "opt": OTP
    }, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def login_mobile_user(request):
    print('Request Data', request.data)
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        try:
            user_data = Profile.objects.get(primary_contact=serializer.validated_data['username'])
            user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
            if user:
                if user.is_active:
                    Token.objects.filter(user=user).delete()
                    token = Token.objects.create(user=user)
                    user_info = UserProfileToJSON(user_data)
                    result, message, user_info, auth_token = "Success", "Login Successful.", user_info, "Token " + str(token)
                else:
                    result, message, user_info, auth_token = "Failure", "User Is Deactivated, Please Contact Admin For Activation.", "", ""
            else:
                result, message, user_info, auth_token = "Failure", "Invalid Password.", "", ""
        except Profile.DoesNotExist:
            result, message, user_info, auth_token = "Failure", "Invalid Mobile Number.", "", ""
    else:
        result, message, user_info, auth_token = "Failure", "Invalid Data.", "", ""
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({
        "result": result,
        "message": message,
        "logindata": user_info,
        "authorization": auth_token
    }, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def register_mobile_user(request):
    try:
        registration_data = request.data['registration_data']
        print("Registration Data", registration_data)
        serializer = RegistrationSerializer(data=registration_data)
        if serializer.is_valid():
            try:
                Profile.objects.get(username=registration_data['primary_contact'])
                result, message, user_info, auth_token = "Failure", "Mobile No Already Exist.", "", ""
            except Profile.DoesNotExist:
                if Profile.objects.filter(email=registration_data['email']).exists():
                    result, message, user_info, auth_token = "Failure", "Email Id Already Exist.", "", ""
                else:
                    user_obj = serializer.register_user(registration_data)
                    if user_obj is not None:
                        token = Token.objects.create(user=user_obj)
                        user_info = UserProfileToJSON(user_obj)
                        result, message, user_info, auth_token = "Success", "User Register Successfully.", user_info, "Token " + str(token)
                    else:
                        result, message, user_info, auth_token = "Failure", "Invalid Data.", "", ""
        else:
            result, message, user_info, auth_token = "Failure", "Invalid Data.", "", ""
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as exc:
        print('Exception In | register_mobile_user'), exc
        result, message, user_info, auth_token = "Failure", "Invalid Data.", "", ""
    return Response({
        "result": result,
        "message": message,
        "logindata": user_info,
        "authorization": auth_token
    }, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['GET'])
@renderer_classes((JSONRenderer,))
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def logout(request):
    user = request.user
    print("In Logout", user)
    Token.objects.filter(user=user).delete()
    return Response({
        "result": "Success",
        "message": "Logout Successful."
    }, status=status.HTTP_200_OK)