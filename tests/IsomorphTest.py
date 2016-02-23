import unittest
from graph.graphIO import loadgraphs
from isomorphism.ColorRefinementChecker import ColorRefinementChecker

class IsomorphTest(unittest.TestCase):

	def setUp(self):
		self._checker = ColorRefinementChecker()

	def test_Quick(self):
		self._graphs = loadgraphs('data\colorref_smallexample_4_7.grl')
		self.runTest(0, 0, True)
		self.runTest(0, 1, False)
		self.runTest(0, 2, True)
		self.runTest(0, 3, False)
		self.runTest(1, 1, True)
		self.runTest(1, 2, False)
		self.runTest(1, 3, True)
		self.runTest(2, 2, True)
		self.runTest(2, 3, False)
		self.runTest(3, 3, True)

	def runTest(self, index1 : int, index2 : int, expectedResult : bool):
		g1 = self._graphs[0][index1]
		g2 = self._graphs[0][index2]
		result = self._checker.isIsomorphic(g1,g2)
		self.assertEqual(expectedResult, result)
