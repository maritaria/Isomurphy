from graph.graphs import Graph, Vertex

#TODO: Create unit tests to confirm behaviour

class Explorer:
	def explore(self, g : Graph, start : Vertex)-> Graph:
		raise NotImplementedError();

class DfsExplorer(Explorer):
	def explore(self, g : Graph, start : Vertex)-> Graph:
		result = g.clone()
		explored = []
		stack = [start]
		while(len(stack) > 0):
			v = stack.pop()
			explored.append(v)
			v._label = len(explored)
			for neighbor in v.nbs():
				if neighbor not in explored:
					stack.append(neighbor)

class BfsExplorer(Explorer):
	def explore(self, g : Graph, start : Vertex)-> Graph:
		result = g.clone()
		explored = []
		stack = [start]
		while(len(stack) > 0):
			v = stack.pop(0)
			explored.append(v)
			v._label = len(explored)
			for neighbor in v.nbs():
				if neighbor not in explored:
					stack.append(neighbor)
