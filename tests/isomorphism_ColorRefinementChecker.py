import unittest

from graph.graphs import Graph
from isomorphism.ColorRefinementChecker import ColorRefinementChecker


class ColorRefinementCheckerTest(unittest.TestCase):

	def setUp(self):
		self.checker = ColorRefinementChecker()

		def link(g : Graph, s : int, t : int):
			g.addedge(g.findvertex(s), g.findvertex(t))

		self.g1 = Graph(10)
		link(self.g1, 0, 1)

		self.g2 = Graph(10)
		link(self.g2, 0, 2)

		self.g3 = Graph(9)
		link(self.g3, 0, 1)

		self.g4 = Graph(9)
		link(self.g4, 0, 1)
		link(self.g4, 0, 2)
		link(self.g4, 0, 3)

		self.g5 = Graph()
		self.g6 = Graph()

		self.g7 = Graph(9)
		link(self.g7, 5, 4)
		link(self.g7, 4, 3)
		link(self.g7, 4, 7)

	def test_OneEdge(self):
		self.assertTrue(self.checker.isIsomorphic(self.g1, self.g2))
	def test_SizeMismatch(self):
		self.assertFalse(self.checker.isIsomorphic(self.g1, self.g3))
		self.assertFalse(self.checker.isIsomorphic(self.g2, self.g3))
	def test_MoreEdges(self):
		self.assertFalse(self.checker.isIsomorphic(self.g3,self.g4))
	def test_OtherEmpty(self):
		self.assertFalse(self.checker.isIsomorphic(self.g1, self.g5))
	def test_BothEmpty(self):
		self.assertTrue(self.checker.isIsomorphic(self.g5, self.g6))
	def test_Equal(self):
		self.assertTrue(self.checker.isIsomorphic(self.g4, self.g7))