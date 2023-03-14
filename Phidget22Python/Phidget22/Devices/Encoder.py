import sys
import ctypes
from Phidget22.PhidgetSupport import PhidgetSupport
from Phidget22.Async import *
from Phidget22.EncoderIOMode import EncoderIOMode
from Phidget22.PhidgetException import PhidgetException

from Phidget22.Phidget import Phidget

class Encoder(Phidget):

	def __init__(self):
		Phidget.__init__(self)
		self.handle = ctypes.c_void_p()

		if sys.platform == 'win32':
			self._PositionChangeFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_double, ctypes.c_int)
		else:
			self._PositionChangeFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_double, ctypes.c_int)
		self._PositionChange = None
		self._onPositionChange = None

		__func = PhidgetSupport.getDll().PhidgetEncoder_create
		__func.restype = ctypes.c_int32
		res = __func(ctypes.byref(self.handle))

		if res > 0:
			raise PhidgetException(res)

	def __del__(self):
		Phidget.__del__(self)

	def _localPositionChangeEvent(self, handle, userPtr, positionChange, timeChange, indexTriggered):
		if self._PositionChange == None:
			return
		self._PositionChange(self, positionChange, timeChange, indexTriggered)

	def setOnPositionChangeHandler(self, handler):
		if handler == None:
			self._PositionChange = None
			self._onPositionChange = None
		else:
			self._PositionChange = handler
			self._onPositionChange = self._PositionChangeFactory(self._localPositionChangeEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetEncoder_setOnPositionChangeHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onPositionChange, None)
		except RuntimeError:
			self._PositionChange = None
			self._onPositionChange = None

	def setEnabled(self, Enabled):
		_Enabled = ctypes.c_int(Enabled)

		__func = PhidgetSupport.getDll().PhidgetEncoder_setEnabled
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _Enabled)

		if result > 0:
			raise PhidgetException(result)


	def getEnabled(self):
		_Enabled = ctypes.c_int()

		__func = PhidgetSupport.getDll().PhidgetEncoder_getEnabled
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_Enabled))

		if result > 0:
			raise PhidgetException(result)

		return bool(_Enabled.value)

	def getDataInterval(self):
		_DataInterval = ctypes.c_uint32()

		__func = PhidgetSupport.getDll().PhidgetEncoder_getDataInterval
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_DataInterval))

		if result > 0:
			raise PhidgetException(result)

		return _DataInterval.value

	def setDataInterval(self, DataInterval):
		_DataInterval = ctypes.c_uint32(DataInterval)

		__func = PhidgetSupport.getDll().PhidgetEncoder_setDataInterval
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _DataInterval)

		if result > 0:
			raise PhidgetException(result)


	def getMinDataInterval(self):
		_MinDataInterval = ctypes.c_uint32()

		__func = PhidgetSupport.getDll().PhidgetEncoder_getMinDataInterval
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MinDataInterval))

		if result > 0:
			raise PhidgetException(result)

		return _MinDataInterval.value

	def getMaxDataInterval(self):
		_MaxDataInterval = ctypes.c_uint32()

		__func = PhidgetSupport.getDll().PhidgetEncoder_getMaxDataInterval
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MaxDataInterval))

		if result > 0:
			raise PhidgetException(result)

		return _MaxDataInterval.value

	def getDataRate(self):
		_DataRate = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetEncoder_getDataRate
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_DataRate))

		if result > 0:
			raise PhidgetException(result)

		return _DataRate.value

	def setDataRate(self, DataRate):
		_DataRate = ctypes.c_double(DataRate)

		__func = PhidgetSupport.getDll().PhidgetEncoder_setDataRate
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _DataRate)

		if result > 0:
			raise PhidgetException(result)


	def getMinDataRate(self):
		_MinDataRate = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetEncoder_getMinDataRate
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MinDataRate))

		if result > 0:
			raise PhidgetException(result)

		return _MinDataRate.value

	def getMaxDataRate(self):
		_MaxDataRate = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetEncoder_getMaxDataRate
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MaxDataRate))

		if result > 0:
			raise PhidgetException(result)

		return _MaxDataRate.value

	def getIndexPosition(self):
		_IndexPosition = ctypes.c_int64()

		__func = PhidgetSupport.getDll().PhidgetEncoder_getIndexPosition
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_IndexPosition))

		if result > 0:
			raise PhidgetException(result)

		return _IndexPosition.value

	def getIOMode(self):
		_IOMode = ctypes.c_int()

		__func = PhidgetSupport.getDll().PhidgetEncoder_getIOMode
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_IOMode))

		if result > 0:
			raise PhidgetException(result)

		return _IOMode.value

	def setIOMode(self, IOMode):
		_IOMode = ctypes.c_int(IOMode)

		__func = PhidgetSupport.getDll().PhidgetEncoder_setIOMode
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _IOMode)

		if result > 0:
			raise PhidgetException(result)


	def getPosition(self):
		_Position = ctypes.c_int64()

		__func = PhidgetSupport.getDll().PhidgetEncoder_getPosition
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_Position))

		if result > 0:
			raise PhidgetException(result)

		return _Position.value

	def setPosition(self, Position):
		_Position = ctypes.c_int64(Position)

		__func = PhidgetSupport.getDll().PhidgetEncoder_setPosition
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _Position)

		if result > 0:
			raise PhidgetException(result)


	def getPositionChangeTrigger(self):
		_PositionChangeTrigger = ctypes.c_uint32()

		__func = PhidgetSupport.getDll().PhidgetEncoder_getPositionChangeTrigger
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_PositionChangeTrigger))

		if result > 0:
			raise PhidgetException(result)

		return _PositionChangeTrigger.value

	def setPositionChangeTrigger(self, PositionChangeTrigger):
		_PositionChangeTrigger = ctypes.c_uint32(PositionChangeTrigger)

		__func = PhidgetSupport.getDll().PhidgetEncoder_setPositionChangeTrigger
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _PositionChangeTrigger)

		if result > 0:
			raise PhidgetException(result)


	def getMinPositionChangeTrigger(self):
		_MinPositionChangeTrigger = ctypes.c_uint32()

		__func = PhidgetSupport.getDll().PhidgetEncoder_getMinPositionChangeTrigger
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MinPositionChangeTrigger))

		if result > 0:
			raise PhidgetException(result)

		return _MinPositionChangeTrigger.value

	def getMaxPositionChangeTrigger(self):
		_MaxPositionChangeTrigger = ctypes.c_uint32()

		__func = PhidgetSupport.getDll().PhidgetEncoder_getMaxPositionChangeTrigger
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MaxPositionChangeTrigger))

		if result > 0:
			raise PhidgetException(result)

		return _MaxPositionChangeTrigger.value
