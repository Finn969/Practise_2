# -*- coding: utf-8 -*-	
#!/usr/bin/env python3

	# <QUESTION 1>

	# The most frequent task in this test is to find out which one of the given numbers differs from the others.
	# Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

	# <EXAMPLES>

	# iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

	# iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd

	# <HINT>
    
def example1(numbers):
	nstring = ''.join(numbers)
	nlist = nstring.split()
	nlist = list(map(int, nlist))
	odds = []
	evens = []
	for i in nlist:
		if i % 2 == 0:
			evens.append(i)
		else:
			odds.append(i)
	if len(odds) == 1:
		return nlist.index(odds[0])+1
	else:
		return nlist.index(evens[0])+1

# <QUESTION 2>

# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

def example2(s):
	t = sorted(s.split(), key=len)
	return len(t[0])

# <QUESTION 3>

# Create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

def example3(l):
	return filter(lambda i:not(type(i) is str), l)