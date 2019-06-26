from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.Index.as_view(), name='index'),
    path('register/', views.register_user, name='register'),
    path('add-new-reg-user/', views.add_new_reg_user),
    path('verify-primary-contact/', views.verify_primary_contact),
    path('get-city-data/', views.get_city_data),
]
