from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path("vendors/", vendor_list, name="vendors"),
    path("vendors/<int:id>/", vendor_details, name="vendor_details"),
     
    path("users/", user_list, name="users"),
    path("users/<int:id>/", user_details, name="user_details"),

    path("transactions/", transaction_list, name="transactions"), 
    path("transactions/<int:id>/", transaction_details, name="transaction_details"), 
]

urlpatterns = format_suffix_patterns(urlpatterns)