#!/usr/bin/env python3

import math, re, sys

# Part Three
# ==========
# Hint: The original message contains alphabetical letters only,
#       and is encrypted using a two stage crypto-system.
# Hint: Part Two may help solve part three
# 
# oddly, all of the characters are in the range ` → ~, which is the last 32 characters in ascii. I wonder if it is important.
# My guess is some method which converts all of the characters into a printable set of characters, followed by a transposition cipher, but I am probably mistaken.

# ciphertext = "knztzgekbqekiqcevp`kdqaxzpjuknvpvpnqknztgrvpzzhokn~p`{eu`rvtddzzs"
# ciphertext = "PzQeO`JeVdE|X~EpQ~TaPJ{NaX@"
# print(bytearray(ciphertext.encode("cp1252")))
# gsvivzivnliveloxzmlvhlmevmfhgszmzmblgsvikozmvgdrgsrmlfihlozihbhgvn
# therearemorevolcanoesonvenusthananyotherplanetwithinoursolarsystem

def decipher(ciphertext):
	# Go forever basically.
	for keycount in range(1, 1000000):
		found = False
		print(str(keycount) + ":")

		for it in range(256**keycount):
			# Generate keys, then XOR each byte.
			keys = [math.floor(it / (256 ** i) % 256) for i in range(keycount)]
			middletext = [chr((ord(c) ^ keys[i%len(keys)]) % 256) for i, c in enumerate(ciphertext)]
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

# search for[a-z]{66}

# gsvivzivnliveloxzmlvhlmevmfhgszmzmblgsvikozmvgdrgsrmlfihlozihbhgvn

# count = Counter(ciphertext)
# for i in range(96, 128):
# 	# test = (~(i & 0x1f)) + 0x60
# 	# print("0b{0:b}".format(test), chr(test), "x" * count[chr(i)])
# 	print("0b{0:b}".format(i), chr(i), "x" * count[chr(i)])
# print()

# 0b1100101 e xxxx
# 0b1111010 z xxxxxxxx

# for c in ciphertext: print(c, "0x{0:b}".format(ord(c)))

# output = ""
# for c in ciphertext:
# 	index = 32 - ord(c) + ord("`")
# 	# print(index)
# 	output += "       abcdefghijklmnopqrstuvwxyz          "[index]

# print(output)

# for columns in range(1, 10):
# 	matrix = ["" for _ in range(columns)]

# 	for i, c in enumerate(output):
# 		matrix[i % columns] += c

# 	for m in matrix:
# 		print(m)

# 	print()
