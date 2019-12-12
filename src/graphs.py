import numpy as np
from sys import argv
from johnson import johnson
from petersen import petersen

graph_families = {
	"johnson": (johnson, [("n", int), ("k", int)], "n > 0, k > 0, k < n"),
	"petersen": (petersen, [("n", int), ("k", int)], "n > 0, k > 0, k < n/2")
}

def main():
	if len(argv) > 1:
		family = argv[1]
		# check existence of family
		if family not in graph_families:
			print("the family " + argv[1] + " does not exist")
			return 1
		# get generator and type of parameters
		gen, arguments, error = graph_families[family]
		# check existence of parameters
		if len(argv)-2 < len(arguments):
			print("wrong number of arguments")
			return 2
		# get parameters
		params = []
		for i in xrange(len(arguments)):
			params.append(arguments[i][1](argv[2+i]))
		# generate graph
		G = gen(*params)
		# check parameters
		if G is None:
			print("incorrect parameters for %s graph: %s" % (argv[1], error))
			return 3
		# print graph
		np.set_printoptions(threshold = np.inf)
		print(G)
	return 0

if __name__ == "__main__":
	main()