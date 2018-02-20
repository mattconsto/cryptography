#!/usr/bin/env python3

ciphertext = "Ufs cpojl wt y kplrsmit kodfwoc, pvr ffoijpst qitrojlse ctgmfu rc nyworojl wu. Wcv kitr hsywo..."

for shift in range(26):
	print(shift, "".join(list(map(lambda c: chr(((ord(c) - ord("a") - shift + 26) % 26) + ord("a")) if c>="a" and c<="z" else (chr(((ord(c) - ord("A") - shift + 26) % 26) + ord("A")) if c>="A" and c<="Z" else c), ciphertext))))
