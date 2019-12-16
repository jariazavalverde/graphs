#!/usr/bin/env python
# -*- coding: utf-8 -*

"""A generator of graphs written in Python and LaTeX.
   https://github.com/jariazavalverde/graphs
"""

import numpy as np



# FORMATS

def format_c(adjacency):
	"""Returns a string representation of the given graph in C format."""
	size = adjacency.shape[0]
	string = "int adjacency[%d][%d] = {\n" % (size, size)
	for i in xrange(size):
		string += "\t{" + ", ".join(map(str, np.array(adjacency[i], dtype=int).tolist())) + "}"
		if i+1 < size:
			string += ","
		string += "\n"
	string += "};"
	return string

def format_dimacs(adjacency):
	"""Returns a string representation of the given graph in DIMACS format."""
	string = ""
	size = adjacency.shape[0]
	edges = 0
	for i in xrange(size):
		for j in xrange(i, size):
			if adjacency[i][j]:
				string += "\ne %d %d" % ((i+1), (j+1))
				edges += 1
	string = ("p edge %d %d" % (size, edges)) + string
	string = "c https://github.com/jariazavalverde/graphs\n" + string
	return string

def format_list(adjacency):
	"""Returns a string representation of the given graph in Python format."""
	return str(np.array(adjacency, dtype=int).tolist())

def format_numpy(adjacency):
	"""Returns a string representation of the given graph in numpy format."""
	return str(np.array(adjacency, dtype=int))



# HANDLING

format_functions = {
	"c": format_c,
	"dimacs": format_dimacs,
	"haskell": format_list,
	"javascript": format_list,
	"prolog": format_list,
	"python": format_list,
	"numpy": format_numpy
}




# AUTHORSHIP INFORMATION

__author__ = "José Antonio Riaza Valverde"
__copyright__ = "Copyright 2019, José Antonio Riaza Valverde"
__credits__ = ["José Antonio Riaza Valverde"]
__license__ = "BSD 3-Clause"
__version__ = "1.0.0"
__maintainer__ = "José Antonio Riaza Valverde"
__email__ = "riaza.valverde@gmail.com"
__status__ = "Development"