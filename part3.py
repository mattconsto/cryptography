#!/usr/bin/env python3

import math, re, sys

# Part Three (XOR and Atbash)

def decipher(ciphertext):
	# Go forever basically.
	for keycount in range(1, 1000000):
		found = False
		print(str(keycount) + ":")

		for it in range(256**keycount):
			# Generate keys, then XOR each byte.
			keys = [math.floor(it / (256 ** i) % 256) for i in range(keycount)]
			middletext = [chr((ord(c)^keys[i%len(keys)])%256) for i,c in enumerate(ciphertext)]
			# Cut down results, to decode more complex strings alter the regex.
			if re.match(r"[a-z]{"+str(len(ciphertext))+"}", "".join(middletext)):
				found = True
				plaintext = [chr(25 - ord(c) + 2*ord("a")) for c in middletext]
				print(keys, "".join(plaintext))

		if not found: print("Nothing found.")
		print()

def encipher(keys, plaintext):
	# Substitute then XOR
	middletext = [chr(25 - ord(c) + 2*ord("a")) for c in plaintext]
	plaintext = [chr((ord(c)^keys[i%len(keys)])%256) for i,c in enumerate(middletext)]
	print("".join(plaintext))

if len(sys.argv) == 2:
	# Brute force decipher
	decipher(sys.argv[1])
elif len(sys.argv) == 3:
	# Encipher text
	keys = list(map(int, sys.argv[1].split(",")))
	encipher(keys, sys.argv[2])
else:
	print("Usage:", sys.argv[0], "- | CIPHERTEXT | KEY1,KEY2,... PLAINTEXT")
	# Default to show it working
	decipher("knztzgekbqekiqcevp`kdqaxzpjuknvpvpnqknztgrvpzzhokn~p`{eu`rvtddzzs")
	exit(1)
