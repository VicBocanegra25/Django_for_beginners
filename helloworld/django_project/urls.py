from django.contrib import admin
from django.urls import path, include

# By creating this pattern, whenever a user visits the homepage, they will be first routed to the pages app and then to the homePageView
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")), 
]