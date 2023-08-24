from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


urlpatterns = [
    path("admin/", admin.site.urls),
    path('healthcheck/', lambda r: HttpResponse("Up and running ...", status=200)),

    path("perks/v1/data/", include('perks.urls')),

    path("perks/v1/auth/", include('perks.authurls')),
]
