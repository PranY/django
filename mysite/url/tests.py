from django.test import TestCase
from url.views import index, redirect
from url.models import Url


class SimpleTest(TestCase):

	def test_url_short_is_correct(self):
		"""
		Tests whether the short URL generated match with database 
		entry for corresponding input URL
		"""
		response = self.client.post('/', {'url': 'http://google.com'})
		new = response.content.split('/')[-1]
		obj = Url.objects.reverse()[0]
		self.assertEqual(new,obj.short)

	def test_url_is_not_valid(self):
		"""
		Tests input URL starts with http:// or not 
		"""

		response = self.client.post('/', {'url': 'http://google.com'})
		obj = Url.objects.reverse()[0]
		self.assertEqual(obj.url.startswith("http://"), True)

	def test_redirect_is_working(self):
		response_self = self.client.post('/', {'url': 'http://google.com'})
		obj = Url.objects.reverse()[0]
		new = response_self.content.split('/')[-1]
		print new
		response_redirect = self.client.get('/',{'url' : '/'+new})
		print response_redirect
		self.assertRedirects(response_redirect, obj.url)