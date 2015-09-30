import OSC
import time

# OSC basic client
c = OSC.OSCClient()
c.connect(('localhost',7110)) # set the address for all following messages
s = OSC.OSCServer(('localhost',7111)) # basic receiver

# single message
v1 = 5

m1 = OSC.OSCMessage()
m1.setAddress("/print") # set OSC address
m1.append(v1) # append message
c.send(m1) # send it!


import socket
import time, threading

# this registers a 'default' handler (for unmatched messages),
# an /'error' handler, an '/info' handler.
# And, if the client supports it, a '/subscribe' & '/unsubscribe' handler
s.addDefaultHandlers()


# define a message-handler function for the server to call.
def printing_handler(addr, tags, stuff, source):
    print "---"
    print "received from :  %s" % OSC.getUrlStr(source)
    print "with addr : %s" % addr
    print "typetags : %s" % tags
    print "data : %s" % stuff
    print "---"

s.addMsgHandler("/uno", printing_handler) # adding our function, first parameter corresponds to the OSC address you want to listen to


# just checking which handlers we have added
print "Registered Callback-functions are :"
for addr in s.getOSCAddressSpace():
    print addr


# Start OSCServer
print "\nStarting OSCServer. Use ctrl-C to quit."
st = threading.Thread( target = s.serve_forever )
st.start()


try :
    while 1 :
        time.sleep(5)

except KeyboardInterrupt :
    print "\nClosing OSCServer."
    s.close()
    print "Waiting for Server-thread to finish"
    st.join() ##!!!
    print "Done"
