import sys
import ctypes
from Phidget22.PhidgetSupport import PhidgetSupport
from Phidget22.Async import *
from Phidget22.PhidgetException import PhidgetException

from Phidget22.Phidget import Phidget

class PressureSensor(Phidget):

	def __init__(self):
		Phidget.__init__(self)
		self.handle = ctypes.c_void_p()

		if sys.platform == 'win32':
			self._PressureChangeFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double)
		else:
			self._PressureChangeFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double)
		self._PressureChange = None
		self._onPressureChange = None

		__func = PhidgetSupport.getDll().PhidgetPressureSensor_create
		__func.restype = ctypes.c_int32
		res = __func(ctypes.byref(self.handle))

		if res > 0:
			raise PhidgetException(res)

	def __del__(self):
		Phidget.__del__(self)

	def _localPressureChangeEvent(self, handle, userPtr, pressure):
		if self._PressureChange == None:
			return
		self._PressureChange(self, pressure)

	def setOnPressureChangeHandler(self, handler):
		if handler == None:
			self._PressureChange = None
			self._onPressureChange = None
		else:
			self._PressureChange = handler
			self._onPressureChange = self._PressureChangeFactory(self._localPressureChangeEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetPressureSensor_setOnPressureChangeHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onPressureChange, None)
		except RuntimeError:
			self._PressureChange = None
			self._onPressureChange = None

	def getDataInterval(self):
		_DataInterval = ctypes.c_uint32()

		__func = PhidgetSupport.getDll().PhidgetPressureSensor_getDataInterval
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_DataInterval))

		if result > 0:
			raise PhidgetException(result)

		return _DataInterval.value

	def setDataInterval(self, DataInterval):
		_DataInterval = ctypes.c_uint32(DataInterval)

		__func = PhidgetSupport.getDll().PhidgetPressureSensor_setDataInterval
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _DataInterval)

		if result > 0:
			raise PhidgetException(result)


	def getMinDataInterval(self):
		_MinDataInterval = ctypes.c_uint32()

		__func = PhidgetSupport.getDll().PhidgetPressureSensor_getMinDataInterval
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MinDataInterval))

		if result > 0:
			raise PhidgetException(result)

		return _MinDataInterval.value

	def getMaxDataInterval(self):
		_MaxDataInterval = ctypes.c_uint32()

		__func = PhidgetSupport.getDll().PhidgetPressureSensor_getMaxDataInterval
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MaxDataInterval))

		if result > 0:
			raise PhidgetException(result)

		return _MaxDataInterval.value

	def getDataRate(self):
		_DataRate = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetPressureSensor_getDataRate
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_DataRate))

		if result > 0:
			raise PhidgetException(result)

		return _DataRate.value

	def setDataRate(self, DataRate):
		_DataRate = ctypes.c_double(DataRate)

		__func = PhidgetSupport.getDll().PhidgetPressureSensor_setDataRate
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _DataRate)

		if result > 0:
			raise PhidgetException(result)


	def getMinDataRate(self):
		_MinDataRate = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetPressureSensor_getMinDataRate
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MinDataRate))

		if result > 0:
			raise PhidgetException(result)

		return _MinDataRate.value

	def getMaxDataRate(self):
		_MaxDataRate = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetPressureSensor_getMaxDataRate
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MaxDataRate))

		if result > 0:
			raise PhidgetException(result)

		return _MaxDataRate.value

	def getPressure(self):
		_Pressure = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetPressureSensor_getPressure
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_Pressure))

		if result > 0:
			raise PhidgetException(result)

		return _Pressure.value

	def getMinPressure(self):
		_MinPressure = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetPressureSensor_getMinPressure
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MinPressure))

		if result > 0:
			raise PhidgetException(result)

		return _MinPressure.value

	def getMaxPressure(self):
		_MaxPressure = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetPressureSensor_getMaxPressure
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MaxPressure))

		if result > 0:
			raise PhidgetException(result)

		return _MaxPressure.value

	def getPressureChangeTrigger(self):
		_PressureChangeTrigger = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetPressureSensor_getPressureChangeTrigger
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_PressureChangeTrigger))

		if result > 0:
			raise PhidgetException(result)

		return _PressureChangeTrigger.value

	def setPressureChangeTrigger(self, PressureChangeTrigger):
		_PressureChangeTrigger = ctypes.c_double(PressureChangeTrigger)

		__func = PhidgetSupport.getDll().PhidgetPressureSensor_setPressureChangeTrigger
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _PressureChangeTrigger)

		if result > 0:
			raise PhidgetException(result)


	def getMinPressureChangeTrigger(self):
		_MinPressureChangeTrigger = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetPressureSensor_getMinPressureChangeTrigger
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MinPressureChangeTrigger))

		if result > 0:
			raise PhidgetException(result)

		return _MinPressureChangeTrigger.value

	def getMaxPressureChangeTrigger(self):
		_MaxPressureChangeTrigger = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetPressureSensor_getMaxPressureChangeTrigger
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MaxPressureChangeTrigger))

		if result > 0:
			raise PhidgetException(result)

		return _MaxPressureChangeTrigger.value
