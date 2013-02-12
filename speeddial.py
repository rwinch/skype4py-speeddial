#!/usr/bin/python

# ---------------------------------------------------------------------------------------------
# This code is heavily based upon the sample found in the skype4py distrubiton. See
# https://github.com/awahlig/skype4py/blob/master/examples/callfriend.py

import time
import re
import sys
import Skype4Py
import signal

def handler(signum, frame):
    if(Call):
        Call.Finish()
    sys.exit()

signal.signal(signal.SIGINT, handler)

# This variable will get its actual value in OnCall handler
CallStatus = 0

# Here we define a set of call statuses that indicate a call has been either aborted or finished
CallIsFinished = set ([Skype4Py.clsFailed, Skype4Py.clsFinished, Skype4Py.clsMissed, Skype4Py.clsRefused, Skype4Py.clsBusy, Skype4Py.clsCancelled]);

def AttachmentStatusText(status):
   return skype.Convert.AttachmentStatusToText(status)

def CallStatusText(status):
    return skype.Convert.CallStatusToText(status)

# This handler is fired when status of Call object has changed
def OnCall(call, status):
    global CallStatus
    CallStatus = status
    if call.WaitTime and status == Skype4Py.clsInProgress:
        print 'Waiting ' + str(call.WaitTime) + ' seconds'
        time.sleep(call.WaitTime)
        print 'Entering Code ' + Call.Extension
        for c in Call.Extension:
          call.DTMF = c

# This handler is fired when Skype attatchment status changes
def OnAttach(status):
    if status == Skype4Py.apiAttachAvailable:
        skype.Attach()
        
# Let's see if we were started with a command line parameter..
try:
    CmdLine = sys.argv[1]
except:
    print 'Missing command line parameter'
    sys.exit()



# Creating Skype object and assigning event handlers..
skype = Skype4Py.Skype()
skype.OnAttachmentStatus = OnAttach
skype.OnCallStatus = OnCall

# Starting Skype if it's not running already..
if not skype.Client.IsRunning:
    print 'Starting Skype..'
    skype.Client.Start()

# Attatching to Skype..
skype.Attach()

number = re.search('(\d+)(,*)([\d#\*]*)', CmdLine)
Call = skype.PlaceCall(number.group(1))
Call.WaitTime = len(number.group(2))
Call.Extension = number.group(3)

#if not Found:
#    print 'Call target not found in contact list'
#    sys.exit()

# Loop until CallStatus gets one of "call terminated" values in OnCall handler
while not CallStatus in CallIsFinished:
    pass
