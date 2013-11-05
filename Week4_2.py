dictionary = set()
lengths = {}

def reducible(word, verbose=False):
	if len(word) == 0:
		return True	
	if not word in dictionary:
		return False
	for i in range(len(word)):
		newWord = word[:i] + word[i+1:]
		if reducible(newWord, verbose):
			if verbose != False:
				print newWord
			lengths[len(word)] = word
			return True

fin = open("words.txt", "r")
for line in fin:
	dictionary.add(line.strip())
dictionary.add("a")
dictionary.add("i")

lengths = {}
for i in dictionary:
	reducible(i)

maxLength = 0
for length in lengths:
	if length > maxLength:
		maxLength = length

reducible(lengths[maxLength], True)
print lengths[maxLength]
