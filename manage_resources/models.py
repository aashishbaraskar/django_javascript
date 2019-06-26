from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    category_image = models.ImageField(null=True, blank=True, upload_to="Category/")
    status_choice = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)


class SubCategory(models.Model):
    sub_cat_name = models.CharField(max_length=200)
    sub_cat_description = models.TextField(max_length=200)
    sub_cat_Image = models.ImageField(null=True, blank=True, upload_to="SubCategory/")
    category_fk = models.ForeignKey(Category, on_delete=models.CASCADE)
    status_choice = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "SubCategory"


class Brand(models.Model):
    brand_name = models.CharField(max_length=200, default="1")
    brand_image = models.ImageField(null=True, blank=True, upload_to="Brand/", default="1")
    status_choice = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)


class Variant(models.Model):
    variant_name = models.CharField(max_length=200)
    # sub_category_fk = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    status_choice = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)


class Product(models.Model):
    product_name = models.CharField(max_length=120, default="1")
    product_category = models.CharField(max_length=120, default="1")
    product_wastage = models.CharField(max_length=120, default="1")
    Product_quantity = models.CharField(max_length=120, default="1")
    sub_category_fk = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    brand_fk = models.ForeignKey(Brand, on_delete=models.CASCADE)
    variant_fk = models.ForeignKey(Variant, on_delete=models.CASCADE)
    status_choice = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)


class WastageType(models.Model):
    wastage_type_name = models.CharField(max_length=120)
    description = models.TextField(max_length=200)
    status_choice = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)


class Unit(models.Model):
    unit_name = models.CharField(max_length=120)
    base_unit = models.CharField(max_length=120)
    status_choice = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
