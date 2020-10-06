from string import ascii_lowercase

all_alphabets = set(ascii_lowercase)

def is_pangram(sentence):
	return True if all_alphabets.issubset(sentence.lower()) else False