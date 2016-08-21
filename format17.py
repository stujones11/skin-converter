#!/usr/bin/python

import os
import sys
import Image

try :
	arg = sys.argv[1]
except IndexError :
	print "Usage: format17.py <file|dir>"
	sys.exit(1)

skins = [arg]
success = 0
failure = 0
path = ""
pl = "s"

if os.path.isdir(arg) :
	path = arg
	skins = os.listdir(arg)

for sfile in skins :
	sfile = os.path.join(path, sfile)
	try :
		imi = Image.open(sfile)
	except IOError :
		failure += 1
	else :
		w, h = imi.size
		if h == w and h >= 64 :
			imo = Image.new("RGBA", (w, h / 2))
			box = (0, 0, w, h / 2)
			imo.paste(imi.crop(box), box)
			imo.save(sfile)
			success += 1
		else :
			failure += 1

if success == 1 : pl = ""
print "%i skin%s successfully converted, %i failed" % (success, pl, failure)
