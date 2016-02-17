import unittest

from graph.explorer import DfsExplorer, BfsExplorer
from graph.graphs import Graph, Vertex


class ExplorerTest(unittest.TestCase):
	def test_dfs(self):
		g = Graph()
		v1 = g.addvertex()
		v2 = g.addvertex()
		v3 = g.addvertex()
		v4 = g.addvertex()
		v5 = g.addvertex()
		e1 = g.addedge(v1, v2)
		e2 = g.addedge(v1, v3)
		e3 = g.addedge(v2, v4)
		expl = DfsExplorer(g, "marker")
		ge = expl.explore(v1)

		def getMarker(v : Vertex) -> int:
			return getattr(ge.findvertex(v.label()), "marker")

		self.assertEqual(getMarker(v1), 0)
		self.assertEqual(getMarker(v2), 1)
		self.assertEqual(getMarker(v3), 3)
		self.assertEqual(getMarker(v4), 2)
		self.assertEqual(getMarker(v5), -1)

	def test_bfs(self):
		g = Graph()
		v1 = g.addvertex()
		v2 = g.addvertex()
		v3 = g.addvertex()
		v4 = g.addvertex()
		v5 = g.addvertex()
		e1 = g.addedge(v1, v2)
		e2 = g.addedge(v1, v3)
		e3 = g.addedge(v2, v4)
		expl = BfsExplorer(g, "marker")
		ge = expl.explore(v1)

		def getMarker(v : Vertex) -> int:
			return getattr(ge.findvertex(v.label()), "marker")

		self.assertEqual(getMarker(v1), 0)
		self.assertEqual(getMarker(v2), 1)
		self.assertEqual(getMarker(v3), 2)
		self.assertEqual(getMarker(v4), 3)
		self.assertEqual(getMarker(v5), -1)