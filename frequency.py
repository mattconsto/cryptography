from collections import Counter

with open("secret.hex","rb") as f: ciphertext = f.read()
# ciphertext = bytearray("...".encode("cp1252"))
count = Counter(ciphertext)
output = ""
for i in range(0, 256):
	output += (str(i-ord("a")) + "\n") * count[i]
print(output)
