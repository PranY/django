from django.test import TestCase
from url.views import index, redirect
from url.models import Url


class SimpleTest(TestCase):

	def test_url_short_is_correct(self):
		response = self.client.post('/', {'url': 'http://google.com'})
		new = response.content.split('/')[-1]
		obj = Url.objects.reverse()[0]
		self.assertEqual(new,obj.short)

	def test_url_is_not_valid(self):
		response = self.client.post('/', {'url': 'http://google.com'})
		obj = Url.objects.reverse()[0]
		self.assertEqual(obj.url.startswith("http://"), True)
