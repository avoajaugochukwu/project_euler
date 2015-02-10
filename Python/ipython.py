import time, math
start = time.time()

#---------------------------------------------------------

def isPrime(number):
	for i in range(2, int(number ** 0.5 + 1)):
		if number % i == 0:
			return False
	else:
		return True

result = 0

for i in range(2, 2000000):
	if isPrime(i):
		print i
		result += i

print result
#---------------------------------------------------------
elapsed = time.time() - start
print 'time taken', elapsed
