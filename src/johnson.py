import numpy as np

def johnson(n, k):
	"""Returns the adjacency matrix of a johnson graph J(n,k)."""
	subsets = filter(lambda x: len(x) == k, powerset(range(n)))
	size = len(subsets)
	adjacency = np.zeros((size, size))
	for i in xrange(size):
		for j in xrange(i+1, size):
			if len(subsets[i].intersection(subsets[j])) == k-1:
				adjacency[i][j] = 1
				adjacency[j][i] = 1
	return adjacency

def powerset(A):
	"""Returns the powerset of a given set."""
	P = [set([])]
	for i in xrange(len(A)):
		for j in xrange(len(P)):
			subset = P[j].copy()
			subset.add(i)
			P.append(set(subset))
	return P