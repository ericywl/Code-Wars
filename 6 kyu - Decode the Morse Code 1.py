def decodeMorse(morseCode):
	sentence = ""
	new_morseCode = morseCode.strip()
	for morseWords in new_morseCode.split("   "):
		for morseChar in morseWords.split(" "):
			sentence += MORSE_CODE[morseChar]
		sentence += " "
	return sentence[:-1]