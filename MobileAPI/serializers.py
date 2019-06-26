import base64
import json
import traceback
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import transaction
from rest_framework import serializers

from account.models import Profile


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(max_length=20, required=True)


class RegistrationSerializer(serializers.Serializer):
    primary_contact = serializers.CharField(max_length=20, required=True)
    email = serializers.EmailField(max_length=100, required=True)

    class Meta:
        model = Profile
        fields = ('primary_contact', 'email')

    @transaction.atomic
    def register_user(self, validated_data):
        sid = transaction.savepoint()  # Transaction open
        try:
            user_data = Profile(
                username=validated_data['primary_contact'],
                primary_contact=validated_data['primary_contact'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                pan_card=validated_data['pan_card'],
                user_type=2
            )
            user_data.save()

            user_data.set_password(validated_data['password'])

            user_data.alternate_contact = validated_data['alternate_contact']
            user_data.address = validated_data['address']
            user_data.city = validated_data['city']
            user_data.town = validated_data['town']
            user_data.pincode = validated_data['pincode']
            user_data.landmark = validated_data['landmark']
            user_data.state = validated_data['state']

            user_data.beneficiary_name = validated_data['beneficiary_name']
            user_data.account_no = validated_data['account_no']
            user_data.ifsc_code = validated_data['ifsc_code']
            user_data.bank_name = validated_data['bank_name']
            user_data.save()

            try:
                pancard_image = json.loads(validated_data['pancard_image'])
                pan_image_file = get_image_file(str(pancard_image["image"]))
                name = pancard_image["name"]
                user_data.pan_image = SimpleUploadedFile(name, pan_image_file, getattr(pancard_image, "content_type",
                                                                                       "application/octet-stream"))
                user_data.save()
            except:
                pass

            transaction.savepoint_commit(sid)
            return user_data
        except Exception as exc:
            print('Exception For Register User | RegistrationSerializer', exc)
            print('exception ', str(traceback.print_exc()))
            transaction.rollback(sid)
            return None


def get_image_file(imagestring):
    image_data = str(imagestring)
    missing_padding = len(image_data) % 4
    if missing_padding != 0:
        image_data += b'=' * (4 - missing_padding)
    return base64.b64decode(image_data)
