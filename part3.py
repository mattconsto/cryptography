#!/usr/bin/env python3

import re

# Part Three
# ==========
# Hint: The original message contains alphabetical letters only,
#       and is encrypted using a two stage crypto-system.
# Hint: Part Two will help solve part three

ciphertext = bytearray("knztzgekbqekiqcevp`kdqaxzpjuknvpvpnqknztgrvpzzhokn~p`{eu`rvtddzzs".encode("ascii"))

for index in range(2**7):
	plaintext = bytearray()
	for character in ciphertext:
		plaintext.append(127 - character + 96 - index)

	print(plaintext.decode("cp1252"))
