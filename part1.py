#!/usr/bin/env python3

from fractions import gcd
from functools import reduce
from collections import defaultdict
import math, re

# Part One (Viginere)

# Find the key length
def kasiki(ciphertext):
	# Adding a space ensures the last word is always added.
	ciphertext = re.sub(r"[^a-z ]", "", ciphertext.lower() + " ")
	positions = defaultdict(list)
	position = 0
	word = ""

	# Identify words
	for character in enumerate(ciphertext):
		if character == " ":
			if word != "":
				positions[word].append(position)
				word = ""
		else:
			word += character
			position += 1

	# Find deltas
	keylengths = []
	for entry in dict(filter(lambda entry: len(entry[1]) > 1, positions.items())).items():
		for index in range(len(entry[1]) - 1):
			keylengths.append(entry[1][index+1] - entry[1][index])

	# Reduce to find the common gcd
	return reduce(gcd, keylengths)

# Reformat lowercase alphabetic plaintext using ciphertext formatting.
def reformat(plain, cipher):
	return "".join(list(map(lambda c: plain.pop(0).lower() if c>="a" and c<="z" else (plain.pop(0).upper() if c>="A" and c<="Z" else c), cipher)))

def decipher(ciphertext, keylength, prefix):
	# Brute force, as the keylength is only 3
	lowertext = re.sub(r"[^a-z]", "", ciphertext.lower())
	for it in range(26**keylength):
		keys = [int((it / (26**n)) % 26) for n in range(keylength)]
		deciphered = [chr((ord(c) - ord("a") - keys[i%keylength]) % 26 + ord("a")) for i,c in enumerate(lowertext)]
		if "".join(deciphered).startswith(prefix):
			print(keys, reformat(deciphered, ciphertext))

# Find the keylength
ciphertext = "Ufs cpojl wt y kplrsmit kodfwoc, pvr ffoijpst qitrojlse ctgmfu rc nyworojl wu. Wcv kitr hsywo wcvp psywo rc dmbtgrfp omj dpqgjzwmghjcg cctpps nyyjlu ecqjqwplg. Mch zmis kwob synzpps ock qjodcg blr qpccypjjwugst. Jsbpb gpcn mhicft; uwtbcn qvbpse gg xggema fvdblrfb. Kicb gyqfb kjrv tmafrvjlu egtgcfflh blr egtggqvjh, dmbtgrfp wu y qiyzmcbhc."
keylength = kasiki(ciphertext)
print(keylength)
decipher(ciphertext, keylength, "the") # "the" is the prefix
