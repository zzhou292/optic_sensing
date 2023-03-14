import sys
import ctypes
from Phidget22.PhidgetSupport import PhidgetSupport
from Phidget22.Async import *
from Phidget22.PhidgetException import PhidgetException

from Phidget22.Phidget import Phidget

class DistanceSensor(Phidget):

	def __init__(self):
		Phidget.__init__(self)
		self.handle = ctypes.c_void_p()

		if sys.platform == 'win32':
			self._DistanceChangeFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32)
		else:
			self._DistanceChangeFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32)
		self._DistanceChange = None
		self._onDistanceChange = None

		if sys.platform == 'win32':
			self._SonarReflectionsUpdateFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint32), ctypes.c_uint32)
		else:
			self._SonarReflectionsUpdateFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint32), ctypes.c_uint32)
		self._SonarReflectionsUpdate = None
		self._onSonarReflectionsUpdate = None

		__func = PhidgetSupport.getDll().PhidgetDistanceSensor_create
		__func.restype = ctypes.c_int32
		res = __func(ctypes.byref(self.handle))

		if res > 0:
			raise PhidgetException(res)

	def __del__(self):
		Phidget.__del__(self)

	def _localDistanceChangeEvent(self, handle, userPtr, distance):
		if self._DistanceChange == None:
			return
		self._DistanceChange(self, distance)

	def setOnDistanceChangeHandler(self, handler):
		if handler == None:
			self._DistanceChange = None
			self._onDistanceChange = None
		else:
			self._DistanceChange = handler
			self._onDistanceChange = self._DistanceChangeFactory(self._localDistanceChangeEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetDistanceSensor_setOnDistanceChangeHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onDistanceChange, None)
		except RuntimeError:
			self._DistanceChange = None
			self._onDistanceChange = None

	def _localSonarReflectionsUpdateEvent(self, handle, userPtr, distances, amplitudes, count):
		if self._SonarReflectionsUpdate == None:
			return
		distances = [distances[i] for i in range(8)]
		amplitudes = [amplitudes[i] for i in range(8)]
		self._SonarReflectionsUpdate(self, distances, amplitudes, count)

	def setOnSonarReflectionsUpdateHandler(self, handler):
		if handler == None:
			self._SonarReflectionsUpdate = None
			self._onSonarReflectionsUpdate = None
		else:
			self._SonarReflectionsUpdate = handler
			self._onSonarReflectionsUpdate = self._SonarReflectionsUpdateFactory(self._localSonarReflectionsUpdateEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetDistanceSensor_setOnSonarReflectionsUpdateHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onSonarReflectionsUpdate, None)
		except RuntimeError:
			self._SonarReflectionsUpdate = None
			self._onSonarReflectionsUpdate = None

	def getDataInterval(self):
		_DataInterval = ctypes.c_uint32()

		__func = PhidgetSupport.getDll().PhidgetDistanceSensor_getDataInterval
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_DataInterval))

		if result > 0:
			raise PhidgetException(result)

		return _DataInterval.value

	def setDataInterval(self, DataInterval):
		_DataInterval = ctypes.c_uint32(DataInterval)

		__func = PhidgetSupport.getDll().PhidgetDistanceSensor_setDataInterval
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _DataInterval)

		if result > 0:
			raise PhidgetException(result)


	def getMinDataInterval(self):
		_MinDataInterval = ctypes.c_uint32()

		__func = PhidgetSupport.getDll().PhidgetDistanceSensor_getMinDataInterval
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MinDataInterval))

		if result > 0:
			raise PhidgetException(result)

		return _MinDataInterval.value

	def getMaxDataInterval(self):
		_MaxDataInterval = ctypes.c_uint32()

		__func = PhidgetSupport.getDll().PhidgetDistanceSensor_getMaxDataInterval
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MaxDataInterval))

		if result > 0:
			raise PhidgetException(result)

		return _MaxDataInterval.value

	def getDataRate(self):
		_DataRate = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetDistanceSensor_getDataRate
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_DataRate))

		if result > 0:
			raise PhidgetException(result)

		return _DataRate.value

	def setDataRate(self, DataRate):
		_DataRate = ctypes.c_double(DataRate)

		__func = PhidgetSupport.getDll().PhidgetDistanceSensor_setDataRate
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _DataRate)

		if result > 0:
			raise PhidgetException(result)


	def getMinDataRate(self):
		_MinDataRate = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetDistanceSensor_getMinDataRate
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MinDataRate))

		if result > 0:
			raise PhidgetException(result)

		return _MinDataRate.value

	def getMaxDataRate(self):
		_MaxDataRate = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetDistanceSensor_getMaxDataRate
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MaxDataRate))

		if result > 0:
			raise PhidgetException(result)

		return _MaxDataRate.value

	def getDistance(self):
		_Distance = ctypes.c_uint32()

		__func = PhidgetSupport.getDll().PhidgetDistanceSensor_getDistance
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_Distance))

		if result > 0:
			raise PhidgetException(result)

		return _Distance.value

	def getMinDistance(self):
		_MinDistance = ctypes.c_uint32()

		__func = PhidgetSupport.getDll().PhidgetDistanceSensor_getMinDistance
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MinDistance))

		if result > 0:
			raise PhidgetException(result)

		return _MinDistance.value

	def getMaxDistance(self):
		_MaxDistance = ctypes.c_uint32()

		__func = PhidgetSupport.getDll().PhidgetDistanceSensor_getMaxDistance
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MaxDistance))

		if result > 0:
			raise PhidgetException(result)

		return _MaxDistance.value

	def getDistanceChangeTrigger(self):
		_DistanceChangeTrigger = ctypes.c_uint32()

		__func = PhidgetSupport.getDll().PhidgetDistanceSensor_getDistanceChangeTrigger
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_DistanceChangeTrigger))

		if result > 0:
			raise PhidgetException(result)

		return _DistanceChangeTrigger.value

	def setDistanceChangeTrigger(self, DistanceChangeTrigger):
		_DistanceChangeTrigger = ctypes.c_uint32(DistanceChangeTrigger)

		__func = PhidgetSupport.getDll().PhidgetDistanceSensor_setDistanceChangeTrigger
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _DistanceChangeTrigger)

		if result > 0:
			raise PhidgetException(result)


	def getMinDistanceChangeTrigger(self):
		_MinDistanceChangeTrigger = ctypes.c_uint32()

		__func = PhidgetSupport.getDll().PhidgetDistanceSensor_getMinDistanceChangeTrigger
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MinDistanceChangeTrigger))

		if result > 0:
			raise PhidgetException(result)

		return _MinDistanceChangeTrigger.value

	def getMaxDistanceChangeTrigger(self):
		_MaxDistanceChangeTrigger = ctypes.c_uint32()

		__func = PhidgetSupport.getDll().PhidgetDistanceSensor_getMaxDistanceChangeTrigger
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MaxDistanceChangeTrigger))

		if result > 0:
			raise PhidgetException(result)

		return _MaxDistanceChangeTrigger.value

	def getSonarQuietMode(self):
		_SonarQuietMode = ctypes.c_int()

		__func = PhidgetSupport.getDll().PhidgetDistanceSensor_getSonarQuietMode
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_SonarQuietMode))

		if result > 0:
			raise PhidgetException(result)

		return bool(_SonarQuietMode.value)

	def setSonarQuietMode(self, SonarQuietMode):
		_SonarQuietMode = ctypes.c_int(SonarQuietMode)

		__func = PhidgetSupport.getDll().PhidgetDistanceSensor_setSonarQuietMode
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _SonarQuietMode)

		if result > 0:
			raise PhidgetException(result)


	def getSonarReflections(self):
		_distances = (ctypes.c_uint32 * 8)()
		_amplitudes = (ctypes.c_uint32 * 8)()
		_count = ctypes.c_uint32()

		__func = PhidgetSupport.getDll().PhidgetDistanceSensor_getSonarReflections
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_distances), ctypes.byref(_amplitudes), ctypes.byref(_count))

		if result > 0:
			raise PhidgetException(result)

		return list(_distances), list(_amplitudes), _count.value
