# We'll instanciate two SimpleTestCase objects to check that our urls return
# status 200.

# Import the SimpleTestCase class from Django's testing framework
from django.test import SimpleTestCase
# Importing reverse to test the url name for each page
from django.urls import reverse

# Define a test case class for the homepage by inheriting from SimpleTestCase
class HomepageTests(SimpleTestCase):
	# Define a test method to check if the homepage URL exists at the correct
	# location
	def test_url_exists_at_correct_location(self):
		# Send an HTTP GET request to the root URL ("/") using the test client
		response = self.client.get("/")
		# Assert that the response status code is 200 (HTTP OK)
		self.assertEqual(response.status_code, 200)

	# Define a test method to check if the homepage URL is available by name
	def test_url_available_by_name(self):
		# Send an HTTP GET request to the reversed name "home"
		response = self.client.get(reverse("home"))
		self.assertEqual(response.status_code, 200)

	# Define a test method to check if the correct template is used for the
	# homepage
	def test_template_name_correct(self):
		# Send an HTTP GET request to the homepage URL using the test client
		# and the reverse function to look up the URL by its name
		response = self.client.get(reverse("home"))
		# Assert that the response used the "home.html" template
		self.assertTemplateUsed(response, "home.html")

	# Define a test method to check if the content of the homepage template is
	# correct
	def test_template_content(self):
		# Send an HTTP GET request to the homepage URL using the test client
		# and the reverse function to look up the URL by its name
		response = self.client.get(reverse("home"))
		# Assert that the response contains the expected content
		self.assertContains(response, "<h1>Homepage</h1>")

# The tests are repeated for the About Page, note the response URL ("/about/")
class AboutpageTests(SimpleTestCase):
	def test_url_exists_at_correct_location(self):
		response = self.client.get("/about/")
		self.assertEqual(response.status_code, 200)

	# Define a test method to check if the about URL is available by name
	def test_url_available_by_name(self):
		# Send an HTTP GET request to the reversed name "about"
		response = self.client.get(reverse("about"))
		self.assertEqual(response.status_code, 200)

	def test_template_name_correct(self):
		response = self.client.get(reverse("about"))
		self.assertTemplateUsed(response, "about.html")

	def test_template_content(self):
		response = self.client.get(reverse("about"))
		self.assertContains(response, "<h1>About page</h1>")
