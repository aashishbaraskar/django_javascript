from django.contrib.auth.models import User
from django.db import models


# this is for user who is going to register with this app
class Profile(User):
    USER_TYPE = (
        (1, "Admin"),
        (2, "Seller"),
        (3, "Buyer"),
        (4, "Warehouse"),
        (5, "Logistics"),
    )
    primary_contact = models.CharField(max_length=20, unique=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    pan_card = models.CharField(max_length=20, blank=False, null=False)
    pan_image = models.ImageField(upload_to='PAN/', blank=True, null=True)
    # Personal Detail
    alternate_contact = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    landmark = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    # Bank Detail
    beneficiary_name = models.CharField(max_length=255, blank=True, null=True)
    account_no = models.CharField(max_length=50, blank=True, null=True)
    ifsc_code = models.CharField(max_length=30, blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)

    profile_photo = models.ImageField(upload_to='Profile/', blank=True, null=True)
    user_type = models.IntegerField(choices=USER_TYPE, default=1)
    is_deleted = models.BooleanField(default=False)

