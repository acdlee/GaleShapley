import unittest

from gale_shapley import GS as gs


class TestGS(unittest.TestCase):
	def test_matches_intuitive(self):
		"""
		Test the accuracy of the algorithm with
		an intuitive preference list.
		"""
		#let's create our input arrays
		prefA = [[3, 1, 2],[2, 3, 1],[3, 2, 1]]
		prefB = [[2, 3, 1],[3, 2, 1],[1, 2, 3]]

		#Since prefA[0] and prefB[2] prefer each other, 
		#they will match. Since prefA[1] prefers prefB[1], 
		#they will initially match, however, since 
		#prefA[2] prefers prefB[1] and, more importantly, 
		#prefB[1] prefers prefA[2] over prefA[1], there will
		#be an unmatching between the second matched pair. 

		#expected result
		expected_result = ([2, 0, 1], [1, 2, 0])

		result = gs(prefA, prefB)
		self.assertEqual(result, expected_result)


	def test_complex_matches(self):
		"""
		Test the accuracy of the algorithm with 
		a more involved preference list.
		"""
		prefA = [[1,6,4,3,2,5,7], [4,3,7,1,6,5,2], 
				[1,6,4,2,3,5,7], [7,3,6,2,4,1,5], 
				[1,6,7,2,3,5,4], [4,7,6,1,5,3,2], [1,5,4,3,6,7,2]]
		prefB = [[3,7,4,2,1,5,6],[4,2,7,5,1,3,6],
				[7,2,3,4,1,6,5], [4,6,2,3,1,7,5],
				[6,7,5,2,4,3,1], [5,4,1,7,3,2,6], [7,6,3,4,5,1,2]]

		#expected result
		expected_result = ([2, 3, 1, 7, 6, 4, 5], [3, 1, 2, 6, 7, 5, 4])

		result = gs(prefA, prefB)
		self.assertEqual(result, expected_result)

if __name__ == '__main__':
	unittest.main()


