import numpy as np

def friendship(n):
	"""Returns the adjacency matrix of a friendship graph F(n)."""
	if n < 1:
		return None
	size = 2*n+1
	adjacency = np.zeros((size, size))
	for i in xrange(1,n+1):
		adjacency[0][i] = 1
		adjacency[i][0] = 1
		adjacency[0][n+i] = 1
		adjacency[n+i][0] = 1
		adjacency[i][n+i] = 1
		adjacency[n+i][i] = 1
	return adjacency