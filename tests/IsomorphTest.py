import unittest
from graph.graphIO import loadgraphs, writeDOT
from isomorphism.ColorRefinementChecker import ColorRefinementChecker
from isomorphism.IndividualizationRefinementChecker import IndividualizationRefinementChecker


class IsomorphTest(unittest.TestCase):

	def setUp(self):
		self._checker = IndividualizationRefinementChecker()

	def test_quick1_01(self):
		self._graphs = loadgraphs('data\colorref_smallexample_4_7.grl')
		self.runTest(0, 1, False)
	def test_quick1_02(self):
		self._graphs = loadgraphs('data\colorref_smallexample_4_7.grl')
		self.runTest(0, 2, True)
	def test_quick1_03(self):
		self._graphs = loadgraphs('data\colorref_smallexample_4_7.grl')
		self.runTest(0, 3, False)
	def test_quick1_12(self):
		self._graphs = loadgraphs('data\colorref_smallexample_4_7.grl')
		self.runTest(1, 2, False)
	def test_quick1_13(self):
		self._graphs = loadgraphs('data\colorref_smallexample_4_7.grl')
		self.runTest(1, 3, True)
	def test_quick1_23(self):
		self._graphs = loadgraphs('data\colorref_smallexample_4_7.grl')
		self.runTest(2, 3, False)

	def test_quick2_01(self):
		self._graphs = loadgraphs('data\colorref_smallexample_4_16.grl')
		self.runTest(0, 1, True)
	def test_quick2_02(self):
		self._graphs = loadgraphs('data\colorref_smallexample_4_16.grl')
		self.runTest(0, 2, False)
	def test_quick2_03(self):
		self._graphs = loadgraphs('data\colorref_smallexample_4_16.grl')
		self.runTest(0, 3, False)
	def test_quick2_12(self):
		self._graphs = loadgraphs('data\colorref_smallexample_4_16.grl')
		self.runTest(1, 2, False)
	def test_quick2_13(self):
		self._graphs = loadgraphs('data\colorref_smallexample_4_16.grl')
		self.runTest(1, 3, False)
	def test_quick2_23(self):
		self._graphs = loadgraphs('data\colorref_smallexample_4_16.grl')
		self.runTest(2, 3, True)

	def test_quick3_01(self):
		self._graphs = loadgraphs('data\colorref_smallexample_6_15.grl')
		self.runTest(0, 1, True)
	def test_quick3_02(self):
		self._graphs = loadgraphs('data\colorref_smallexample_6_15.grl')
		self.runTest(0, 2, False)
	def test_quick3_03(self):
		self._graphs = loadgraphs('data\colorref_smallexample_6_15.grl')
		self.runTest(0, 3, False)
	def test_quick3_04(self):
		self._graphs = loadgraphs('data\colorref_smallexample_6_15.grl')
		self.runTest(0, 4, False)
	def test_quick3_05(self):
		self._graphs = loadgraphs('data\colorref_smallexample_6_15.grl')
		self.runTest(0, 5, False)
	def test_quick3_12(self):
		self._graphs = loadgraphs('data\colorref_smallexample_6_15.grl')
		self.runTest(1, 2, False)
	def test_quick3_13(self):
		self._graphs = loadgraphs('data\colorref_smallexample_6_15.grl')
		self.runTest(1, 3, False)
	def test_quick3_14(self):
		self._graphs = loadgraphs('data\colorref_smallexample_6_15.grl')
		self.runTest(1, 4, False)
	def test_quick3_15(self):
		self._graphs = loadgraphs('data\colorref_smallexample_6_15.grl')
		self.runTest(1, 5, False)
	def test_quick3_23(self):
		self._graphs = loadgraphs('data\colorref_smallexample_6_15.grl')
		self.runTest(2, 3, True)
	def test_quick3_24(self):
		self._graphs = loadgraphs('data\colorref_smallexample_6_15.grl')
		self.runTest(2, 4, False)
	def test_quick3_25(self):
		self._graphs = loadgraphs('data\colorref_smallexample_6_15.grl')
		self.runTest(2, 5, False)
	def test_quick3_34(self):
		self._graphs = loadgraphs('data\colorref_smallexample_6_15.grl')
		self.runTest(3, 4, False)
	def test_quick3_35(self):
		self._graphs = loadgraphs('data\colorref_smallexample_6_15.grl')
		self.runTest(3, 5, False)
	def test_quick3_45(self):
		self._graphs = loadgraphs('data\colorref_smallexample_6_15.grl')
		self.runTest(4, 5, True)

	def test_quick4(self):
		self._graphs = loadgraphs('data\colorref_smallexample_2_49.grl')
		self.runTest(0, 1, True)

	"""
	def test_large1_01(self):
		self._graphs = loadgraphs('data\colorref_largeexample_6_960.grl')
		self.runTest(0, 1, False)
	def test_large1_02(self):
		self._graphs = loadgraphs('data\colorref_largeexample_6_960.grl')
		self.runTest(0, 2, False)
	def test_large1_03(self):
		self._graphs = loadgraphs('data\colorref_largeexample_6_960.grl')
		self.runTest(0, 3, False)
	def test_large1_04(self):
		self._graphs = loadgraphs('data\colorref_largeexample_6_960.grl')
		self.runTest(0, 4, True)
	def test_large1_05(self):
		self._graphs = loadgraphs('data\colorref_largeexample_6_960.grl')
		self.runTest(0, 5, False)
	def test_large1_12(self):
		self._graphs = loadgraphs('data\colorref_largeexample_6_960.grl')
		self.runTest(1, 2, False)
	def test_large1_13(self):
		self._graphs = loadgraphs('data\colorref_largeexample_6_960.grl')
		self.runTest(1, 3, True)
	def test_large1_14(self):
		self._graphs = loadgraphs('data\colorref_largeexample_6_960.grl')
		self.runTest(1, 4, False)
	def test_large1_15(self):
		self._graphs = loadgraphs('data\colorref_largeexample_6_960.grl')
		self.runTest(1, 5, False)
	def test_large1_23(self):
		self._graphs = loadgraphs('data\colorref_largeexample_6_960.grl')
		self.runTest(2, 3, False)
	def test_large1_24(self):
		self._graphs = loadgraphs('data\colorref_largeexample_6_960.grl')
		self.runTest(2, 4, False)
	def test_large1_25(self):
		self._graphs = loadgraphs('data\colorref_largeexample_6_960.grl')
		self.runTest(2, 5, True)
	def test_large1_34(self):
		self._graphs = loadgraphs('data\colorref_largeexample_6_960.grl')
		self.runTest(3, 4, False)
	def test_large1_35(self):
		self._graphs = loadgraphs('data\colorref_largeexample_6_960.grl')
		self.runTest(3, 5, False)
	def test_large1_45(self):
		self._graphs = loadgraphs('data\colorref_largeexample_6_960.grl')
		self.runTest(4, 5, False)
	"""
	def runTest(self, index1 : int, index2 : int, expectedResult : bool):
		g1 = self._graphs[0][index1].clone()
		g2 = self._graphs[0][index2].clone()
		result = self._checker.isIsomorphic(g1, g2)
		self.assertEqual(expectedResult, result)
