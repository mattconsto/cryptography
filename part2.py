#!/usr/bin/env python3

import codecs, sys

# Part Two
# ========
# Hint: The first letter of the original message is A
# Are NULs significant?

# ciphertext = "R !3YvAa |Lw qOj `EvI}G3OfT3FaO~ gHv gRrI}²` dI}D|W3S{OfTvD–--³WAw3L|Ox gHv gRvE` rRv tOzNt qE{I}D2´*WAw `MzLvD3A}D3A3Y|U}G3C|UcLv `IgTzNt }ErRqY? O|KvD3Ag gHv !3YvAa |Lw²` pHzLwI`H3BvHrVzOa dIgH3PzTj3SfDwE}Lj {E3AtAzN3EkCAzMvD–--³WAw3L|Ox gHv pL|UwS3AaE3RfN}I}G3WzT{ fS2´**GHv pOfPE3C|UD}²g aE`I`T3A}D3SrIw gO3T{E3OD3MrN–--³DHj wO}²g jOf gAxE3Y|Ua `O} gO3A3G|Ow wOpT|R,´3t{E3OD3MrN3S~IEw rNw `AzD–³Z wIw rNw dE3AaE3JfSg pO~I}G3FaO~ gHv {O`PzTrL? ~Y3S|N3WrS3BI}D3FaO~ qIaT{3Hv yU`T3G|T3HzS3EjE` gOwAj‡--eeEaY3SzNtLv cEaS|N3O} gHv cLrNvT3HrS3A3SgOaY= WO}²g yUwGv cE|PE3BvF|Rv jOf gRfLj xN|W3T{E~3t{E3TaUgH3MzG{T3SfRcRzSv jOf"

#     0x52 = 0b0101_0010
# xor 0x13 = 0b0001_0011
#   = 0x41 = 0b0100_0001

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
