import sys
import ctypes
from Phidget22.PhidgetSupport import PhidgetSupport
from Phidget22.Async import *
from Phidget22.RCServoVoltage import RCServoVoltage
from Phidget22.PhidgetException import PhidgetException

from Phidget22.Phidget import Phidget

class RCServo(Phidget):

	def __init__(self):
		Phidget.__init__(self)
		self.handle = ctypes.c_void_p()
		self._setTargetPosition_async = None
		self._onsetTargetPosition_async = None

		if sys.platform == 'win32':
			self._PositionChangeFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double)
		else:
			self._PositionChangeFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double)
		self._PositionChange = None
		self._onPositionChange = None

		if sys.platform == 'win32':
			self._TargetPositionReachedFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double)
		else:
			self._TargetPositionReachedFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double)
		self._TargetPositionReached = None
		self._onTargetPositionReached = None

		if sys.platform == 'win32':
			self._VelocityChangeFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double)
		else:
			self._VelocityChangeFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double)
		self._VelocityChange = None
		self._onVelocityChange = None

		__func = PhidgetSupport.getDll().PhidgetRCServo_create
		__func.restype = ctypes.c_int32
		res = __func(ctypes.byref(self.handle))

		if res > 0:
			raise PhidgetException(res)

	def __del__(self):
		Phidget.__del__(self)

	def _localPositionChangeEvent(self, handle, userPtr, position):
		if self._PositionChange == None:
			return
		self._PositionChange(self, position)

	def setOnPositionChangeHandler(self, handler):
		if handler == None:
			self._PositionChange = None
			self._onPositionChange = None
		else:
			self._PositionChange = handler
			self._onPositionChange = self._PositionChangeFactory(self._localPositionChangeEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_setOnPositionChangeHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onPositionChange, None)
		except RuntimeError:
			self._PositionChange = None
			self._onPositionChange = None

	def _localTargetPositionReachedEvent(self, handle, userPtr, position):
		if self._TargetPositionReached == None:
			return
		self._TargetPositionReached(self, position)

	def setOnTargetPositionReachedHandler(self, handler):
		if handler == None:
			self._TargetPositionReached = None
			self._onTargetPositionReached = None
		else:
			self._TargetPositionReached = handler
			self._onTargetPositionReached = self._TargetPositionReachedFactory(self._localTargetPositionReachedEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_setOnTargetPositionReachedHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onTargetPositionReached, None)
		except RuntimeError:
			self._TargetPositionReached = None
			self._onTargetPositionReached = None

	def _localVelocityChangeEvent(self, handle, userPtr, velocity):
		if self._VelocityChange == None:
			return
		self._VelocityChange(self, velocity)

	def setOnVelocityChangeHandler(self, handler):
		if handler == None:
			self._VelocityChange = None
			self._onVelocityChange = None
		else:
			self._VelocityChange = handler
			self._onVelocityChange = self._VelocityChangeFactory(self._localVelocityChangeEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_setOnVelocityChangeHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onVelocityChange, None)
		except RuntimeError:
			self._VelocityChange = None
			self._onVelocityChange = None

	def getAcceleration(self):
		_Acceleration = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetRCServo_getAcceleration
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_Acceleration))

		if result > 0:
			raise PhidgetException(result)

		return _Acceleration.value

	def setAcceleration(self, Acceleration):
		_Acceleration = ctypes.c_double(Acceleration)

		__func = PhidgetSupport.getDll().PhidgetRCServo_setAcceleration
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _Acceleration)

		if result > 0:
			raise PhidgetException(result)


	def getMinAcceleration(self):
		_MinAcceleration = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetRCServo_getMinAcceleration
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MinAcceleration))

		if result > 0:
			raise PhidgetException(result)

		return _MinAcceleration.value

	def getMaxAcceleration(self):
		_MaxAcceleration = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetRCServo_getMaxAcceleration
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MaxAcceleration))

		if result > 0:
			raise PhidgetException(result)

		return _MaxAcceleration.value

	def getDataInterval(self):
		_DataInterval = ctypes.c_uint32()

		__func = PhidgetSupport.getDll().PhidgetRCServo_getDataInterval
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_DataInterval))

		if result > 0:
			raise PhidgetException(result)

		return _DataInterval.value

	def setDataInterval(self, DataInterval):
		_DataInterval = ctypes.c_uint32(DataInterval)

		__func = PhidgetSupport.getDll().PhidgetRCServo_setDataInterval
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _DataInterval)

		if result > 0:
			raise PhidgetException(result)


	def getMinDataInterval(self):
		_MinDataInterval = ctypes.c_uint32()

		__func = PhidgetSupport.getDll().PhidgetRCServo_getMinDataInterval
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MinDataInterval))

		if result > 0:
			raise PhidgetException(result)

		return _MinDataInterval.value

	def getMaxDataInterval(self):
		_MaxDataInterval = ctypes.c_uint32()

		__func = PhidgetSupport.getDll().PhidgetRCServo_getMaxDataInterval
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MaxDataInterval))

		if result > 0:
			raise PhidgetException(result)

		return _MaxDataInterval.value

	def getDataRate(self):
		_DataRate = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetRCServo_getDataRate
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_DataRate))

		if result > 0:
			raise PhidgetException(result)

		return _DataRate.value

	def setDataRate(self, DataRate):
		_DataRate = ctypes.c_double(DataRate)

		__func = PhidgetSupport.getDll().PhidgetRCServo_setDataRate
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _DataRate)

		if result > 0:
			raise PhidgetException(result)


	def getMinDataRate(self):
		_MinDataRate = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetRCServo_getMinDataRate
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MinDataRate))

		if result > 0:
			raise PhidgetException(result)

		return _MinDataRate.value

	def getMaxDataRate(self):
		_MaxDataRate = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetRCServo_getMaxDataRate
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MaxDataRate))

		if result > 0:
			raise PhidgetException(result)

		return _MaxDataRate.value

	def getEngaged(self):
		_Engaged = ctypes.c_int()

		__func = PhidgetSupport.getDll().PhidgetRCServo_getEngaged
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_Engaged))

		if result > 0:
			raise PhidgetException(result)

		return bool(_Engaged.value)

	def setEngaged(self, Engaged):
		_Engaged = ctypes.c_int(Engaged)

		__func = PhidgetSupport.getDll().PhidgetRCServo_setEngaged
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _Engaged)

		if result > 0:
			raise PhidgetException(result)


	def enableFailsafe(self, failsafeTime):
		_failsafeTime = ctypes.c_uint32(failsafeTime)

		__func = PhidgetSupport.getDll().PhidgetRCServo_enableFailsafe
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _failsafeTime)

		if result > 0:
			raise PhidgetException(result)


	def getMinFailsafeTime(self):
		_MinFailsafeTime = ctypes.c_uint32()

		__func = PhidgetSupport.getDll().PhidgetRCServo_getMinFailsafeTime
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MinFailsafeTime))

		if result > 0:
			raise PhidgetException(result)

		return _MinFailsafeTime.value

	def getMaxFailsafeTime(self):
		_MaxFailsafeTime = ctypes.c_uint32()

		__func = PhidgetSupport.getDll().PhidgetRCServo_getMaxFailsafeTime
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MaxFailsafeTime))

		if result > 0:
			raise PhidgetException(result)

		return _MaxFailsafeTime.value

	def getIsMoving(self):
		_IsMoving = ctypes.c_int()

		__func = PhidgetSupport.getDll().PhidgetRCServo_getIsMoving
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_IsMoving))

		if result > 0:
			raise PhidgetException(result)

		return bool(_IsMoving.value)

	def getPosition(self):
		_Position = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetRCServo_getPosition
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_Position))

		if result > 0:
			raise PhidgetException(result)

		return _Position.value

	def setMinPosition(self, MinPosition):
		_MinPosition = ctypes.c_double(MinPosition)

		__func = PhidgetSupport.getDll().PhidgetRCServo_setMinPosition
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _MinPosition)

		if result > 0:
			raise PhidgetException(result)


	def getMinPosition(self):
		_MinPosition = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetRCServo_getMinPosition
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MinPosition))

		if result > 0:
			raise PhidgetException(result)

		return _MinPosition.value

	def setMaxPosition(self, MaxPosition):
		_MaxPosition = ctypes.c_double(MaxPosition)

		__func = PhidgetSupport.getDll().PhidgetRCServo_setMaxPosition
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _MaxPosition)

		if result > 0:
			raise PhidgetException(result)


	def getMaxPosition(self):
		_MaxPosition = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetRCServo_getMaxPosition
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MaxPosition))

		if result > 0:
			raise PhidgetException(result)

		return _MaxPosition.value

	def setMinPulseWidth(self, MinPulseWidth):
		_MinPulseWidth = ctypes.c_double(MinPulseWidth)

		__func = PhidgetSupport.getDll().PhidgetRCServo_setMinPulseWidth
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _MinPulseWidth)

		if result > 0:
			raise PhidgetException(result)


	def getMinPulseWidth(self):
		_MinPulseWidth = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetRCServo_getMinPulseWidth
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MinPulseWidth))

		if result > 0:
			raise PhidgetException(result)

		return _MinPulseWidth.value

	def setMaxPulseWidth(self, MaxPulseWidth):
		_MaxPulseWidth = ctypes.c_double(MaxPulseWidth)

		__func = PhidgetSupport.getDll().PhidgetRCServo_setMaxPulseWidth
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _MaxPulseWidth)

		if result > 0:
			raise PhidgetException(result)


	def getMaxPulseWidth(self):
		_MaxPulseWidth = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetRCServo_getMaxPulseWidth
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MaxPulseWidth))

		if result > 0:
			raise PhidgetException(result)

		return _MaxPulseWidth.value

	def getMinPulseWidthLimit(self):
		_MinPulseWidthLimit = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetRCServo_getMinPulseWidthLimit
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MinPulseWidthLimit))

		if result > 0:
			raise PhidgetException(result)

		return _MinPulseWidthLimit.value

	def getMaxPulseWidthLimit(self):
		_MaxPulseWidthLimit = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetRCServo_getMaxPulseWidthLimit
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MaxPulseWidthLimit))

		if result > 0:
			raise PhidgetException(result)

		return _MaxPulseWidthLimit.value

	def resetFailsafe(self):
		__func = PhidgetSupport.getDll().PhidgetRCServo_resetFailsafe
		__func.restype = ctypes.c_int32
		result = __func(self.handle)

		if result > 0:
			raise PhidgetException(result)


	def getSpeedRampingState(self):
		_SpeedRampingState = ctypes.c_int()

		__func = PhidgetSupport.getDll().PhidgetRCServo_getSpeedRampingState
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_SpeedRampingState))

		if result > 0:
			raise PhidgetException(result)

		return bool(_SpeedRampingState.value)

	def setSpeedRampingState(self, SpeedRampingState):
		_SpeedRampingState = ctypes.c_int(SpeedRampingState)

		__func = PhidgetSupport.getDll().PhidgetRCServo_setSpeedRampingState
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _SpeedRampingState)

		if result > 0:
			raise PhidgetException(result)


	def getTargetPosition(self):
		_TargetPosition = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetRCServo_getTargetPosition
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_TargetPosition))

		if result > 0:
			raise PhidgetException(result)

		return _TargetPosition.value

	def setTargetPosition(self, TargetPosition):
		_TargetPosition = ctypes.c_double(TargetPosition)

		__func = PhidgetSupport.getDll().PhidgetRCServo_setTargetPosition
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _TargetPosition)

		if result > 0:
			raise PhidgetException(result)


	def setTargetPosition_async(self, TargetPosition, asyncHandler):
		_TargetPosition = ctypes.c_double(TargetPosition)

		_ctx = ctypes.c_void_p()
		if asyncHandler != None:
			_ctx = ctypes.c_void_p(AsyncSupport.add(asyncHandler, self))
		_asyncHandler = AsyncSupport.getCallback()

		__func = PhidgetSupport.getDll().PhidgetRCServo_setTargetPosition_async
		__func(self.handle, _TargetPosition, _asyncHandler, _ctx)


	def getTorque(self):
		_Torque = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetRCServo_getTorque
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_Torque))

		if result > 0:
			raise PhidgetException(result)

		return _Torque.value

	def setTorque(self, Torque):
		_Torque = ctypes.c_double(Torque)

		__func = PhidgetSupport.getDll().PhidgetRCServo_setTorque
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _Torque)

		if result > 0:
			raise PhidgetException(result)


	def getMinTorque(self):
		_MinTorque = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetRCServo_getMinTorque
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MinTorque))

		if result > 0:
			raise PhidgetException(result)

		return _MinTorque.value

	def getMaxTorque(self):
		_MaxTorque = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetRCServo_getMaxTorque
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MaxTorque))

		if result > 0:
			raise PhidgetException(result)

		return _MaxTorque.value

	def getVelocity(self):
		_Velocity = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetRCServo_getVelocity
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_Velocity))

		if result > 0:
			raise PhidgetException(result)

		return _Velocity.value

	def getVelocityLimit(self):
		_VelocityLimit = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetRCServo_getVelocityLimit
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_VelocityLimit))

		if result > 0:
			raise PhidgetException(result)

		return _VelocityLimit.value

	def setVelocityLimit(self, VelocityLimit):
		_VelocityLimit = ctypes.c_double(VelocityLimit)

		__func = PhidgetSupport.getDll().PhidgetRCServo_setVelocityLimit
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _VelocityLimit)

		if result > 0:
			raise PhidgetException(result)


	def getMinVelocityLimit(self):
		_MinVelocityLimit = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetRCServo_getMinVelocityLimit
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MinVelocityLimit))

		if result > 0:
			raise PhidgetException(result)

		return _MinVelocityLimit.value

	def getMaxVelocityLimit(self):
		_MaxVelocityLimit = ctypes.c_double()

		__func = PhidgetSupport.getDll().PhidgetRCServo_getMaxVelocityLimit
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_MaxVelocityLimit))

		if result > 0:
			raise PhidgetException(result)

		return _MaxVelocityLimit.value

	def getVoltage(self):
		_Voltage = ctypes.c_int()

		__func = PhidgetSupport.getDll().PhidgetRCServo_getVoltage
		__func.restype = ctypes.c_int32
		result = __func(self.handle, ctypes.byref(_Voltage))

		if result > 0:
			raise PhidgetException(result)

		return _Voltage.value

	def setVoltage(self, Voltage):
		_Voltage = ctypes.c_int(Voltage)

		__func = PhidgetSupport.getDll().PhidgetRCServo_setVoltage
		__func.restype = ctypes.c_int32
		result = __func(self.handle, _Voltage)

		if result > 0:
			raise PhidgetException(result)

