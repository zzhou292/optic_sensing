import sys
import ctypes
class ErrorEventCode:
	# Client and Server protocol versions don't match. Ensure that both sides are using the same release of phidget22.
	EEPHIDGET_BADVERSION = 1
	# Check that the Phidget is not already open in another program, such as the Phidget Control Panel, or another program you are developing.
	EEPHIDGET_BUSY = 2
	# This could be a network communication issue, an authentication issue (if server password is enabled), or a Device access / hardware issue.
	EEPHIDGET_NETWORK = 3
	# An error occured dispatching a command or event.
	EEPHIDGET_DISPATCH = 4
	# A general failure occured - see description for details.
	EEPHIDGET_FAILURE = 5
	# An error state has cleared.
	EEPHIDGET_OK = 4096
	# A sampling overrun happened in firmware.
	EEPHIDGET_OVERRUN = 4098
	# One or more packets were lost.
	EEPHIDGET_PACKETLOST = 4099
	# Variable has wrapped around.
	EEPHIDGET_WRAP = 4100
	# Over-temperature condition detected.
	EEPHIDGET_OVERTEMP = 4101
	# Over-current condition detected.
	EEPHIDGET_OVERCURRENT = 4102
	# Out of range condition detected.
	EEPHIDGET_OUTOFRANGE = 4103
	# Power supply problem detected.
	EEPHIDGET_BADPOWER = 4104
	# Saturation condition detected.
	EEPHIDGET_SATURATION = 4105
	# Over-voltage condition detected.
	EEPHIDGET_OVERVOLTAGE = 4107
	# Failsafe condition detected.
	EEPHIDGET_FAILSAFE = 4108
	# Voltage error detected.
	EEPHIDGET_VOLTAGEERROR = 4109
	# Energy dump condition detected.
	EEPHIDGET_ENERGYDUMP = 4110
	# Motor stall detected.
	EEPHIDGET_MOTORSTALL = 4111
	# Invalid state detected.
	EEPHIDGET_INVALIDSTATE = 4112
	# Bad connection detected.
	EEPHIDGET_BADCONNECTION = 4113
	# Measurement is above the valid range.
	EEPHIDGET_OUTOFRANGEHIGH = 4114
	# Measurement is below the valid range.
	EEPHIDGET_OUTOFRANGELOW = 4115
	# Fault condition detected.
	EEPHIDGET_FAULT = 4116
	# Emergency stop condition detected.
	EEPHIDGET_ESTOP = 4117

	@classmethod
	def getName(self, val):
		if val == self.EEPHIDGET_BADVERSION:
			return "EEPHIDGET_BADVERSION"
		if val == self.EEPHIDGET_BUSY:
			return "EEPHIDGET_BUSY"
		if val == self.EEPHIDGET_NETWORK:
			return "EEPHIDGET_NETWORK"
		if val == self.EEPHIDGET_DISPATCH:
			return "EEPHIDGET_DISPATCH"
		if val == self.EEPHIDGET_FAILURE:
			return "EEPHIDGET_FAILURE"
		if val == self.EEPHIDGET_OK:
			return "EEPHIDGET_OK"
		if val == self.EEPHIDGET_OVERRUN:
			return "EEPHIDGET_OVERRUN"
		if val == self.EEPHIDGET_PACKETLOST:
			return "EEPHIDGET_PACKETLOST"
		if val == self.EEPHIDGET_WRAP:
			return "EEPHIDGET_WRAP"
		if val == self.EEPHIDGET_OVERTEMP:
			return "EEPHIDGET_OVERTEMP"
		if val == self.EEPHIDGET_OVERCURRENT:
			return "EEPHIDGET_OVERCURRENT"
		if val == self.EEPHIDGET_OUTOFRANGE:
			return "EEPHIDGET_OUTOFRANGE"
		if val == self.EEPHIDGET_BADPOWER:
			return "EEPHIDGET_BADPOWER"
		if val == self.EEPHIDGET_SATURATION:
			return "EEPHIDGET_SATURATION"
		if val == self.EEPHIDGET_OVERVOLTAGE:
			return "EEPHIDGET_OVERVOLTAGE"
		if val == self.EEPHIDGET_FAILSAFE:
			return "EEPHIDGET_FAILSAFE"
		if val == self.EEPHIDGET_VOLTAGEERROR:
			return "EEPHIDGET_VOLTAGEERROR"
		if val == self.EEPHIDGET_ENERGYDUMP:
			return "EEPHIDGET_ENERGYDUMP"
		if val == self.EEPHIDGET_MOTORSTALL:
			return "EEPHIDGET_MOTORSTALL"
		if val == self.EEPHIDGET_INVALIDSTATE:
			return "EEPHIDGET_INVALIDSTATE"
		if val == self.EEPHIDGET_BADCONNECTION:
			return "EEPHIDGET_BADCONNECTION"
		if val == self.EEPHIDGET_OUTOFRANGEHIGH:
			return "EEPHIDGET_OUTOFRANGEHIGH"
		if val == self.EEPHIDGET_OUTOFRANGELOW:
			return "EEPHIDGET_OUTOFRANGELOW"
		if val == self.EEPHIDGET_FAULT:
			return "EEPHIDGET_FAULT"
		if val == self.EEPHIDGET_ESTOP:
			return "EEPHIDGET_ESTOP"
		return "<invalid enumeration value>"
