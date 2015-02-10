import time
start = time.time()

sum_of_square = 0
square_of_sum = 0
#---------------------------------------------------------
number = 1
check = 0
counter = 1

def isPrime(number):
	for i in range(2, number):
		if number % i == 0:
			return False
	else:
		return True


while counter < 10001:
	for i in range(2, number):
		if number % i == 0:
			break
		else:
			# print number, counter
			counter += 1
	number += 2
print number, counter
#---------------------------------------------------------
elapsed = time.time() - start
print 'time taken', elapsed
