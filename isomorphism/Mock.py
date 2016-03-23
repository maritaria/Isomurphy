from utils.lists import *

class ColorClass:
	def __init__(self, g1, g2, color):
		self._G1 = g1
		self._G2 = g2
		self._V1 = []
		self._V2 = []
		self._color = color

	def V1(self):
		return self._V1

	def V2(self):
		return self._V2

	def count(self):
		return len(self._V1)

	def addVerts(self, vs1, vs2):
		if len(vs1) != len(vs2):
			raise InvalidSplitException()
		for v in vs1:
			self.addV1(v)

		for v in vs2:
			self.addV2(v)

	def addV1(self, v):
		if (hasattr(v, "colorClass")):
			v.colorClass.V1().remove(v)
		self.V1().append(v)
		v.colorClass = self
		v.colornum = self._color

	def addV2(self, v):
		if (hasattr(v, "colorClass")):
			v.colorClass.V2().remove(v)
		self.V2().append(v)
		v.colorClass = self
		v.colornum = self._color

	def __str__(self):
		return str(self._color)
	def __repr__(self):
		return str(self)


class InvalidSplitException(Exception):
	pass


class Partitioner:
	def __init__(self, g1, g2):
		self._G1 = g1
		self._G2 = g2
		self._colors = {}
		self._topColor = 0
		self._directed = self._G1._directed

	def partition(self):
		self.prepare()
		# steps
		try:
			while self._queue:
				self.step()
		except InvalidSplitException:
			return False
		return True

	def step(self):
		colorClass = self._queue.pop(0)
		self.split(colorClass)

	def prepare(self):
		# setup
		self._queue = []
		self._colors = {}
		self._topColor = 0
		for v in self._G1.V():
			color = -1
			if hasattr(v, 'colornum'):
				color = v.colornum
			else:
				color = v.deg()
			self.getColorClass(color).addV1(v)
		for v in self._G2.V():
			color = -1
			if hasattr(v, 'colornum'):
				color = v.colornum
			else:
				color = v.deg()
			self.getColorClass(color).addV2(v)
		#Put all classes on the queue, except the largest one
		self._queue = list(self._colors.values())
		#TODO: Verify integrity of all colorClasses

	def split(self, colorClass):
		for otherClass in list(self._colors.values()):
			if otherClass is not colorClass:
				self.splitClass(colorClass, otherClass)

	def splitClass(self, colorClass, otherClass):
		if colorClass.count() * otherClass.count() == 0:
			return

		newClasses = []
		#Calculate degrees between verts and the colorClass
		degrees1 = {}
		for v in otherClass.V1():
			degree = self.getDegreeWithClass1(v, colorClass)
			degrees1[degree] = degrees1.get(degree, [])
			degrees1[degree].append(v)

		degrees2 = {}
		for v in otherClass.V2():
			degree = self.getDegreeWithClass2(v, colorClass)
			degrees2[degree] = degrees2.get(degree, [])
			degrees2[degree].append(v)
		# TODO: degrees1 en degrees2 should be bijections
		#Split otherClass based on degree with colorClass
		if (len(degrees1) == 1):
			return
		for d in degrees1:
			verts1 = degrees1[d]
			if not d in degrees2.keys():
				raise InvalidSplitException()
			verts2 = degrees2[d]

			newClass = self.getNextColorClass()
			newClass.addVerts(verts1, verts2)
			newClasses.append(newClass)

		#Add all classes except the largest one to the queue
		largest = newClasses[0]
		for colorClass in newClasses:
			if colorClass is not largest:
				if colorClass.count() > largest.count():
					self._queue.append(largest)
					largest = colorClass
				else:
					self._queue.append(colorClass)
		if otherClass in self._queue:
			self._queue.remove(otherClass)

	def getDegreeWithClass1(self, v, colorClass) -> int:
		return len(filter(lambda edge: edge.head() in colorClass.V1() or (not self._directed and edge.tail() in colorClass.V1()), v.inclist()))

	def getDegreeWithClass2(self, v, colorClass) -> int:
		return len(filter(lambda edge: edge.head() in colorClass.V2() or (not self._directed and edge.tail() in colorClass.V2()), v.inclist()))

	def getNextColorClass(self):
		self._topColor += 1
		colorClass = ColorClass(self._G1, self._G2, self._topColor)
		self._colors[self._topColor] = colorClass
		return colorClass

	def getColorClass(self, color):
		colorClass = self._colors.get(color)
		if colorClass == None:
			colorClass = ColorClass(self._G1, self._G2, color)
			self._colors[color] = colorClass
		self._topColor = max(self._topColor, color)
		return colorClass

	#####################################SIM CODE

	def getColors(self, g ) -> dict:
		result = {}
		for v in g.V():
			if hasattr(v, "colornum"):
				result[v] = v.colornum
			else:
				result[v] = -1
		return result