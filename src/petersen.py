import numpy as np

def petersen(n, k):
	"""Returns the adjacency matrix of a generalized petersen graph GP(n,k)."""
	if n < 1 or k < 1 or float(k) >= float(n)/2.0:
		return None
	# u_0, ..., u_{n-1}, v_0, ..., v_{n-1}
	size = n*2
	adjacency = np.zeros((size, size))
	for i in xrange(n):
		# u_i <-> u_{i+1}
		adjacency[i][(i+1) % n] = 1
		adjacency[(i+1) % n][i] = 1
		# u_i <-> v_i
		adjacency[i][i+n] = 1
		adjacency[i+n][i] = 1
		# v_i <-> v_{i+k}
		adjacency[n+i][n + (i+k) % n] = 1
		adjacency[n + (i+k) % n][n+i] = 1
	return adjacency