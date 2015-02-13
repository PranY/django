from django.test import TestCase
from url.views import index, redirect


class SimpleTest(TestCase):

	def test_index(self):
		response = self.client.get('http://localhost:8000/')
		self.assertEqual(response.status_code, 200)

	def test_redirect(self):
		response = self.client.get('http://localhost:8000/')
		self.assertEqual(response.status_code, 200)