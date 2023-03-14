import sys
import ctypes


class SpatialQuaternion(ctypes.Structure):
	_fields_ = [
		("_x", ctypes.c_double),
		("_y", ctypes.c_double),
		("_z", ctypes.c_double),
		("_w", ctypes.c_double),
	]

	def __init__(self):
		self.x = 0
		self.y = 0
		self.z = 0
		self.w = 0

	def fromPython(self):
		self._x = self.x
		self._y = self.y
		self._z = self.z
		self._w = self.w
		return self

	def toPython(self):
		if self._x == None:
			self.x = None
		else:
			self.x = self._x
		if self._y == None:
			self.y = None
		else:
			self.y = self._y
		if self._z == None:
			self.z = None
		else:
			self.z = self._z
		if self._w == None:
			self.w = None
		else:
			self.w = self._w
		return self

	def __str__(self):
		return ("[SpatialQuaternion] ("
			"x: " + str(self.x) + ", "
			"y: " + str(self.y) + ", "
			"z: " + str(self.z) + ", "
			"w: " + str(self.w) + 
			")")
