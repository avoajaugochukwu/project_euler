from math import sqrt
import time
start = time.time()
#---------------------------------------------------------
number = 600851475143
def isPrime(number):
	i = 3
	while i < number:
		if number % i == 0:
			number = number / i
		i += 2

	return i
print isPrime(number)





#---------------------------------------------------------
elapsed = time.time() - start
print 'time taken', elapsed

check = 0

number = 600851475143 # number = 13195 # number = 2639
i = 3
solution = []
while i < 1000000:
	if number % i == 0:
		for j in range(1, i + 1):
			if i % j == 0:
				check += 1

		if check == 2:
			solution.append(i)
			check = 0

	i += 2

print 'answer', max(solution)