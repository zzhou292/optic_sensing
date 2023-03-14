import sys
import ctypes
class PhidgetServerType:
	# Phidget22 Server<br/>Server discovery with this server type allows discovery of servers hosting Phidget devices. Enabling server discovery with this server type allows automated connection to these servers, and the Phidgets connected to them. Enabling server discovery with this server type will also enable ServerAdded and ServerRemoved events for this server type.
	PHIDGETSERVER_DEVICEREMOTE = 3
	# Phidget22 Web server<br/>Server discovery with this server type detects the presence of Phidget web servers used to communicate with in-browser JavaScript. Enabling server discovery with this server type will enable ServerAdded and ServerRemoved events for this server type.
	PHIDGETSERVER_WWWREMOTE = 6
	# Phidget SBC<br/>Server discovery with this server type detects the presence of Phidget SBCs on the network. Enabling server discovery with this server type will enable ServerAdded and ServerRemoved events for this server type.
	PHIDGETSERVER_SBC = 7

	@classmethod
	def getName(self, val):
		if val == self.PHIDGETSERVER_DEVICEREMOTE:
			return "PHIDGETSERVER_DEVICEREMOTE"
		if val == self.PHIDGETSERVER_WWWREMOTE:
			return "PHIDGETSERVER_WWWREMOTE"
		if val == self.PHIDGETSERVER_SBC:
			return "PHIDGETSERVER_SBC"
		return "<invalid enumeration value>"
