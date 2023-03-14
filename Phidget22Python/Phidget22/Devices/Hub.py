import sys
import ctypes
from Phidget22.PhidgetSupport import PhidgetSupport
from Phidget22.Async import *
from Phidget22.HubPortMode import HubPortMode
from Phidget22.PhidgetException import PhidgetException

from Phidget22.Phidget import Phidget

class Hub(Phidget):

	def __init__(self):
		Phidget.__init__(self)
		self.handle = ctypes.c_void_p()

		__func = PhidgetSupport.getDll().PhidgetHub_create
		__func.restype = ctypes.c_int32
		res = __func(ctypes.byref(self.handle))

		if res > 0:
			raise PhidgetException(res)

	def __del__(self):
		Phidget.__del__(self)

	def getPortMaxSpeed(self, port):
		_port = ctypes.c_int(port)
		_state = ctypes.c_uint32()

		__func = PhidgetSupport.getDll().PhidgetHub_getPortMaxSpeed
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _port, ctypes.byref(_state))

		if result > 0:
			raise PhidgetException(result)

		return _state.value

	def getPortMode(self, port):
		_port = ctypes.c_int(port)
		_mode = ctypes.c_int()

		__func = PhidgetSupport.getDll().PhidgetHub_getPortMode
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _port, ctypes.byref(_mode))

		if result > 0:
			raise PhidgetException(result)

		return _mode.value

	def setPortMode(self, port, mode):
		_port = ctypes.c_int(port)
		_mode = ctypes.c_int(mode)

		__func = PhidgetSupport.getDll().PhidgetHub_setPortMode
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _port, _mode)

		if result > 0:
			raise PhidgetException(result)


	def getPortPower(self, port):
		_port = ctypes.c_int(port)
		_state = ctypes.c_int()

		__func = PhidgetSupport.getDll().PhidgetHub_getPortPower
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _port, ctypes.byref(_state))

		if result > 0:
			raise PhidgetException(result)

		return bool(_state.value)

	def setPortPower(self, port, state):
		_port = ctypes.c_int(port)
		_state = ctypes.c_int(state)

		__func = PhidgetSupport.getDll().PhidgetHub_setPortPower
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _port, _state)

		if result > 0:
			raise PhidgetException(result)


	def getPortSupportsSetSpeed(self, port):
		_port = ctypes.c_int(port)
		_state = ctypes.c_int()

		__func = PhidgetSupport.getDll().PhidgetHub_getPortSupportsSetSpeed
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _port, ctypes.byref(_state))

		if result > 0:
			raise PhidgetException(result)

		return bool(_state.value)
