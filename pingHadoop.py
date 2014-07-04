#! /bin/env python
# D. Thiebaut
# http://www.wellho.net/solutions/python-python-threads-a-first-example.html
# this program launches several parallel threads, each one in charge of pinging
# a host and report on whether it is responding or dead.
# the hosts addresses are defined by the main for-loop:
#
# for hostId in ["01","02","03","04","05","06","07","08","09","10"]:
#      host = "hadoop1%s.dyndns.org" % hostId
#
# 
import os
import re
import time
import sys
from threading import Thread
 
class testit( Thread ):
   def __init__ ( self, ip ):
      Thread.__init__(self)
      self.ip = ip
      self.status = -1
 
   def run( self ):
      pingaling = os.popen( "ping -q -c2 " + self.ip, "r" )
      while True:
        line = pingaling.readline()
        if not line: break
        igot = re.findall(testit.lifeline, line)
        if igot:
           self.status = int( igot[0] )
 
#--- static members for the class ---
testit.lifeline = re.compile(r"(\d) received")
report = ( "No response", "Partial Response", "Alive")
 
print time.ctime()
 
pinglist = []
 
for hostId in ["01","02","03","04","05","06","07","08","09","10"]:
   #ip = "131.229.72."+str(host)
   host = "hadoop1%s.dyndns.org" % hostId
   current = testit( host )
   pinglist.append(current)
   current.start()
 
for pingle in pinglist:
   pingle.join()
 
for pingle in pinglist:
   print "Status from ",pingle.ip,"is",report[pingle.status]
