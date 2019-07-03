#!/usr/bin/python
#

import hmac


def main():
   f = open("test_tags_shuffle")
   data = f.read().splitlines()
   key = "ae810b5d745031b4754679e52cc44ea987dfec32d9539b979bd6deb4cacf1d254e18214e1f58b2ab5b25bec3dd42cbc1b2465494ebdc0b4ec53e6eedfec04c1c"

   for line in data:
      fields = line.split(':')
      hm = hmac.new( key )
      msg = fields[0]
      hm.update (msg)
      d = hm.hexdigest()
     
      if d == fields[1].strip():
         print fields[0], fields[1]
      else:
         print ".\n"


if __name__ == "__main__":
   main()
