#!/usr/bin/env python
# -*- coding: utf-8 -*

"""A generator of graphs written in Python and LaTeX.
   https://github.com/jariazavalverde/graphs
"""

import numpy as np



# FORMATS

def format_dimacs(adjacency):
	"""Returns a string representation of the given graph in DIMACS format."""
	string = ""
	nodes = adjacency.shape[0]
	edges = 0
	for i in xrange(nodes):
		for j in xrange(i, nodes):
			if adjacency[i][j]:
				string += "e %d %d\n" % ((i+1), (j+1))
				edges += 1
	string = ("p edge %d %d\n" % (nodes, edges)) + string
	string = "c https://github.com/jariazavalverde/graphs\n" + string
	return string

def format_python(adjacency):
	"""Returns a string representation of the given graph in Python format."""
	return str(np.array(adjacency, dtype=int).tolist())

def format_numpy(adjacency):
	"""Returns a string representation of the given graph in numpy format."""
	return str(np.array(adjacency, dtype=int))



# HANDLING

format_functions = {
	"dimacs": format_dimacs,
	"python": format_python,
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