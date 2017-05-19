#!/usr/bin/python

p = raw_input("p: ")
q = raw_input("q: ")
e = raw_input("e: ")

phi = (int(p)-1) * (int(q)-1)

for d in range (0, 1000000):
   one = (int(e) * d) % phi
   if one == 1:
      print str(d) + " Found it!"
      break

