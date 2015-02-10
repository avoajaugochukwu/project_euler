import time
start = time.time()

sum_of_square = 0
square_of_sum = 0
#---------------------------------------------------------
number = 2
check = 0
counter = 1

def isPrime(number):
	for i in range(2, int(number ** 0.5 + 1)):
		if number % i == 0:
			return False
	else:
		return True


while counter <= 10001:
	if isPrime(number):
		counter += 1
	number += 1
print number-1, counter
# print number, counter
#---------------------------------------------------------
elapsed = time.time() - start
print 'time taken', elapsed
