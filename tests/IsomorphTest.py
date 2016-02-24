import unittest
from graph.graphIO import loadgraphs, writeDOT
from isomorphism.ColorRefinementChecker import ColorRefinementChecker

class IsomorphTest(unittest.TestCase):

	def setUp(self):
		self._checker = ColorRefinementChecker()

	def test_Quick(self):
		self._graphs = loadgraphs('data\colorref_smallexample_4_7.grl')
		self.runTest(0, 1, False)
		self.runTest(0, 2, True)
		self.runTest(0, 3, False)
		self.runTest(1, 2, False)
		self.runTest(1, 3, True)
		self.runTest(2, 3, False)

	def test_Quick1(self):
		self._graphs = loadgraphs('data\colorref_smallexample_4_16.grl')
		self.runTest(0, 1, True)
		self.runTest(0, 2, False)
		self.runTest(0, 3, False)
		self.runTest(1, 2, False)
		self.runTest(1, 3, False)
		self.runTest(2, 3, True)

	def test_Quick2(self):
		self._graphs = loadgraphs('data\colorref_smallexample_6_15.grl')
		self.runTest(0, 1, True)
		self.runTest(0, 2, False)
		self.runTest(0, 3, False)
		self.runTest(0, 4, False)
		self.runTest(0, 5, False)
		self.runTest(1, 2, False)
		self.runTest(1, 3, False)
		self.runTest(1, 4, False)
		self.runTest(1, 5, False)
		self.runTest(2, 3, True)
		self.runTest(2, 4, False)
		self.runTest(2, 5, False)
		self.runTest(3, 4, False)
		self.runTest(3, 5, False)
		self.runTest(4, 5, True)

	def test_Quick3(self):
		self._graphs = loadgraphs('data\colorref_smallexample_2_49.grl')
		self.runTest(0, 1, True)

	def test_Quick4(self):
		self._graphs = loadgraphs('data\colorref_largeexample_6_960.grl')
		self.runTest(0, 1, False)
		self.runTest(0, 2, False)
		self.runTest(0, 3, False)
		self.runTest(0, 4, True)
		self.runTest(0, 5, False)
		self.runTest(1, 2, False)
		self.runTest(1, 3, True)
		self.runTest(1, 4, False)
		self.runTest(1, 5, False)
		self.runTest(2, 3, False)
		self.runTest(2, 4, False)
		self.runTest(2, 5, True)
		self.runTest(3, 4, False)
		self.runTest(3, 5, False)
		self.runTest(4, 5, False)

	def runTest(self, index1 : int, index2 : int, expectedResult : bool):
		g1 = self._graphs[0][index1].clone()
		g2 = self._graphs[0][index2].clone()
		result, graphcolors = self._checker.isIsomorphic(g1,g2)
		print(index1, index2, result)
		#self.assertEqual(expectedResult, result)
