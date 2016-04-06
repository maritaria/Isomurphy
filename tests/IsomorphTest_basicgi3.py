import copy
import unittest
from graph.graphIO import loadgraphs, writeDOT
from isomorphism.ColorRefinementChecker import ColorRefinementChecker
from isomorphism.IndividualizationRefinementChecker import IndividualizationRefinementChecker
from isomorphism.FastPartitionRefinement import FastPartitionRefinementChecker


class IsomorphTest(unittest.TestCase):

	def setUp(self):
		self._checker = IndividualizationRefinementChecker()
		self._checker._checker = FastPartitionRefinementChecker()

	def test_gi_01(self):
		self._graphs = loadgraphs('data\\modulesc.grl')
		self.runTest(0, 1)
	def test_gi_02(self):
		self._graphs = loadgraphs('data\\modulesc.grl')
		self.runTest(0, 2)
	def test_gi_03(self):
		self._graphs = loadgraphs('data\\modulesc.grl')
		self.runTest(0, 3)
	def test_gi_04(self):
		self._graphs = loadgraphs('data\\modulesc.grl')
		self.runTest(0, 4)
	def test_gi_05(self):
		self._graphs = loadgraphs('data\\modulesc.grl')
		self.runTest(0, 5)
	def test_gi_06(self):
		self._graphs = loadgraphs('data\\modulesc.grl')
		self.runTest(0, 6)
	def test_gi_12(self):
		self._graphs = loadgraphs('data\\modulesc.grl')
		self.runTest(1, 2)
	def test_gi_13(self):
		self._graphs = loadgraphs('data\\modulesc.grl')
		self.runTest(1, 3)
	def test_gi_14(self):
		self._graphs = loadgraphs('data\\modulesc.grl')
		self.runTest(1, 4)
	def test_gi_15(self):
		self._graphs = loadgraphs('data\\modulesc.grl')
		self.runTest(1, 5)
	def test_gi_16(self):
		self._graphs = loadgraphs('data\\modulesc.grl')
		self.runTest(1, 6)
	def test_gi_23(self):
		self._graphs = loadgraphs('data\\modulesc.grl')
		self.runTest(2, 3)
	def test_gi_24(self):
		self._graphs = loadgraphs('data\\modulesc.grl')
		self.runTest(2, 4)
	def test_gi_25(self):
		self._graphs = loadgraphs('data\\modulesc.grl')
		self.runTest(2, 5)
	def test_gi_26(self):
		self._graphs = loadgraphs('data\\modulesc.grl')
		self.runTest(2, 6)
	def test_gi_34(self):
		self._graphs = loadgraphs('data\\modulesc.grl')
		self.runTest(3, 4)
	def test_gi_35(self):
		self._graphs = loadgraphs('data\\modulesc.grl')
		self.runTest(3, 5)
	def test_gi_36(self):
		self._graphs = loadgraphs('data\\modulesc.grl')
		self.runTest(3, 6)
	def test_gi_45(self):
		self._graphs = loadgraphs('data\\modulesc.grl')
		self.runTest(4, 5)
	def test_gi_46(self):
		self._graphs = loadgraphs('data\\modulesc.grl')
		self.runTest(4, 6)
	def test_gi_56(self):
		self._graphs = loadgraphs('data\\modulesc.grl')
		self.runTest(5, 6)

	def runTest(self, index1 : int, index2 : int):
		g1 = (self._graphs[0][index1])
		g2 = (self._graphs[0][index2])
		result = self._checker.isIsomorphic(copy.deepcopy(g1), copy.deepcopy(g2))
		print(index1, index2, result)
		writeDOT(g1, "data\\basicgi2_%s.dot"%(index1))
		#self.assertEqual(expectedResult, result)
