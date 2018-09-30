import unittest

#following https://docs.python.org/2/library/unittest.html

class TestStringMethods(unittest.TestCase):
	def setUp(self):	#called before each test case
	 	print("\nsetUp")

	def suite():
		stringTestSuite = unittest.TestSuite()		#suite object to hold tests
		stringTestSuite.addTest("test_isupper")		#individual tests
		stringTestSuite.addTest("test_split")
		stringTestSuite.addTest("test_upper")
		return stringTestSuite						#return the suite

	def suite2():
		#identical functionally to suite()
		tests=['test_isupper','test_split','test_upper']	#individual tests listed
		return unittest.TestSuite(TestStringMethods,tests)	#return the suite

	def oldTestInterface():
		#runs a test without requiring every test to be rewritten in new style
		test = unittest.FunctionTestCase(test_upper,setUp=setUp,tearDown=tearDown)

		
	@unittest.skipIf(False,"reason True")	#will skip running this method if True
	def test_upper(self):
		self.assertEqual('foo'.upper(),'FOO')

	@unittest.skipUnless(True,"reason False")	#will skip if false
	def test_isupper(self):
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())

	def test_split(self):
		s='hello world'		#because why not
		self.assertEqual(s.split(), ['hello', 'world'])
		with self.assertRaises(TypeError):
			s.split(2)

	@unittest.skip("skipping test_to_not_run()")		#will always skip this test
	def test_to_not_run(self):
		print("shouldn't run")

	def tearDown(self):	#called after each test case
		print("tearDown")
		#NOTE: nomenclature setUp() + tearDown() = fixture

class OtherTests(unittest.TestCase):
	def runTest(self):
		pass

	@unittest.expectedFailure
	def test_fail(self):
		print("fail!")
		self.assertEqual(1,0,"broken test case")

if __name__ == '__main__':
	#unittest.main()		#functional, equivalent to $ python -m unittest testing.py
	#equivalent to $ python -m unittest -vv testing.py 
	suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
	unittest.TextTestRunner(verbosity=2).run(suite)	#an elegant weapon, of a more civilized age
	
	suite = unittest.TestLoader().loadTestsFromTestCase(OtherTests)
	unittest.TextTestRunner().run(suite) 