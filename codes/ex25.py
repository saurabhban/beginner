def break_works(words):
	words =words.split('')
	return words

def sort_words(words):
	return sorted(words)

def print_first_word(words):
	word=words.pop(0)
 	return word

def print_last_word(words):
	word=words.pop(-1)


def break_sentances(words):
	word=break_works(words)
	return sort_words(word)

def print_first_and_last(words):
	words = break_words(words)
	print_first_word(words)
	print_last_word(words)



