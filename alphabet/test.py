import copy
import unittest

from graph.graphIO import loadgraphs, writeDOT
from isomorphism.ColorRefinementChecker import ColorRefinementChecker
from isomorphism.IndividualizationRefinementChecker import IndividualizationRefinementChecker


class SomeTest(unittest.TestCase):

	def setUp(self):
		self._checker = IndividualizationRefinementChecker()
		self._alphabet_jan = loadgraphs("alphabet_jan.grl")
		self._alphabet_tygo = loadgraphs("alphabet_tygo.grl")
		self._alphabet_pixel = loadgraphs("alphabet_pixel.grl")
		
	def test_jan(self):
		print("jan:")
		self.alpha_self(self._alphabet_jan)
	def test_pixel(self):
		print("pixel:")
		self.alpha_self(self._alphabet_pixel)
	def test_tygo(self):
		print("tygo:")
		self.alpha_self(self._alphabet_tygo)

	def test_jan_pixel_vs(self):
		print("jan vs pixel:")
		self.alpha_versus(self._alphabet_jan, self._alphabet_pixel)
	def test_jan_tygo_vs(self):
		print("jan vs tygo:")
		self.alpha_versus(self._alphabet_jan, self._alphabet_tygo)
	def test_pixel_tygo_vs(self):
		print("pixel vs tygo:")
		self.alpha_versus(self._alphabet_pixel, self._alphabet_tygo)

	def test_jan_pixel_all(self):
		print("jan and pixel:")
		self.alpha_all(self._alphabet_jan, self._alphabet_pixel)
	def test_jan_tygo_all(self):
		print("#jan and *tygo:")
		self.alpha_all(self._alphabet_jan, self._alphabet_tygo)
	def test_pixel_tygo_all(self):
		print("pixel and tygo:")
		self.alpha_all(self._alphabet_pixel, self._alphabet_tygo)

	def alpha_self(self, alpha : list):
		isos = []
		queue = list(range(0, 26))
		while(len(queue) > 0):
			index = queue.pop(0)
			localiso = []
			localiso.append(chr(index + 97))
			for i in range(index+1, 26):

				g1 = copy.deepcopy(alpha[0][index])
				g2 = copy.deepcopy(alpha[0][i])
				if self._checker.isIsomorphic(g1, g2):
					if i in queue:
						queue.remove(i)
					localiso.append(chr(i + 97))
			isos.append(localiso)
		print(isos)

	def alpha_versus(self, alpha1 : list, alpha2 : list):
		isos = []
		for i in range(0, 26):
			jan = copy.deepcopy(alpha1[0][i])
			tygo = copy.deepcopy(alpha2[0][i])
			iso = self._checker.isIsomorphic(jan, tygo)
			if iso:
				isos.append(chr(i + 97))
		print(isos)

	def alpha_all(self, alpha1 : list, alpha2 : list):
		alpha1 = copy.deepcopy(alpha1)
		alpha2 = copy.deepcopy(alpha2)
		for i in range(0, 26):
			alpha1[0][i]._label = "#%s" % chr(97 + i)
			alpha2[0][i]._label = "*%s" % chr(97 + i)
		mountain = list(alpha1[0]) + list(alpha2[0])
		isos = []
		while(len(mountain) > 0):
			g1 = mountain.pop(0)
			localiso = []
			localiso.append(g1._label)
			for g2 in mountain[:]:
				if self._checker.isIsomorphic(g1, g2):
					mountain.remove(g2)
					localiso.append(g2._label)
			isos.append(localiso)
		print(isos)