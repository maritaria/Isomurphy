import copy
import unittest
from graph.graphIO import loadgraphs, writeDOT
from isomorphism.ColorRefinementChecker import ColorRefinementChecker
from isomorphism.IndividualizationRefinementChecker import IndividualizationRefinementChecker


class IsomorphTest(unittest.TestCase):

	def setUp(self):
		self._checker = IndividualizationRefinementChecker()

	def test_huge1_01(self):
		self._graphs = loadgraphs('data\colorref_largeexample_4_1026.grl')
		self.runTest(0, 1)
	def test_huge1_02(self):
		self._graphs = loadgraphs('data\colorref_largeexample_4_1026.grl')
		self.runTest(0, 2)
	def test_huge1_03(self):
		self._graphs = loadgraphs('data\colorref_largeexample_4_1026.grl')
		self.runTest(0, 3)
	def test_huge1_12(self):
		self._graphs = loadgraphs('data\colorref_largeexample_4_1026.grl')
		self.runTest(1, 2)
	def test_huge1_13(self):
		self._graphs = loadgraphs('data\colorref_largeexample_4_1026.grl')
		self.runTest(1, 3)
	def test_huge1_23(self):
		self._graphs = loadgraphs('data\colorref_largeexample_4_1026.grl')
		self.runTest(2, 3)

	def runTest(self, index1 : int, index2 : int):
		g1 = (self._graphs[0][index1])
		g2 = (self._graphs[0][index2])
		result = self._checker.isIsomorphic(g1, g2)
		#self.assertEqual(expectedResult, result)
