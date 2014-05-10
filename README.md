invertedIndex
=============

Inverted Index data structure written in python. Use it in your next search engine.

SPECIFICATIONS
==============
InvertedIndex() generates a new structure. Calling the constructor with a filename will load that file.
addToken() will add a specific token into the data structure, with a specific line number. 
addString() will add a string of alphanumeric characters, separated by spaces, into the data structure
load() loads a single file, with line numbers as indices.
loadFile() loads a single file, in which all words are given the same index
loadMultipleFiles() loads a list of filenames, in which each document has a different index
lookupToken() looks up a single token
lookup() looks up any string. Any index associated with all words in the string will be returned, or None
write() writes the data structure to a file.



