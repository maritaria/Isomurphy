from graph.graphs import Graph, Vertex


class Explorer:
	def __init__(self, g: Graph, targetAttribute: str):
		self._graph = g
		self._targetAttr = targetAttribute

	def explore(self, start: Vertex) -> Graph:
		raise NotImplementedError()

	def mark(self, v: Vertex, value: int):
		setattr(v, self._targetAttr, value)

	def prepareClone(self, defaultMark : int) -> Graph:
		cloned = self._graph.clone()
		for v in cloned.V():
			self.mark(v, defaultMark)
		return cloned


class DfsExplorer(Explorer):

	def explore(self, start: Vertex) -> Graph:
		cloned = self.prepareClone(-1)
		clonedStart = cloned.findvertex(start.label())
		explored = []
		stack = [clonedStart]
		while len(stack) > 0:
			v = stack.pop()
			explored.append(v)
			self.mark(v, len(explored) - 1)
			for neighbor in v.nbs():
				if neighbor not in explored:
					stack.append(neighbor)
		return cloned


class BfsExplorer(Explorer):
	def __init__(self, g: Graph, targetAttribute: str):
		super().__init__(g, targetAttribute)

	def explore(self, start: Vertex) -> Graph:
		cloned = self.prepareClone(-1)
		clonedStart = cloned.findvertex(start.label())
		explored = []
		stack = [clonedStart]
		while len(stack) > 0:
			v = stack.pop(0)
			explored.append(v)
			self.mark(v, len(explored) - 1)
			for neighbor in v.nbs():
				if neighbor not in explored:
					stack.append(neighbor)
		return cloned