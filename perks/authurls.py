from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import login, signup

urlpatterns = [
    re_path('login/', login, name='login'),

    re_path('signup/', signup, name='signup'),
]

urlpatterns = format_suffix_patterns(urlpatterns)