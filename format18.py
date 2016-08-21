#!/usr/bin/python

import os
import sys
import Image

try :
	arg = sys.argv[1]
except IndexError :
	print "Usage: format18.py <file|dir>"
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
		if h * 2 == w :
			s = w / 64
			imo = Image.new("RGBA", (w, w))
			imo.paste(imi, (0, 0, w, h))
			# Right Leg
			rl_top = (4 * s, 16 * s, 8 * s, 20 * s)
			rl_btm = (8 * s, 16 * s, 12 * s, 20 * s)
			rl_ins = (8 * s, 20 * s, 12 * s, 32 * s)
			rl_out = (0, 20 * s, 4 * s, 32 * s)
			rl_fro = (4 * s, 20 * s, 8 * s, 32 * s)
			rl_bak = (12 * s, 20 * s, 16 * s, 32 * s)
			# Left Leg
			ll_top = (20 * s, 48 * s, 24 * s, 52 * s)
			ll_btm = (24 * s, 48 * s, 28 * s, 52 * s)
			ll_ins = (24 * s, 52 * s, 28 * s, 64 * s)
			ll_out = (16 * s, 52 * s, 20 * s, 64 * s)
			ll_fro = (20 * s, 52 * s, 24 * s, 64 * s)
			ll_bak = (28 * s, 52 * s, 32 * s, 64 * s)
			# Right Arm
			ra_top = (44 * s, 16 * s, 48 * s, 20 * s)
			ra_btm = (48 * s, 16 * s, 52 * s, 20 * s)
			ra_ins = (48 * s, 20 * s, 52 * s, 32 * s)
			ra_out = (40 * s, 20 * s, 44 * s, 32 * s)
			ra_fro = (44 * s, 20 * s, 48 * s, 32 * s)
			ra_bak = (52 * s, 20 * s, 56 * s, 32 * s)
			# Left Arm
			la_top = (36 * s, 48 * s, 40 * s, 52 * s)
			la_btm = (40 * s, 48 * s, 44 * s, 52 * s)
			la_ins = (40 * s, 52 * s, 44 * s, 64 * s)
			la_out = (32 * s, 52 * s, 36 * s, 64 * s)
			la_fro = (36 * s, 52 * s, 40 * s, 64 * s)
			la_bak = (44 * s, 52 * s, 48 * s, 64 * s)
			# Leg
			imo.paste(imi.crop(rl_top).transpose(Image.FLIP_LEFT_RIGHT), ll_top)
			imo.paste(imi.crop(rl_btm).transpose(Image.FLIP_LEFT_RIGHT), ll_btm)
			imo.paste(imi.crop(rl_ins).transpose(Image.FLIP_LEFT_RIGHT), ll_out)
			imo.paste(imi.crop(rl_out).transpose(Image.FLIP_LEFT_RIGHT), ll_ins)
			imo.paste(imi.crop(rl_fro).transpose(Image.FLIP_LEFT_RIGHT), ll_fro)
			imo.paste(imi.crop(rl_bak).transpose(Image.FLIP_LEFT_RIGHT), ll_bak)
			# Arm
			imo.paste(imi.crop(ra_top).transpose(Image.FLIP_LEFT_RIGHT), la_top)
			imo.paste(imi.crop(ra_btm).transpose(Image.FLIP_LEFT_RIGHT), la_btm)
			imo.paste(imi.crop(ra_ins).transpose(Image.FLIP_LEFT_RIGHT), la_out)
			imo.paste(imi.crop(ra_out).transpose(Image.FLIP_LEFT_RIGHT), la_ins)
			imo.paste(imi.crop(ra_fro).transpose(Image.FLIP_LEFT_RIGHT), la_fro)
			imo.paste(imi.crop(ra_bak).transpose(Image.FLIP_LEFT_RIGHT), la_bak)
			imo.save(sfile)
			success += 1
		else :
			failure += 1

if success == 1 : pl = ""
print "%i skin%s successfully converted, %i failed" % (success, pl, failure)
