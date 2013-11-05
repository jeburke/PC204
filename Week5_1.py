import os
import sys
import operator

def count_extensions(directory):
	extDict = {}
	for root, dirs, files in os.walk(directory):
		for i in files:
			root, ext = os.path.splitext(i)
			if not ext in extDict:
				extDict[ext] = 1
			else:
				extDict[ext] += 1
	return extDict

exts = count_extensions(sys.argv[1])
sorted_exts = sorted(exts.iteritems(), key=operator.itemgetter(1))
for key, value in sorted_exts:
	print '%s \t %d' % (key, value)
