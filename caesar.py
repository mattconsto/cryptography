#!/usr/bin/env python3

import re

class Caesar():
	@staticmethod
	def shift(text, shift):
		text = bytearray(text, "utf8")
		for index in range(len(text)):
			if re.match(r"[a-z]", chr(text[index])):
				text[index] = ((text[index] - ord("a") + shift + 26) % 26) + ord("a")
			elif re.match(r"[A-Z]", chr(text[index])):
				text[index] = ((text[index] - ord("A") + shift + 26) % 26) + ord("A")
		return text.decode("utf-8")

	def encrypt(text, key):
		key = key.lower()
		prefix = ""
		avaliable = "abcdefghijklmnopqrstuvwxyz"

		for character in key:
			if character in avaliable:
				prefix += character
				avaliable = avaliable.replace(character, "")

		key = prefix + avaliable

		text = bytearray(text, "utf8")
		for index in range(len(text)):
			if re.match(r"[a-z]", chr(text[index])):
				text[index] = key.find(chr(text[index])) + ord("a")
			elif re.match(r"[A-Z]", chr(text[index])):
				text[index] = key.find(chr(text[index] - ord("A") + ord("a"))) + ord("A")
		return text.decode("utf-8")

	@staticmethod
	def unshift(text, shift):
		return Caesar.shift(text, -shift)

	@staticmethod
	def analyze(text):
		text = re.sub(r"[^a-z]", "", text.lower())
		table = {}
		for character in text:
			if not character in table:
				table[character] = 0
			table[character] += 1
		for character in table:
			table[character] /= len(text)
		return table

	@staticmethod
	def guess(text):
		analysis = Caesar.analyze(text)
		table = {"a": 0.08167, "b": 0.01492, "c": 0.02782, "d": 0.04253, "e": 0.12702, "f": 0.02228, "g": 0.02015, "h": 0.06094, "i": 0.06966, "j": 0.00153, "k": 0.00772, "l": 0.04025, "m": 0.02406, "n": 0.06749, "o": 0.07507, "p": 0.01929, "q": 0.00095, "r": 0.05987, "s": 0.06327, "t": 0.09056, "u": 0.02758, "v": 0.00978, "w": 0.02360, "x": 0.00150, "y": 0.01974, "z": 0.00074}
		order = "etaoinsrhdlucmfyywgpbvkxqjz"
		mapping = {}
		for (letter, frequency) in sorted(analysis.items(), key=lambda x:x[1], reverse=True):
			mapping[letter] = order[0]
			order = order[1:]

		output = ""

		for character in text:
			if re.match(r"[a-z]", character):
				output += mapping[character]
			elif re.match(r"[A-Z]", character):
				output += mapping[character.lower()].upper()
			else:
				output += character

		return output

plaintext = "The action of a Caesar cipher is to replace each plaintext letter with a different one a fixed number of places down the alphabet. The cipher illustrated here uses a left shift of three, so that (for example) each occurrence of E in the plaintext becomes B in the ciphertext. In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.[1]  The encryption step performed by a Caesar cipher is often incorporated as part of more complex schemes, such as the Vigenère cipher, and still has modern application in the ROT13 system. As with all single-alphabet substitution ciphers, the Caesar cipher is easily broken and in modern practice offers essentially no communication security.  Contents  1	Example 2	History and usage 3	Breaking the cipher 4	Notes 5	Bibliography 6	External links Example The transformation can be represented by aligning two alphabets; the cipher alphabet is the plain alphabet rotated left or right by some number of positions. For instance, here is a Caesar cipher using a left rotation of three places, equivalent to a right shift of 23 (the shift parameter is used as the key):  Plain:    ABCDEFGHIJKLMNOPQRSTUVWXYZ Cipher:   XYZABCDEFGHIJKLMNOPQRSTUVW When encrypting, a person looks up each letter of the message in the \"plain\" line and writes down the corresponding letter in the \"cipher\" line.  Plaintext:  THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG Ciphertext: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD Deciphering is done in reverse, with a right shift of 3.  The encryption can also be represented using modular arithmetic by first transforming the letters into numbers, according to the scheme, A → 0, B → 1, ..., Z → 25.[2] Encryption of a letter x by a shift n can be described mathematically as,[3]  {\displaystyle E_{n}(x)=(x+n)\mod {26}.} E_{n}(x)=(x+n)\mod {26}. Decryption is performed similarly,  {\displaystyle D_{n}(x)=(x-n)\mod {26}.} D_{n}(x)=(x-n)\mod {26}. (There are different definitions for the modulo operation. In the above, the result is in the range 0 to 25; i.e., if x + n or x − n are not in the range 0 to 25, we have to subtract or add 26.)  The replacement remains the same throughout the message, so the cipher is classed as a type of monoalphabetic substitution, as opposed to polyalphabetic substitution.  History and usage See also: History of cryptography  The Caesar cipher is named for Julius Caesar, who used an alphabet with a left shift of three. The Caesar cipher is named after Julius Caesar, who, according to Suetonius, used it with a shift of three to protect messages of military significance. While Caesar's was the first recorded use of this scheme, other substitution ciphers are known to have been used earlier.[4][5]  \"If he had anything confidential to say, he wrote it in cipher, that is, by so changing the order of the letters of the alphabet, that not a word could be made out. If anyone wishes to decipher these, and get at their meaning, he must substitute the fourth letter of the alphabet, namely D, for A, and so with the others.\"  — Suetonius, Life of Julius Caesar 56 His nephew, Augustus, also used the cipher, but with a right shift of one, and it did not wrap around to the beginning of the alphabet:  \"Whenever he wrote in cipher, he wrote B for A, C for B, and the rest of the letters on the same principle, using AA for Z.\"  — Suetonius, Life of Augustus 88 Evidence exists that Julius Caesar also used more complicated systems,[6] and one writer, Aulus Gellius, refers to a (now lost) treatise on his ciphers:  \"There is even a rather ingeniously written treatise by the grammarian Probus concerning the secret meaning of letters in the composition of Caesar's epistles.\"  — Aulus Gellius, Attic Nights 17.9.1–5 It is unknown how effective the Caesar cipher was at the time, but it is likely to have been reasonably secure, not least because most of Caesar's enemies would have been illiterate and others would have assumed that the messages were written in an unknown foreign language.[7] There is no record at that time of any techniques for the solution of simple substitution ciphers. The earliest surviving records date to the 9th century works of Al-Kindi in the Arab world with the discovery of frequency analysis.[8]  A Caesar cipher with a shift of one is used on the back of the mezuzah to encrypt the names of God. This may be a holdover from an earlier time when Jewish people were not allowed to have mezuzot. The letters of the cryptogram themselves comprise a religiously significant \"divine name\" which Orthodox belief holds keeps the forces of evil in check.[9]  In the 19th century, the personal advertisements section in newspapers would sometimes be used to exchange messages encrypted using simple cipher schemes. Kahn (1967) describes instances of lovers engaging in secret communications enciphered using the Caesar cipher in The Times.[10] Even as late as 1915, the Caesar cipher was in use: the Russian army employed it as a replacement for more complicated ciphers which had proved to be too difficult for their troops to master; German and Austrian cryptanalysts had little difficulty in decrypting their messages.[11]  Caesar ciphers can be found today in children's toys such as secret decoder rings. A Caesar shift of thirteen is also performed in the ROT13 algorithm, a simple method of obfuscating text widely found on Usenet and used to obscure text (such as joke punchlines and story spoilers), but not seriously used as a method of encryption.[12]  A construction of 2 rotating disks with a Caesar cipher can be used to encrypt or decrypt the code.  The Vigenère cipher uses a Caesar cipher with a different shift at each position in the text; the value of the shift is defined using a repeating keyword. If the keyword is as long as the message, chosen random, never becomes known to anyone else, and is never reused, this is the one-time pad cipher, proven unbreakable. The conditions are so difficult they are, in practical effect, never achieved. Keywords shorter than the message (e.g., \"Complete Victory\" used by the Confederacy during the American Civil War), introduce a cyclic pattern that might be detected with a statistically advanced version of frequency analysis.[13]  In April 2006, fugitive Mafia boss Bernardo Provenzano was captured in Sicily partly because some of his messages, clumsily written in a variation of the Caesar cipher, were broken. Provenzano's cipher used numbers, so that \"A\" would be written as \"4\", \"B\" as \"5\", and so on.[14]  In 2011, Rajib Karim was convicted in the United Kingdom of \"terrorism offences\" after using the Caesar cipher to communicate with Bangladeshi Islamic activists discussing plots to blow up British Airways planes or disrupt their IT networks. Although the parties had access to far better encryption techniques (Karim himself used PGP for data storage on computer disks), they chose to use their own scheme (implemented in Microsoft Excel), rejecting a more sophisticated code program called Mujhaddin Secrets \"because 'kaffirs', or non-believers, know about it, so it must be less secure\". [15]  Breaking the cipher Decryption shift	Candidate plaintext 0	exxegoexsrgi 1	dwwdfndwrqfh 2	cvvcemcvqpeg 3	buubdlbupodf 4	attackatonce 5	zsszbjzsnmbd 6	yrryaiyrmlac ... 23	haahjrhavujl 24	gzzgiqgzutik 25	fyyfhpfytshj The Caesar cipher can be easily broken even in a ciphertext-only scenario. Two situations can be considered:  an attacker knows (or guesses) that some sort of simple substitution cipher has been used, but not specifically that it is a Caesar scheme; an attacker knows that a Caesar cipher is in use, but does not know the shift value. In the first case, the cipher can be broken using the same techniques as for a general simple substitution cipher, such as frequency analysis or pattern words.[16] While solving, it is likely that an attacker will quickly notice the regularity in the solution and deduce that a Caesar cipher is the specific algorithm employed.   The distribution of letters in a typical sample of English language text has a distinctive and predictable shape. A Caesar shift \"rotates\" this distribution, and it is possible to determine the shift by examining the resultant frequency graph. In the second instance, breaking the scheme is even more straightforward. Since there are only a limited number of possible shifts (26 in English), they can each be tested in turn in a brute force attack.[17] One way to do this is to write out a snippet of the ciphertext in a table of all possible shifts[18] – a technique sometimes known as \"completing the plain component\".[19] The example given is for the ciphertext \"EXXEGOEXSRGI\"; the plaintext is instantly recognisable by eye at a shift of four. Another way of viewing this method is that, under each letter of the ciphertext, the entire alphabet is written out in reverse starting at that letter. This attack can be accelerated using a set of strips prepared with the alphabet written down in reverse order. The strips are then aligned to form the ciphertext along one row, and the plaintext should appear in one of the other rows.  Another brute force approach is to match up the frequency distribution of the letters. By graphing the frequencies of letters in the ciphertext, and by knowing the expected distribution of those letters in the original language of the plaintext, a human can easily spot the value of the shift by looking at the displacement of particular features of the graph. This is known as frequency analysis. For example, in the English language the plaintext frequencies of the letters E, T, (usually most frequent), and Q, Z (typically least frequent) are particularly distinctive.[20] Computers can also do this by measuring how well the actual frequency distribution matches up with the expected distribution; for example, the chi-squared statistic can be used.[21]  For natural language plaintext, there will typically be only one plausible decryption, although for extremely short plaintexts, multiple candidates are possible. For example, the ciphertext MPQY could, plausibly, decrypt to either \"aden\" or \"know\" (assuming the plaintext is in English); similarly, \"ALIIP\" to \"dolls\" or \"wheel\"; and \"AFCCP\" to \"jolly\" or \"cheer\" (see also unicity distance).  With the Caesar cipher, encrypting a text multiple times provides no additional security. This is because two encryptions of, say, shift A and shift B, will be equivalent to a single encryption with shift A + B. In mathematical terms, the set of encryption operations under each possible key forms a group under composition.[22]"
ciphertext = Caesar.shift(plaintext, 3)
decrypted = Caesar.unshift(ciphertext, 3)
keyed = Caesar.encrypt(plaintext, "Look Busy")
analysis = Caesar.guess(keyed)

print(plaintext)
print()
print(ciphertext)
print()
print(decrypted)
print()
print(keyed)
print()
print(analysis)
