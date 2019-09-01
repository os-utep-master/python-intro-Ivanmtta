import sys		# command line arguments
import re		# regular expression tools
import os		# checking if file exists

# Check program arguments are correct
if len(sys.argv) is not 3:
	print("Correct usage: wordCount.py <input text> <output file>")
	exit()

inputName = sys.argv[1]
outputName = sys.argv[2]

# Make sure input file exists
if not os.path.exists(inputName):
	print ("Text file input %s doesn't exist! Exiting" % inputName)
	exit()

# Make sure output file exists
if not os.path.exists(outputName):
	print ("WordCount output file %s doesn't exist! Exiting" % outputName)
	exit()

# Dictionary to storage the word counts
words = {}

# Open input file and populate dictionary
with open(inputName, "r") as inputFile:
	for line in inputFile:
		# Get rid of extra characters and newline characters, make it lower case
		# and split the line into a word list
		line = re.split(" ", re.sub("[^A-Za-z]+", " ", line).strip().lower())
		for word in line:
			if word in words:
				words[word] += 1
			else:
				words[word] = 1

# Write the words and the how many times they appear on the file into the output file
with open(outputName, "w") as outputFile:
	for word in sorted(words):
		if word is not "":
			outputFile.write(word + " " + str(words[word]) + "\n")