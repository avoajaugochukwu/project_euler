from math import sqrt
import time
start = time.time()
#---------------------------------------------------------
result = []
count = 0
for i in range(2520, 2600, 10):
	for j in range(1, 11):
		if i % j == 0:
			count += 1
			print i, count
			if count == 10:
				print 'I am Here'
		elif count == 10:
			print 'answer', i
			break
		else:
			count = 0

# if count == 10:
# 	print count




#---------------------------------------------------------
elapsed = time.time() - start
print 'time taken', elapsed



def isFactor(value, factor):
	if factor > 0 and value % factor == 0:
		return True
	else:
		return False

def increase(num, check):
	i = 11
	while i < 21:
		if isFactor(num, i):
			# print i
			check += 1
		i += 1
	return check
