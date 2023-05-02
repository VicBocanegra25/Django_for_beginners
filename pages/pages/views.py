from django.views.generic import TemplateView

# The class contains the logic needed to display our template
class HomePageView(TemplateView):
	# Specifying the template's name
	template_name = "home.html"

# Adding a new view for our About page
class AboutPageView(TemplateView):
	template_name = "about.html"