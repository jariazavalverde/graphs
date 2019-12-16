#!/usr/bin/env python
# -*- coding: utf-8 -*

"""A generator of graphs written in Python and LaTeX.
   https://github.com/jariazavalverde/graphs
"""

from sys import argv
import numpy as np
from adjacency import adjacency_functions



# MAIN FUNCTION

def main():
	if len(argv) > 1:
		family = argv[1]
		# Check existence of the family
		if family not in adjacency_functions:
			print("the family " + argv[1] + " does not exist")
			return 1
		# Get generator and type of parameters
		gen, arguments, error = adjacency_functions[family]
		# Check existence of parameters
		if len(argv)-2 < len(arguments):
			print("wrong number of arguments")
			return 2
		# Get parameters
		params = []
		for i in xrange(len(arguments)):
			params.append(arguments[i][1](argv[2+i]))
		# Generate adjacency matrix
		G = gen(*params)
		# Check parameters
		if G is None:
			print("incorrect parameters for %s graph: %s" % (argv[1], error))
			return 3
		# Print graph
		np.set_printoptions(threshold = np.inf)
		print(G)
	return 0

if __name__ == "__main__":
	main()



# AUTHORSHIP INFORMATION

__author__ = "José Antonio Riaza Valverde"
__copyright__ = "Copyright 2019, José Antonio Riaza Valverde"
__credits__ = ["José Antonio Riaza Valverde"]
__license__ = "BSD 3-Clause"
__version__ = "1.0.0"
__maintainer__ = "José Antonio Riaza Valverde"
__email__ = "riaza.valverde@gmail.com"
__status__ = "Development"