from invertedIndex import *

testingIndices = InvertedIndex()
def testAddToken():
	DEBUG.contracts = True
	testingIndices.addToken("hello", 1)
	testingIndices.addToken("hello", 0)
	testingIndices.addToken("yolo", 3)
	assert testingIndices.contents == {'yolo': set([3]), 'hello': set([0, 1])}

def testAddString():
	testingIndices.addString("hello my name is James", 2)
	assert testingIndices.contents == \
	{'name': set([2]), 'James': set([2]), 'is': set([2]), 'yolo': set([3]), 'my': set([2]), 'hello': set([0, 1, 2])}


def testAlphanums():
	assert "hello" == testingIndices.filterAlphanums("hello?")


def testLoad():
	testingIndices.load("testFile.txt")
	solution = {'enjoy': set([1]), 'what': set([2]), 'your': set([2]), 
	'name': set([0, 1]), 'I': set([1]), 'James': set([0]), 
	'is': set([0, 2]), 'favorite': set([2]), 'playing': set([1]), 
	'games': set([1]), 'word': set([2]), 'my': set([0]), 
	'hello': set([0])}
	assert solution == testingIndices.contents


def testWrite():
	testingIndices.write("outputFile.txt")

def testLoadMultipleFiles():
	testingIndices.loadMultipleFiles(["testFile.txt", "test2.txt"])
	assert len(testingIndices.contents) == 589

def testLookup():
	t = InvertedIndex()
	t.load("test2.txt")


testAddToken()
testAddString()
testAlphanums()
testingIndices = InvertedIndex()
testLoad()
testLookup()
testWrite()
testingIndices = InvertedIndex()
testLoadMultipleFiles()
