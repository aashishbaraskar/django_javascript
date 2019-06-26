from django.conf.urls import url
from django.urls import path
from MobileAPI.view import common

urlpatterns = [
    path('', common.api_index),
    path('login', common.login_mobile_user),
    path('generate_otp', common.generate_otp),
    path('register_mobile_user', common.register_mobile_user),
    path('logout', common.logout),
]