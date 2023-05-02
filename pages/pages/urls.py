from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
	# Adding our AboutPageView to our urls
	path("about/", AboutPageView.as_view(), name = "about"),
	# Since we're using class-based views, we add as_view to the HomePageView
	path("", HomePageView.as_view(), name = "home"),
]

