#!/usr/bin/env python
# -*- coding: utf-8 -*

"""A generator of graphs written in Python and LaTeX.
   https://github.com/jariazavalverde/graphs
"""

import numpy as np



# ADJACENCY MATRICES

def complete(n):
	"""Returns the adjacency matrix of a complete graph K(n).
	   For: n > 0."""
	if n < 1:
		return None
	size = n
	adjacency = np.ones((size,size))
	for i in xrange(size):
		adjacency[i][i] = 0
	return adjacency

def friendship(n):
	"""Returns the adjacency matrix of a friendship graph F(n).
	   For: n > 0."""
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

def johnson(n, k):
	"""Returns the adjacency matrix of a johnson graph J(n,k).
	   For: n > 0, k > 0, k < n."""
	if n < 1 or k < 1 or k > n:
		return None
	subsets = filter(lambda x: len(x) == k, _powerset(range(n)))
	size = len(subsets)
	adjacency = np.zeros((size, size))
	for i in xrange(size):
		for j in xrange(i+1, size):
			if len(subsets[i].intersection(subsets[j])) == k-1:
				adjacency[i][j] = 1
				adjacency[j][i] = 1
	return adjacency

def petersen(n, k):
	"""Returns the adjacency matrix of a generalized petersen graph GP(n,k).
	   For: n > 0, k > 0, k < n/2."""
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

def windmill(k, n):
	"""Returns the adjacency matrix of a windmill graph Wd(k, n).
	   For: k > 1, n > 1."""
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



# HANDLING AND TYPE CHECKING

adjacency_functions = {
	"complete": (complete, [("n", int)], "n > 0"),
	"friendship": (friendship, [("n", int)], "n > 0"),
	"johnson": (johnson, [("n", int), ("k", int)], "n > 0, k > 0, k < n"),
	"petersen": (petersen, [("n", int), ("k", int)], "n > 0, k > 0, k < n/2"),
	"windmill": (windmill, [("k", int), ("n", int)], "k > 1, n > 1")
}



# AUXILIAR OPERATIONS

def _powerset(A):
	"""Returns the powerset of a given set."""
	P = [set([])]
	for i in xrange(len(A)):
		for j in xrange(len(P)):
			subset = P[j].copy()
			subset.add(i)
			P.append(set(subset))
	return P



# AUTHORSHIP INFORMATION

__author__ = "José Antonio Riaza Valverde"
__copyright__ = "Copyright 2019, José Antonio Riaza Valverde"
__credits__ = ["José Antonio Riaza Valverde"]
__license__ = "BSD 3-Clause"
__version__ = "1.0.0"
__maintainer__ = "José Antonio Riaza Valverde"
__email__ = "riaza.valverde@gmail.com"
__status__ = "Development"