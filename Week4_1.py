def has_dups(test_list):
	return len(set(test_list)) != len(test_list)


def has_dups_list(test_list):
	for i in range(len(test_list)):
		for j in range(i+1, len(test_list)):
			if test_list[j] == test_list[i]:
				return True
	return False
	

def timing(func, argument, repeat=1000):
	import time
	total = 0.0
	for i in range(repeat):
		start = time.time()
		func(argument)
		total += time.time() - start
	print "Average time (s):", total / repeat * 1000.0

test_list = list(range(1000))

print has_dups(test_list)
print has_dups_list(test_list)

timing(has_dups, test_list)
timing(has_dups_list, test_list)

test_list = list(range(1000)) ; test_list[-1] = test_list[500]

print has_dups(test_list)
print has_dups_list(test_list)

timing(has_dups, test_list)
timing(has_dups_list, test_list)

test_list = list(range(1000)) ; test_list[1] = test_list[0]

print has_dups(test_list)
print has_dups_list(test_list)

timing(has_dups, test_list)
timing(has_dups_list, test_list)
