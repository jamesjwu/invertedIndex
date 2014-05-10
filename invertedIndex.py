from contracts import *
import re, string; 
"""
Inverted Index Data Structure: Takes in a list of text files and generates 
a dictionary of ints that match each token with each occurence

James Wu
"""

DEBUG.contracts = False
class InvertedIndex(object):
	pattern = re.compile('[\W_]+')

	def __init__(self, info = None):
		#we store the content of the inverted index 
		#structure in a dictionary
		self.contents = {}
		if info:
			self.load(info)


	#addtoken: string * int -> void
	def addToken(self, token, line):
		requires(len(token.split()) <= 1) #we require the token is exactly one string
		requires(line >= 0)

		token = self.filterAlphanums(token)

		if token in self.contents:
			self.contents[token].add(line)
		else:
			self.contents[token] = set([line])

		ensures(token in self.contents)

	#regular expression to match only alphanumeric chars
	#filterAlphanums: string -> string
	def filterAlphanums(self, string):
		return InvertedIndex.pattern.sub("", string)


	#addString: string * int -> void
	#adds a string into the inverted index structure
	def addString(self, string, line):
		words = string.split()
		(map)(lambda x : self.addToken(x, line), words)

	#load: filename -> void
	#attempts to load a file and then read from it 
	#sentences that get converted into a invertedIndex structure
	def load(self, filename):
		#requires: filename is a valid file in the same directory
		#ensures: each token in the file is properly loaded
		text = open(filename, 'r')
		i = 0
		for line in text:
			if line:
				self.addString(line, i)
				i += 1

		text.close()

	#same as load, except takes in a line argument
	def loadFile(self, filename, linenum):
		#requires: filename is a valid file in the same directory
		#ensures: each token in the file is properly loaded
		text = open(filename, 'r')
		for line in text:
			if line:
				self.addString(line, linenum)

		text.close()

	#loadMultipleFiles: string list -> void
	def loadMultipleFiles(self, filenames):
		requires(type(filenames) == list)
		i = 0
		for f in filenames:
			self.loadFile(f, i)
			i += 1

	#lookup: string -> set
	def lookupToken(self, token):
		requires(len(token.split()) == 1) 
		#we require the token is exactly one string
		#ensures: returns a set of matches, or None if not in dict
		return self.contents.get(token, None)


	def lookup(self, string):
		words = string.split()
		return reduce(lambda x,y : x & y, map(self.lookupToken, words))


	#write: filename -> void
	#writes the contents of our data structure to a file for later use
	def write(self, filename):
		f = open(filename, 'w')
		for key in self.contents.keys():
			f.write(key)
			f.write(": [")			
			for x in list(self.contents[key]):
				f.write(str(x)+ ",")
			f.write("]\n")
		f.close()


		
