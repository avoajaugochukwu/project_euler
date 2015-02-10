import time, math
start = time.time()

#---------------------------------------------------------



def pythagoras(limit):
	for i in range(1, limit):
		for j in range(1, limit):
			for k in range(1, limit):

				if i**2 + j** 2 == k**2:
						# print i, j, k
						if i + j + k == 1000:
							print 'result', '>>>>', i, j, k
							print i * j * k
							return True

print pythagoras(500)

#---------------------------------------------------------
elapsed = time.time() - start
print 'time taken', elapsed
