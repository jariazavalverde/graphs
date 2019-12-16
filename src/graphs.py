#!/usr/bin/env python
# -*- coding: utf-8 -*

"""A generator of graphs written in Python and LaTeX.
   https://github.com/jariazavalverde/graphs
"""

from sys import argv
from adjacency import adjacency_functions
from formats import format_functions



# MAIN FUNCTION

def main():
	if len(argv) > 1:
		family = argv[1]
		output = None
		format = "numpy"
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
		# Check options
		for i in xrange(2+len(arguments), len(argv), 2):
			if argv[i] == "-o" or argv[i] == "-output":
				output = argv[i+1]
			elif argv[i] == "-f" or argv[i] == "-format":
				format = argv[i+1]
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
		string = format_functions[format](G)
		if output is None:
			print(string)
		else:
			f = open(output, "w")
			f.write(string)
			f.close()
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