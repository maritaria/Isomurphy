import copy
import unittest
from graph.graphIO import loadgraphs, writeDOT
from isomorphism.ColorRefinementChecker import ColorRefinementChecker
from isomorphism.IndividualizationRefinementChecker import IndividualizationRefinementChecker
from isomorphism.FastPartitionRefinement import FastPartitionRefinementChecker


class IsomorphTest(unittest.TestCase):

	def setUp(self):
		self._checker = IndividualizationRefinementChecker()
		self._checker._checker = ColorRefinementChecker()

	def test_gi_01(self):
		self._graphs = loadgraphs('data\\basicgi2.grl')
		self.runTest(0, 1)
	def test_gi_02(self):
		self._graphs = loadgraphs('data\\basicgi2.grl')
		self.runTest(0, 2)
	def test_gi_03(self):
		self._graphs = loadgraphs('data\\basicgi2.grl')
		self.runTest(0, 3)
	def test_gi_12(self):
		self._graphs = loadgraphs('data\\basicgi2.grl')
		self.runTest(1, 2)
	def test_gi_13(self):
		self._graphs = loadgraphs('data\\basicgi2.grl')
		self.runTest(1, 3)
	def test_gi_23(self):
		self._graphs = loadgraphs('data\\basicgi2.grl')
		self.runTest(2, 3)

	def runTest(self, index1 : int, index2 : int):
		g1 = (self._graphs[0][index1])
		g2 = (self._graphs[0][index2])
		result = self._checker.isIsomorphic(copy.deepcopy(g1), copy.deepcopy(g2))
		print(result)
		writeDOT(g1, "data\\basicgi2_%s.dot"%(index1))
		#self.assertEqual(expectedResult, result)
