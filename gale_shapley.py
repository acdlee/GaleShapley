#Implementation of the Gale-Shapley Algorithm. 
#Guarentees a stable, perfect matching between employers E
#and applicants A. 

#Debug tool
DEBUG_MATCHES_INIT = 0

#Parameters A for the list of applicants and E
#for the list of employers. 
def GS(A, E):
	#let matches be a hash containing the matches
	#each of each applicant and employer.
	#default value of 0 to indicate being "free" (no match). 
	matches = {name: 0 for name in A+E}
	print(matches)
	if DEBUG_MATCHES_INIT:
		return matches
