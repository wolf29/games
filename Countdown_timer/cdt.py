#!/usr/bin/python

import socket, sys, time
from datetime import timedelta
from threading import Thread

host = "countdown.ksc.nasa.gov"
textport = "8080"
second = timedelta(seconds = 1)

class Clock(Thread):
        nasastring = " -  "
        launch = timedelta(days = 0, hours = 1, minutes = 0, seconds = 0)
        counting = True
        def __init__(self, s):
                Thread.__init__(self)
                self.sock = s
        def run(self):
                while True:
                        buf = s.recv(2048)
                        if not len(buf):
                                return
                        self.nasastring = buf[1:]
                        fields = self.nasastring.split(" ")
                        if len(fields[0]):
                                TMinus = fields[0].split(":")
                                day = TMinus[0].replace('-', '').replace('+', '')
                                self.launch = timedelta(days=int(day), hours=int(TMinus[1]), minutes=int(TMinus[2]), seconds=int(TMinus[3]))
                                self.counting = fields[2]!="0"
        def tick(self):
                if(self.counting):
                        self.launch = self.launch - second if (self.nasastring[1] == "-") else self.launch + second
                s.send("")
                print "\rT", self.nasastring[0], self.launch, "and " + ("counting" if self.counting else "holding "),
                sys.stdout.flush()


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)

s.connect((host, port))
s.send("")
print "STS-127 (Endeavour) Launch in"
foo = Clock(s)
id = foo.start()
while True:
        foo.tick()
        time.sleep(1)
