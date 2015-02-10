from math import sqrt
import time
start = time.time()
#---------------------------------------------------------

# lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lists = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
parser = 2520 # using 2520 increases the speed of execution
check = 0
while True:
	for i in lists:
		if parser % i == 0:
			check += 1

	if check == 10:
		print parser
		break;
	else:
		check = 0

	parser += 20 # using 2520 increases the speed of execution

#---------------------------------------------------------
elapsed = time.time() - start
print 'time taken', elapsed