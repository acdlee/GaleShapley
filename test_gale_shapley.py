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

		#since this input is structured as a priority queue
		#(ie, prefA[0][0] is the candidate number for the highest
		#rated candidate), we have to restructure the input
		new_prefA, new_prefB = self.restructure_input(prefA, prefB)

		#expected result
		expected_result = ([2, 3, 1, 7, 6, 4, 5], [3, 1, 2, 6, 7, 5, 4])

		result = gs(prefA, prefB)
		self.assertEqual(result, expected_result)

	def restructure_input(self, prefA, prefB):
		"""
		Takes the current input, where prefA[0][0] is the 
		candidate number of the highest favored candidate
		for employer 0, and restructures it such that prefA[0][0]
		is the ranking of candidate 0 for employer 0. 

		O(n) time to restrucutre each individual list. 
		2n total lists that need restructuring. 
		Time complexity of restructuring the input:
			O(n^2)
		Time complexity of restructuring the input and
		running the algorithm:
			T(n) = O(n^2 + n^2),
			T(n) = O(n^2)
		"""
		new_prefA = [self.restructure_helper(lst) for lst in prefA]
		new_prefB = [self.restructure_helper(lst) for lst in prefB]

		return new_prefA, new_prefB

	def restructure_helper(self, lst):
		"""
		Helper function for restructure_input().
		Most of the grunt work is done here.
		"""
		n = len(lst)
		tmp_lst = [0] * n
		for i in range(0, n):
			tmp_lst[lst[i] - 1] = i + 1
		return tmp_lst

if __name__ == '__main__':
	unittest.main()


