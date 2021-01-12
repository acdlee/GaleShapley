#Implementation of the Gale-Shapley Algorithm. 
#Guarentees a stable, perfect matching between employers E
#and applicants A. 


#A is the 2D array preference list for applicants.
#Similarly, E is the 2S preference list for employers.
#Specifically, A[0] has the priority list (pref list) for
#applicant 0
def GS(A, E):
	#we'll (for simplicity of the implementation) assume 
	#the sizes of both A and E are the same.
	N = len(A)				#number of applicants (or employers)
	matches_A, matches_B = [-1]*N, [-1]*N 	#list of matches; -1 => free
	num_free = N 			#number of unmatched applicants

	iter_a = 1000

	#while there is an unmatched applicant
	while num_free:
		curr_applicant = -1
		for i in range(len(matches_A)):
			#find the unmatched applicant
			if matches_A[i] == curr_applicant:
				curr_applicant = i
				break

		#find the employer with the highest preference for curr_applicant
		best_employer = find_best_employer(A[curr_applicant])

		if not iter_a:
			print(best_employer)
			print(curr_applicant)
			print(matches_A)
			print(matches_B)
			input()
		else:
			iter_a -= 1

		if matches_B[best_employer] == -1:
			#if that employer is free, create a new match
			match(curr_applicant, best_employer, matches_A, matches_B)
			num_free -= 1
		else:
			#check if employer prefers curr_applicant over their match
			curr_applicant_rank = E[best_employer][curr_applicant]
			curr_match_rank = E[best_employer][matches_B[best_employer]]
			
			#NOTE: for this implementation, a lower numeric value
			#is equivalent to a higher rank
			if curr_match_rank > curr_applicant_rank:
				old_applicant = matches_B[best_employer]
				#create a new matching
				match(curr_applicant, best_employer, matches_A, matches_B)
				#unmatch the old matching
				#need the old applicant, not
				#currapplicant
				matches_A[old_applicant] = -1

		#remove best_employer from curr_applicant's pref
		#list, regardless out the proposal's outcome
		#See *1* at the bottom for more details
		A[curr_applicant][best_employer] = N + 1

	return matches_A, matches_B

#helper function to find the current applicant's 
#highest-ranked employer. 
def find_best_employer(pref_list):
	index = 0

	#find the index of the highest (lowest numeric value) preference
	for i in range(1, len(pref_list)):
		if pref_list[index] > pref_list[i]:
			index = i

	return index

#helper function to set a matching between an employer and
#an applicant
def match(curr_applicant, employer, matches_A, matches_B):
	matches_A[curr_applicant] = employer
	matches_B[employer] = curr_applicant


prefA = [[3, 1, 2],[2, 3, 1],[3, 2, 1]]
prefB = [[2, 3, 1],[3, 2, 1],[1, 2, 3]]

print(GS(prefA, prefB))

#*1*
#Since we only select an employer in find_best_employer
#when the current index value is greater than
#another index value, the function, 
#given a value of N for some employer e,
#will never return employer e. 
#Moreover, the function will never be called 
#with an preference list with all values N
#(proof 1.3).