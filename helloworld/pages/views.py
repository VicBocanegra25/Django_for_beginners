# Importing the HttpResponse method so we can return a response object to the user.
from django.http import HttpResponse

# Whenever the view function is called, return the text Hello World!
def homePageView(request):
    return HttpResponse("Hello, World!")