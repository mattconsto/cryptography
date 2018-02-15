#!/usr/bin/env python3

from collections import Counter
from fractions import gcd
from functools import reduce
import re
import heapq
import math

# Part One
# ========
# Vinginere

def reformat(plain, cipher):
	index = 0; output = ""
	for c in cipher:
		if re.match(r"[a-zA-Z]", c):
			output += plain[index].upper() if re.match(r"[A-Z]", c) else plain[index].lower()
			index += 1
		else:
			output += c
	return output

ciphertext = "Ufs cpojl wt y kplrsmit kodfwoc, pvr ffoijpst qitrojlse ctgmfu rc nyworojl wu. Wcv kitr hsywo wcvp psywo rc dmbtgrfp omj dpqgjzwmghjcg cctpps nyyjlu ecqjqwplg. Mch zmis kwob synzpps ock qjodcg blr qpccypjjwugst. Jsbpb gpcn mhicft; uwtbcn qvbpse gg xggema fvdblrfb. Kicb gyqfb kjrv tmafrvjlu egtgcfflh blr egtggqvjh, dmbtgrfp wu y qiyzmcbhc."

print(reformat("".join([chr((ord(c) - ord("a") - [1,24,14][i%3]) % 26 + ord("a")) for i,c in enumerate(re.sub(r"[^a-z]", "", ciphertext.lower()))]), ciphertext))

# originaltext = "Ufs cpojl wt y kplrsmit kodfwoc, pvr ffoijpst qitrojlse ctgmfu rc nyworojl wu. Wcv kitr hsywo wcvp psywo rc dmbtgrfp omj dpqgjzwmghjcg cctpps nyyjlu ecqjqwplg. Mch zmis kwob synzpps ock qjodcg blr qpccypjjwugst. Jsbpb gpcn mhicft; uwtbcn qvbpse gg xggema fvdblrfb. Kicb gyqfb kjrv tmafrvjlu egtgcfflh blr egtggqvjh, dmbtgrfp wu y qiyzmcbhc."

# ciphertext = re.sub(r"[^a-z ]", "", originaltext.lower())
# frequencies = dict(filter(lambda item: item[0] != " ", Counter(ciphertext).items()))

# # find the key length
# def kasiki(ciphertext):
# 	positions = {}
# 	keylengths = []
# 	length = 0
# 	word = ""

# 	# Identify words
# 	for character in ciphertext.lower():
# 		if character == " ":
# 			if word != "":
# 				if not word in positions:
# 					positions[word] = []
# 				positions[word].append(length)
# 				word = ""
# 		else:
# 			word += character
# 			length += 1

# 	# Cleanup
# 	if word != "":
# 		if not word in positions:
# 			positions[word] = []
# 		positions[word].append(length)
# 		word = "" # Unnecessary

# 	# Find deltas
# 	for entry in dict(filter(lambda entry: len(entry[1]) > 1, positions.items())).items():
# 		for index in range(len(entry[1]) - 1):
# 			keylengths.append(entry[1][index+1] - entry[1][index])

# 	# Reduce to find the common gcd
# 	return reduce(gcd, keylengths)

# def vingere(ciphertext, keylength):
# 	frequencytable = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]

# 	def measurefrequencies(text, length = 26, offset = ord("a")):
# 		table = [0 for _ in range(length)]
# 		for character in text:
# 			table[ord(character) - offset] += 1
# 		for index in range(len(table)):
# 			table[index] /= len(text)
# 		return table

# 	def comparetables(alpha, beta):
# 		difference = abs(len(alpha) - len(beta))
# 		for index in range(min(len(alpha), len(beta))):
# 			difference += abs(alpha[index] - beta[index])
# 		return difference

# 	priorityqueue = []

# 	ciphertext = re.sub(r"[^a-z]", "", originaltext.lower())
# 	print(ciphertext)

# 	# bruteforce
# 	print(pow(len(frequencytable), keylength))
# 	for iteration in range(pow(len(frequencytable), keylength)):
# 		text = ""

# 		for index in range(len(ciphertext)):
# 			shift = math.floor((iteration / pow(len(frequencytable), index % keylength)) % len(frequencytable))
# 			text += chr(((shift - ord(ciphertext[index]) + ord("a") + 26) % len(frequencytable)) + ord("a"))

# 		difference = comparetables(measurefrequencies(text, len(frequencytable), ord("a")), frequencytable)
# 		heapq.heappush(priorityqueue, (difference, text))

# 		print(difference, originaltext)

# 	for entry in heapq.nlargest(25, priorityqueue):
# 		print(entry)

# 	for entry in heapq.nsmallest(25, priorityqueue):
# 		print(entry)

# 	return ""

# print("Ciphertext: " + originaltext)
# keylength = kasiki(ciphertext)
# print("keylength?: " + str(keylength))
# print("plaintext?: " + vingere(ciphertext, keylength))
