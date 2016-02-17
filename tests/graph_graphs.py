import unittest

from graph.graphs import Graph


class GraphTest(unittest.TestCase):

	def test_edge_tracking(self):
		#initialize graph
		g = Graph()
		v1 = g.addvertex(1)
		v2 = g.addvertex(2)
		v3 = g.addvertex(2)

		e1 = g.addedge(v1, v2)
		self.assertIn(v2, v1.nbs())
		#Deleted edges disconnect neighbors
		g.deledge(e1)
		self.assertNotIn(v2, v1.nbs())

		e2 = g.addedge(v1,v3)
		e3 = g.addedge(v1,v3)

		#Deleted edges dont disconnect if another edge remains
		g.deledge(e3)
		self.assertIn(v3, v1.nbs())

		#Deleted edges not in neighbors
		g.delvertex(v3)
		self.assertNotIn(v3, v1.nbs())