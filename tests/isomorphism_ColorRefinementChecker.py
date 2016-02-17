import unittest

from graph.graphs import Graph
from isomorphism.ColorRefinementChecker import ColorRefinementChecker


class ColorRefinementCheckerTest(unittest.TestCase):

	def test_Equals(self):
		checker = ColorRefinementChecker()

		def link(g : Graph, s : int, t : int):
			g.addedge(g.findvertex(s), g.findvertex(t))

		g1 = Graph(10)
		link(g1, 0, 1)

		g2 = Graph(10)
		link(g2, 0, 2)

		g3 = Graph(9)
		link(g3, 0, 1)

		g4 = Graph(9)
		link(g4, 0, 1)
		link(g4, 0, 2)
		link(g4, 0, 3)

		g5 = Graph()
		g6 = Graph()

		g7 = Graph(9)
		link(g7, 5, 4)
		link(g7, 4, 3)
		link(g7, 4, 7)

		self.assertTrue(checker.isIsomorphic(g1, g2))
		self.assertFalse(checker.isIsomorphic(g1, g3))
		self.assertFalse(checker.isIsomorphic(g2, g3))
		self.assertFalse(checker.isIsomorphic(g3,g4))
		self.assertFalse(checker.isIsomorphic(g1, g5))
		self.assertTrue(checker.isIsomorphic(g5, g6))
		self.assertTrue(checker.isIsomorphic(g4, g7))