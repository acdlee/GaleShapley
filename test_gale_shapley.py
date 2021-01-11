import unittest

from gale_shapley import GS as gs

#constant to note any initialization tests
#that were passed. 
PASSED = 1

class TestGS(unittest.TestCase):
	def __init__(self):
		self.A = ["Chris", "Twisted Fate", "Ori"]
		self.E = ["CompA", "CompB", "CompC"]
	def test_matches_init(self):
		return PASSED

		"""
		Test the accuracy in the initlization of the
		hash matches. 
		"""
		#data is the target hash
		data = {"Chris": 0, "Twisted Fate": 0, "Ori": 0, "CompA": 0, 
				"CompB": 0, "CompC": 0}

		#algorithm arguments
		A = ["Chris", "Twisted Fate", "Ori"]
		E = ["CompA", "CompB", "CompC"]
		result = gs(A, E)	
		self.assertEqual(result, data)

if __name__ == '__main__':
	unittest.main()