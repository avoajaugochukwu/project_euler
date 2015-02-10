from math import sqrt
import time
start = time.time()
#---------------------------------------------------------
limit = 999
a = 100
b = 100
pal = 0
while a <= limit:
	for b in range(1, limit + 1):
		if str(a*b)[::-1] == str(a*b):
			if pal < a*b:
				pal = a*b

	a += 1
print pal

#---------------------------------------------------------
elapsed = time.time() - start
print 'time taken', elapsed
