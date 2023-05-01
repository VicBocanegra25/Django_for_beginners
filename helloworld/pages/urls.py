# Import the path module from Django to power our URL pattern
from django.urls import path
# Telling Django to look within the current directory for a views.py file and import homePageView
from .views import homePageView

"""
Our urlpattern has three parts: 
A) A python regex for the empty string ""
B) A reference to the view homePageView
C) An optional named URL pattern called "home"
"""
urlpatterns = [
    path("", homePageView, name="home"),
]