import unittest

class TestStringMethods(unittest.TestCase):
	def setUp(self):
		#Initialize your data here, for example setup database connection
		pass

	def tearDown(self):
		#Cleanup the test here, for example cancel database transactions
		pass

	#every other non magic/special method is a test case
	def test_upper(self):
		self.assertEqual('foo'.upper(), 'FOO')

	def test_isupper(self):
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())

	def test_split(self):
		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'world'])
		# check that s.split fails when the separator is not a string
		with self.assertRaises(TypeError):
			s.split(2)
