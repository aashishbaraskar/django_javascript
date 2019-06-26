from django.contrib import admin
from manage_resources.models import *


class ManageBrandAdmin(admin.ModelAdmin):
    list_display = ["brand_id", "brand_name", "brand_image", "status_choice"]
    search_fields = ["brand_name"]
    list_filter = ['brand_id', "brand_name"]


admin.site.register(Brand)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["category_id", "category_name", "description", "category_image", "status_choice"]
    search_fields = ["category_name"]
    list_filter = ['category_id', "category_name"]


admin.site.register(Category)


class VariantAdmin(admin.ModelAdmin):
    list_display = ["variant_id", "variant_name", "status_choice"]
    search_fields = ["variant_name"]
    list_filter = ["variant_id", "variant_name"]


admin.site.register(Variant)


class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_name", "product_category", "product_quantity"]
    search_fields = ["product_name"]
    list_filter = ["product_name", "product_category"]


admin.site.register(Product)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ["sub_cat_name", "status_choice"]
    search_fields = ["sub_cat_name"]
    list_filter = ["sub_cat_name", ]


admin.site.register(SubCategory)


@admin.register(WastageType)
class WastageTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'wastage_type_name', 'description','status_choice']
    search_fields = ['wastage_type_name']
    list_filter = ['wastage_type_name']

