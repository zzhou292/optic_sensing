import sys
import ctypes
from Phidget22.PhidgetSupport import PhidgetSupport
from Phidget22.Async import *
from Phidget22.SPLRange import SPLRange
from Phidget22.PhidgetException import PhidgetException

from Phidget22.Phidget import Phidget

class SoundSensor(Phidget):

	def __init__(self):
		Phidget.__init__(self)
		self.handle = ctypes.c_void_p()

		if sys.platform == 'win32':
			self._SPLChangeFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double))
		else:
			self._SPLChangeFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double))
		self._SPLChange = None
		self._onSPLChange = None

		__func = PhidgetSupport.getDll().PhidgetSoundSensor_create
		__func.restype = ctypes.c_int32
		res = __func(ctypes.byref(self.handle))

		if res > 0:
			raise PhidgetException(res)

	def __del__(self):
		Phidget.__del__(self)

	def _localSPLChangeEvent(self, handle, userPtr, dB, dBA, dBC, Octaves):
		if self._SPLChange == None:
			return
		Octaves = [Octaves[i] for i in range(10)]
		self._SPLChange(self, dB, dBA, dBC, Octaves)

	def setOnSPLChangeHandler(self, handler):
		if handler == None:
			self._SPLChange = None
			self._onSPLChange = None
		else:
			self._SPLChange = handler
			self._onSPLChange = self._SPLChangeFactory(self._localSPLChangeEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetSoundSensor_setOnSPLChangeHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onSPLChange, None)
		except RuntimeError:
			self._SPLChange = None
			self._onSPLChange = None

	def getDataInterval(self):
		_DataInterval = ctypes.c_uint32()

		__func = PhidgetSupport.getDll().PhidgetSoundSensor_getDataInterval
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_DataInterval))

		if result > 0:
			raise PhidgetException(result)

		return _DataInterval.value

	def setDataInterval(self, DataInterval):
		_DataInterval = ctypes.c_uint32(DataInterval)

		__func = PhidgetSupport.getDll().PhidgetSoundSensor_setDataInterval
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _DataInterval)

		if result > 0:
			raise PhidgetException(result)


	def getMinDataInterval(self):
		_MinDataInterval = ctypes.c_uint32()

		__func = PhidgetSupport.getDll().PhidgetSoundSensor_getMinDataInterval
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MinDataInterval))

		if result > 0:
			raise PhidgetException(result)

		return _MinDataInterval.value

	def getMaxDataInterval(self):
		_MaxDataInterval = ctypes.c_uint32()

		__func = PhidgetSupport.getDll().PhidgetSoundSensor_getMaxDataInterval
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MaxDataInterval))

		if result > 0:
			raise PhidgetException(result)

		return _MaxDataInterval.value

	def getDataRate(self):
		_DataRate = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetSoundSensor_getDataRate
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_DataRate))

		if result > 0:
			raise PhidgetException(result)

		return _DataRate.value

	def setDataRate(self, DataRate):
		_DataRate = ctypes.c_double(DataRate)

		__func = PhidgetSupport.getDll().PhidgetSoundSensor_setDataRate
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _DataRate)

		if result > 0:
			raise PhidgetException(result)


	def getMinDataRate(self):
		_MinDataRate = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetSoundSensor_getMinDataRate
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MinDataRate))

		if result > 0:
			raise PhidgetException(result)

		return _MinDataRate.value

	def getMaxDataRate(self):
		_MaxDataRate = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetSoundSensor_getMaxDataRate
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MaxDataRate))

		if result > 0:
			raise PhidgetException(result)

		return _MaxDataRate.value

	def getdB(self):
		_dB = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetSoundSensor_getdB
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_dB))

		if result > 0:
			raise PhidgetException(result)

		return _dB.value

	def getMaxdB(self):
		_MaxdB = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetSoundSensor_getMaxdB
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MaxdB))

		if result > 0:
			raise PhidgetException(result)

		return _MaxdB.value

	def getdBA(self):
		_dBA = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetSoundSensor_getdBA
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_dBA))

		if result > 0:
			raise PhidgetException(result)

		return _dBA.value

	def getdBC(self):
		_dBC = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetSoundSensor_getdBC
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_dBC))

		if result > 0:
			raise PhidgetException(result)

		return _dBC.value

	def getNoiseFloor(self):
		_NoiseFloor = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetSoundSensor_getNoiseFloor
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_NoiseFloor))

		if result > 0:
			raise PhidgetException(result)

		return _NoiseFloor.value

	def getOctaves(self):
		_Octaves = (ctypes.c_double * 10)()

		__func = PhidgetSupport.getDll().PhidgetSoundSensor_getOctaves
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_Octaves))

		if result > 0:
			raise PhidgetException(result)

		return list(_Octaves)

	def getSPLChangeTrigger(self):
		_SPLChangeTrigger = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetSoundSensor_getSPLChangeTrigger
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_SPLChangeTrigger))

		if result > 0:
			raise PhidgetException(result)

		return _SPLChangeTrigger.value

	def setSPLChangeTrigger(self, SPLChangeTrigger):
		_SPLChangeTrigger = ctypes.c_double(SPLChangeTrigger)

		__func = PhidgetSupport.getDll().PhidgetSoundSensor_setSPLChangeTrigger
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _SPLChangeTrigger)

		if result > 0:
			raise PhidgetException(result)


	def getMinSPLChangeTrigger(self):
		_MinSPLChangeTrigger = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetSoundSensor_getMinSPLChangeTrigger
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MinSPLChangeTrigger))

		if result > 0:
			raise PhidgetException(result)

		return _MinSPLChangeTrigger.value

	def getMaxSPLChangeTrigger(self):
		_MaxSPLChangeTrigger = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetSoundSensor_getMaxSPLChangeTrigger
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MaxSPLChangeTrigger))

		if result > 0:
			raise PhidgetException(result)

		return _MaxSPLChangeTrigger.value

	def getSPLRange(self):
		_SPLRange = ctypes.c_int()

		__func = PhidgetSupport.getDll().PhidgetSoundSensor_getSPLRange
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_SPLRange))

		if result > 0:
			raise PhidgetException(result)

		return _SPLRange.value

	def setSPLRange(self, SPLRange):
		_SPLRange = ctypes.c_int(SPLRange)

		__func = PhidgetSupport.getDll().PhidgetSoundSensor_setSPLRange
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _SPLRange)

		if result > 0:
			raise PhidgetException(result)

