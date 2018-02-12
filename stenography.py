#!/usr/bin/env python3

import re, struct, sys, zlib

try:
	from PIL import Image
except ModuleNotFoundError:
	print("Missing pillow! Install with `pip install pillow`, requires python3-devel and libjpeg-dev.")
	exit(1)

# Setup
image = Image.open(sys.argv[1])
pixels = image.load()

slimit = len(pixels[0,0]) if not isinstance(pixels[0,0], int) else 1
xlimit = image.width
ylimit = image.height
zlimit = 8

# Error checking
if image.palette != None:
	print("Paletted images are NOT supported, aborting!")
	exit(2)

if not image.mode in ["L", "RGB", "RGBA", "CMYK", "YCbCr", "LAB", "HSV"]:
	print("Unsupported mode: %s, aborting!" % image.mode)
	exit(3)

if len(sys.argv) == 2:
	# Extract message
	spointer = 0; xpointer = 0; ypointer = 0; zpointer = 0

	# Find the length of the message
	messageLength = bytearray(4)
	for lpointer in range(8*4):
		if slimit > 1:
			messageLength[lpointer // 8] |= (((list(pixels[xpointer, ypointer])[spointer] >> zpointer) & 1) << (lpointer % 8))
		else:
			messageLength[lpointer // 8] |= (((pixels[xpointer, ypointer] >> zpointer) & 1) << (lpointer % 8))

		spointer += 1
		if spointer >= slimit: spointer = 0; xpointer += 1
		if xpointer >= xlimit: xpointer = 0; ypointer += 1
		if ypointer >= ylimit: ypointer = 0; zpointer += 1
		if zpointer >= zlimit:
			print("Ran out of bits to read, something has gone wrong, aborting!")
			exit(4)
	
	messageLength = struct.unpack("I", messageLength)[0]
	message = bytearray(messageLength)

	for mpointer in range(messageLength*8):
		if slimit > 1:
			message[mpointer // 8] |= (((list(pixels[xpointer, ypointer])[spointer] >> zpointer) & 1) << (mpointer % 8))
		else:
			message[mpointer // 8] |= (((pixels[xpointer, ypointer] >> zpointer) & 1) << (mpointer % 8))

		spointer += 1
		if spointer >= slimit: spointer = 0; xpointer += 1
		if xpointer >= xlimit: xpointer = 0; ypointer += 1
		if ypointer >= ylimit: ypointer = 0; zpointer += 1
		if zpointer >= zlimit:
			print("Ran out of bits to read, something has gone wrong, aborting!")
			exit(4)

	print(zlib.decompress(message).decode("utf-8"))
elif len(sys.argv) == 3:
	# Insert message
	message = zlib.compress(sys.argv[2].encode("utf-8")) # Compress for more randomness and a smaller message
	message = struct.pack("I", len(message)) + message
	# print(str(message))

	if len(message) > image.width * image.height:
		print("Image smaller than message, aborting!")
		exit(5)

	spointer = 0; xpointer = 0; ypointer = 0; zpointer = 0

	for index in range(len(message)):
		for bit in range(8):
			if slimit > 1:
				pixel = list(pixels[xpointer, ypointer])
				pixel[spointer] = (pixel[spointer] & (~(1 << zpointer))) | ((message[index] >> bit) & 1)
				pixels[xpointer, ypointer] = tuple(pixel)
			else:
				pixels[xpointer, ypointer] = (pixels[xpointer, ypointer] & (~(1 << zpointer))) | ((message[index] >> bit) & 1)

			spointer += 1
			if spointer >= slimit: spointer = 0; xpointer += 1
			if xpointer >= xlimit: xpointer = 0; ypointer += 1
			if ypointer >= ylimit: ypointer = 0; zpointer += 1
			if zpointer >= zlimit:
				print("Ran out of bits to set, something has gone wrong, aborting!")
				exit(4)

	image.save("hidden_" + sys.argv[1])
else:
	print("%s FILE {MESSAGE}" % sys.argv[0])
	exit(1)
