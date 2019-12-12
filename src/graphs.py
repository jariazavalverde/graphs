import numpy as np
from sys import argv
from johnson import johnson

graph_families = {
	"johnson": (johnson, [("n", int), ("k", int)], (lambda n, k: n > 0 and k > 0 and n > k), "n > 0, k > 0, n > k")
}

def main():
	if len(argv) > 1:
		family = argv[1]
		# check existence of family
		if family not in graph_families:
			print("the family " + argv[1] + " does not exist")
			return 1
		# get generator and type of parameters
		gen, arguments, precondition, error = graph_families[family]
		# check existence of parameters
		if len(argv)-2 < len(arguments):
			print("wrong number of arguments")
			return 2
		# get parameters
		params = []
		for i in xrange(len(arguments)):
			params.append(arguments[i][1](argv[2+i]))
		# check parameters
		if not precondition(*params):
			print("incorrect parameters: " + error)
			return 3
		# generate graph
		G = gen(*params)
		# print graph
		np.set_printoptions(threshold = np.inf)
		print(G)
	return 0

if __name__ == "__main__":
	main()