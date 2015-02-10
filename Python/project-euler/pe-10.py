import time
time1 = time.time()

odds = range(3, 2000000, 2)
numbers = range(2, 700000)
primes = [True] * len(odds)
p = 0
total = 0

for n in odds:
    if primes[(n-3)/2]:
        p = n
        for m in numbers:
            if (m * p) > 2000000:
                break
            elif (m * p) % 2 != 0:
                primes[(m * p - 3)/2] = False

for n in odds:
    if primes[(n-3)/2]:
        total += n
        
print total + 2
print time.time() - time1