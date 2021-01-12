import unittest

from gale_shapley import GS as gs

#constant to note any initialization tests
#that were passed. 
PASSED = 1

class TestGS(unittest.TestCase):
	def __init__(self):
		self.A = ["Chris", "Twisted Fate", "Ori"]
		self.E = ["CompA", "CompB", "CompC"]

		'''
		input interpretation:
		*prefA[0][0] is Chris's preference value of CompA
		*If prefA[0][0] = 1, than Chris prefers CompA to all other companies.
		'''

		#let's create our input arrays
		self.prefA = [[3, 1, 2],[2, 3, 1],[3, 2, 1]]
		self.prefB = [[2, 3, 1],[3, 2, 1],[1, 2, 3]]

	def test_matches_init(self):
		"""
		Test the accuracy in the initlization of the
		hash matches. 
		"""
		result = gs(self.prefA, self.prefB)
		self.assertEqual(result, data)





if __name__ == '__main__':
	unittest.main()


