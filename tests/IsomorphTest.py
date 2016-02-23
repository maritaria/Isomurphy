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
		writeDOT(self._graphs[0][0], 'colorful.dot')
		writeDOT(self._graphs[0][1], 'colorful1.dot')
		writeDOT(self._graphs[0][2], 'colorful2.dot')
		writeDOT(self._graphs[0][3], 'colorful3.dot')

	def test_Quick1(self):
		self._graphs = loadgraphs('data\colorref_smallexample_4_16.grl')
		self.runTest(0, 1, True)
		self.runTest(0, 2, False)
		self.runTest(0, 3, False)
		self.runTest(1, 2, False)
		self.runTest(1, 3, False)
		self.runTest(2, 3, True)
		writeDOT(self._graphs[0][0], 'colorfuls.dot')
		writeDOT(self._graphs[0][1], 'colorfuls1.dot')
		writeDOT(self._graphs[0][2], 'colorfuls2.dot')
		writeDOT(self._graphs[0][3], 'colorfuls3.dot')

	def test_Quick3(self):
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
		writeDOT(self._graphs[0][0], 'colorfulss.dot')
		writeDOT(self._graphs[0][1], 'colorfulss1.dot')
		writeDOT(self._graphs[0][2], 'colorfulss2.dot')
		writeDOT(self._graphs[0][3], 'colorfulss3.dot')
		writeDOT(self._graphs[0][4], 'colorfulss4.dot')
		writeDOT(self._graphs[0][5], 'colorfulss5.dot')

	def runTest(self, index1 : int, index2 : int, expectedResult : bool):
		g1 = self._graphs[0][index1]
		g2 = self._graphs[0][index2]
		result = self._checker.isIsomorphic(g1,g2)
		#print(index1, index2, result)
		self.assertEqual(expectedResult, result)
