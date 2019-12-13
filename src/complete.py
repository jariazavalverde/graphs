import numpy as np

def complete(n):
	"""Returns the adjacency matrix of a complete graph K(n)."""
	if n < 1:
		return None
	size = n
	adjacency = np.ones((size,size))
	for i in xrange(size):
		adjacency[i][i] = 0
	return adjacency