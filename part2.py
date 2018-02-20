#!/usr/bin/env python3

import codecs, sys

# Part Two (XOR)

if len(sys.argv) == 2:
	# Decipher using keys from argv and data from stdin
	keys = list(map(int, sys.argv[1].split(",")))
	data = sys.stdin.buffer.read()
	print(bytearray([c^keys[i%len(keys)] for i,c in enumerate(data)]).decode("cp1252"))
elif len(sys.argv) == 3:
	# Decipher using keys and filename from argv
	keys = list(map(int, sys.argv[1].split(",")))
	with open(sys.argv[2],"rb") as f: data = f.read()
	print(bytearray([c^keys[i%len(keys)] for i,c in enumerate(data)]).decode("cp1252"))
else:
	print("Usage:", sys.argv[0], "KEY1,KEY2,... | KEY1,KEY2,... FILE")
	# Default to show it working
	with open("secret.hex","rb") as f: data = f.read()
	print(bytearray([c^[0x13,0x20][i%2] for i,c in enumerate(data)]).decode("cp1252"))
	exit(1)
