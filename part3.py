#!/usr/bin/env python3

import re

from collections import Counter

# Part Three
# ==========
# Hint: The original message contains alphabetical letters only,
#       and is encrypted using a two stage crypto-system.
# Hint: Part Two may help solve part three
# 
# oddly, all of the characters are in the range ` → ~, which is the last 32 characters in ascii. I wonder if it is important.
# My guess is some method which converts all of the characters into a printable set of characters, followed by a transposition cipher, but I am probably mistaken.

ciphertext = bytearray("knztzgekbqekiqcevp`kdqaxzpjuknvpvpnqknztgrvpzzhokn~p`{eu`rvtddzzs".encode("ascii"))

plaintext = ""

mapping = {122: "e", 107: "t", 112: "a", 110: "o", 118: "i", 101: "n", 113: "s", 116: "r", 96: "h", 100: "d", 103: "l", 117: "u", 114: "c", 98: "m", 105: "f", 99: "y", 97: "w", 120: "g", 106: "p", 104: "b", 111: "v", 126: "k", 123: "x", 127: "q", 115: "j"}

for character in ciphertext:
	plaintext += mapping[character]

print(plaintext)
