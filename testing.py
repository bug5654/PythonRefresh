import unittest

#following https://docs.python.org/2/library/unittest.html

class TestStringMethods(unittest.TestCase):

	def test_upper(self):
		self.assertEqual('foo'.upper(),'FOO')

	def test_isupper(self):
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())

	def test_split(self):
		s='hello world'		#because why not
		self.assertEqual(s.split(), ['hello', 'world'])
		with self.assertRaises(TypeError):
			s.split(2)

if __name__ == '__main__':
	#unittest.main()		#functional, equivalent to $ python -m unittest testing.py
	#equivalent to $ python -m unittest -vv testing.py 
	suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
	unittest.TextTestRunner(verbosity=2).run(suite)	#an elegant weapon, of a more civilized age
