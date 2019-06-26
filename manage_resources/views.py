from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class Unit(TemplateView):
    template_name = "manage_resources/Units.html"


# class Category(TemplateView):
#     template_name = "manage_resources/Category.html"



class variant(TemplateView):
    template_name = "manage_resources/variant.html"


class wastageType(TemplateView):
    template_name = "manage_resources/wastageType.html"


class Products(TemplateView):
    template_name = "manage_resources/products.html"


#Todo manage_resources html pages
def ColdStorage(request):
    return render(request, 'manage_location/ColdStorage.html')


def DispatchDepot(request):
    return render(request, 'manage_location/DispatchDepot.html')


def ServiceCity(request):
    return render(request, 'manage_location/ServiceCity.html')


def Warehouse(request):
    return render(request, 'manage_location/Warehouse.html')


#Todo E-Commerce html pages

def page_ecom_customer_view(request):
    return render(request, 'ecommerce/page_ecom_customer_view.html')


def page_ecom_dashboard(request):
    return render(request, 'ecommerce/page_ecom_dashboard.html')


def page_ecom_order_view(request):
    return render(request, 'ecommerce/page_ecom_order_view.html')


def page_ecom_orders(request):
    return render(request, 'ecommerce/page_ecom_orders.html')


def page_ecom_product_edit(request):
    return render(request, 'ecommerce/page_ecom_product_edit.html')


def page_ecom_products(request):
    return render(request, 'ecommerce/page_ecom_products.html')