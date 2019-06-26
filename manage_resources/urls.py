from django.conf.urls import url
from django.urls import path
from manage_resources.view import brand, category, subcategory, variant, wastageType, units
from . import views


urlpatterns = [
    # path('unit/', views.Unit.as_view(), name='unit'),
    # path('category/', views.Category.as_view(), name='category'),

    path('products/', views.Products.as_view(), name='products'),

    path('brand/', brand.brand_landing_screen, name='brand'),
    path('brand-datatable/', brand.load_brand_table, name='brand-datatable'),
    path('add-new-brand/', brand.add_new_brand),
    path('change-brand-status/', brand.change_brand_status),
    path('delete-brand-detail/', brand.delete_brand_detail),
    path('show-brand-data/', brand.edit_brand_data),
    path('update-brand-data/', brand.update_brand_data),

    # variant urls
    path('variant/', variant.variant_landing_screen, name='variant'),
    path('variant-datatable/', variant.load_variant_table, name='variant_datatable'),
    path('add-new-variant/', variant.add_new_variant),
    path('change-variant-status/', variant.change_variant_status),
    path('delete-variant-detail/', variant.delete_variant_detail),
    path('show-variant-data/', variant.edit_variant_data),
    path('update-variant-data/', variant.update_variant_data),
    
    # wastageType urls
    path('wastageType/', wastageType.wastageType_landing_screen, name='wastageType'),
    path('wastageType-datatable/', wastageType.load_wastageType_table, name='wastageType_datatable'),
    path('add-new-wastageType/', wastageType.add_new_wastageType),
    path('change-wastageType-status/', wastageType.change_wastageType_status),
    path('delete-wastageType-detail/', wastageType.delete_wastageType_detail),
    path('show-wastageType-data/', wastageType.edit_wastageType_data),
    path('update-wastageType-data/', wastageType.update_wastageType_data),

    # unit
    path('unit/', units.unit_landing_screen, name='unit'),
    path('unit-datatable/', units.load_unit_table, name='unit_datatable'),
    path('add-new-unit/', units.add_new_unit),
    path('change-unit-status/', units.change_unit_status),
    path('delete-unit-detail/', units.delete_unit_detail),
    path('show-unit-data/', units.edit_unit_data),
    path('update-unit-data/', units.update_unit_data),


    url(r'subcategory/', subcategory.subcategory_landing_screen, name='subcategory'),
    url(r'subcategory-datatable/', subcategory.load_subcategory_table, name='subcategory_datatable'),
    url(r'add-new-subcategory/', subcategory.add_new_sub_category),

    path('category/', category.category_landing_screen, name='category'),
    path('category-datatable/', category.load_category_table, name='category_datatable'),
    path('add-new-category/', category.add_new_category),
    path('change-category-status/', category.change_category_status),
    path('delete-category-detail/', category.delete_category_detail),
    path('show-category-data/', category.edit_category_data),
    path('update-category-data/', category.update_category_data),



    url(r'^ColdStorage/', views.ColdStorage, name='ColdStrage'),
    url(r'^DispatchDepot/', views.DispatchDepot, name='DispatchDepot'),
    url(r'^ServiceCity/', views.ServiceCity, name='ServiceCity'),
    url(r'^Warehouse/', views.Warehouse, name='Warehouse'),
    url(r'^page_ecom_customer_view/', views.page_ecom_customer_view),
    url(r'^page_ecom_dashboard/', views.page_ecom_dashboard),
    url(r'^page_ecom_order_view/', views.page_ecom_order_view),
    url(r'^page_ecom_orders/', views.page_ecom_orders),
    url(r'^page_ecom_products/', views.page_ecom_products),
    url(r'^page_ecom_product_edit/', views.page_ecom_product_edit),
]
