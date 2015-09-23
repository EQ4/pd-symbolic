import OSC
import time

# Init OSC
c = OSC.OSCClient()
c.connect(('localhost', 7110)) # first argument is the IP of the host, second argument is the port to use

try:
	c.send(OSC.OSCMessage("/adress", 6)) # first argument is what we could call the OSC adress of the data, second argument is the actual data to be sent.
except:
	print "not connected"
        pass
