import copy
import unittest
from graph.graphIO import loadgraphs, writeDOT
from isomorphism.ColorRefinementChecker import ColorRefinementChecker
from isomorphism.IndividualizationRefinementChecker import IndividualizationRefinementChecker


class IsomorphTest(unittest.TestCase):

	def setUp(self):
		self._checker = IndividualizationRefinementChecker()

	def test_bigtrees1_01(self):
		self._graphs = loadgraphs("data\\bigtrees1.grl")
		self.runTest(0, 1, False)
	def test_bigtrees1_02(self):
		self._graphs = loadgraphs("data\\bigtrees1.grl")
		self.runTest(0, 2, True)
	def test_bigtrees1_03(self):
		self._graphs = loadgraphs("data\\bigtrees1.grl")
		self.runTest(0, 3, False)
	def test_bigtrees1_12(self):
		self._graphs = loadgraphs("data\\bigtrees1.grl")
		self.runTest(1, 2, False)
	def test_bigtrees1_13(self):
		self._graphs = loadgraphs("data\\bigtrees1.grl")
		self.runTest(1, 3, True)
	def test_bigtrees1_23(self):
		self._graphs = loadgraphs("data\\bigtrees1.grl")
		self.runTest(2, 3, False)

	def runTest(self, index1 : int, index2 : int, expectedResult : bool):
		g1 = (self._graphs[0][index1])
		g2 = (self._graphs[0][index2])
		result = self._checker.isIsomorphic(g1, g2)
		self.assertEqual(expectedResult, result)
