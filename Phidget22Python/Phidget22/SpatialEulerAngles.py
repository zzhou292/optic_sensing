import sys
import ctypes


class SpatialEulerAngles(ctypes.Structure):
	_fields_ = [
		("_pitch", ctypes.c_double),
		("_roll", ctypes.c_double),
		("_heading", ctypes.c_double),
	]

	def __init__(self):
		self.pitch = 0
		self.roll = 0
		self.heading = 0

	def fromPython(self):
		self._pitch = self.pitch
		self._roll = self.roll
		self._heading = self.heading
		return self

	def toPython(self):
		if self._pitch == None:
			self.pitch = None
		else:
			self.pitch = self._pitch
		if self._roll == None:
			self.roll = None
		else:
			self.roll = self._roll
		if self._heading == None:
			self.heading = None
		else:
			self.heading = self._heading
		return self

	def __str__(self):
		return ("[SpatialEulerAngles] ("
			"pitch: " + str(self.pitch) + ", "
			"roll: " + str(self.roll) + ", "
			"heading: " + str(self.heading) + 
			")")
