# import all the required libraries
from django.test import TestCase
import json
from purbeurre.models import Categories, Products
from purbeurre.management.commands.db_loading import Command


# db_loading command
class CommandTestCase(TestCase):
	"""
	Tests the db_loading command that updates the database
	"""
	def setUp(self):
		"""
		Limit to one category to explore
		"""
		self.com = Command()
		self.category = "Fromages"
		prod_data = {
			"product_name": "SKYR",
			"product_id": 3033490004743,
			"product_url": "http://",
			"product_img": "http://",
			"nutrition_score": "a",
			"fat": 0.2,
			"saturated_fat": 0.1,
			"salt": 0.09,
			"sugar": 3.9,
			"categories": ['Produits laitiers']
			}
		self.content = [prod_data]

	def test_handle(self):
		json_results = open("../P8_v2/tests/mockup/off.json")
		mock = json.load(json_results)

		def mockreturn(a):
			return mock

		# Execute the command
		self.com._request_api = mockreturn
		self.com.handle()

		# database must have been populated
		self.assertEqual(Products.objects.all().exists(), True)
		self.assertEqual(Categories.objects.all().exists(), True)