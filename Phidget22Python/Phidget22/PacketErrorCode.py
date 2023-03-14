import sys
import ctypes
class PacketErrorCode:
	# No error
	PACKET_ERROR_OK = 0
	# Unknown Error
	PACKET_ERROR_UNKNOWN = 1
	# The response packet timed out
	PACKET_ERROR_TIMEOUT = 2
	# Something about the received transmission didn't match the expected format.
	PACKET_ERROR_FORMAT = 3
	# The input lines are invalid. This likely means a cable has been unplugged.
	PACKET_ERROR_INVALID = 4
	# Data is being received fater than it can be processed. Some has been lost.
	PACKET_ERROR_OVERRUN = 5
	# Something behind the scenes got out of sequence.
	PACKET_ERROR_CORRUPT = 6

	@classmethod
	def getName(self, val):
		if val == self.PACKET_ERROR_OK:
			return "PACKET_ERROR_OK"
		if val == self.PACKET_ERROR_UNKNOWN:
			return "PACKET_ERROR_UNKNOWN"
		if val == self.PACKET_ERROR_TIMEOUT:
			return "PACKET_ERROR_TIMEOUT"
		if val == self.PACKET_ERROR_FORMAT:
			return "PACKET_ERROR_FORMAT"
		if val == self.PACKET_ERROR_INVALID:
			return "PACKET_ERROR_INVALID"
		if val == self.PACKET_ERROR_OVERRUN:
			return "PACKET_ERROR_OVERRUN"
		if val == self.PACKET_ERROR_CORRUPT:
			return "PACKET_ERROR_CORRUPT"
		return "<invalid enumeration value>"
