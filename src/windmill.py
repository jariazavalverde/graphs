import numpy as np

def windmill(k, n):
	"""Returns the adjacency matrix of a windmill graph Wd(k, n)."""
	if k < 2 or n < 2:
		return None
	size = (k-1)*n+1
	adjacency = np.zeros((size, size))
	for i in xrange(n):
		for j in xrange(k-1):
			z = i*(k-1)+j+1
			adjacency[0][z] = 1
			adjacency[z][0] = 1
			for l in xrange(k-1):
				x = i*(k-1)+j+1
				y = i*(k-1)+l+1
				if x != y:
					adjacency[x][y] = 1
					adjacency[y][x] = 1
	return adjacency