import unittest

from graph.graphs import Graph
from isomorphism.ColorRefinementChecker import ColorRefinementChecker


class ColorRefinementCheckerTest(unittest.TestCase):

	def test_Equals(self):
		checker = ColorRefinementChecker()

		g1 = Graph(10)
		g1.addedge(g1.findvertex(0), g1.findvertex(1))

		g2 = Graph(10)
		g2.addedge(g2.findvertex(0), g2.findvertex(2))

		g3 = Graph(9)
		g3.addedge(g3.findvertex(0), g3.findvertex(1))

		g4 = Graph(9)
		g4.addedge(g4.findvertex(0), g4.findvertex(1))
		g4.addedge(g4.findvertex(0), g4.findvertex(2))
		g4.addedge(g4.findvertex(0), g4.findvertex(3))

		g5 = Graph()
		g6 = Graph()

		self.assertTrue(checker.isIsomorphic(g1, g2))
		self.assertFalse(checker.isIsomorphic(g1, g3))
		self.assertFalse(checker.isIsomorphic(g2, g3))
		self.assertFalse(checker.isIsomorphic(g3,g4))
		self.assertFalse(checker.isIsomorphic(g1, g5))
		self.assertTrue(checker.isIsomorphic(g5, g6))