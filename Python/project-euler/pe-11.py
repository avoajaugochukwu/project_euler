import time
start = time.time()
#---------------------------------------------------------
divisors = []
check = 0
num = 1
final = 1
while len(divisors) <= 2:
	# print divisors

	divisors = []
	for i in range(1, final + 1):
		if final % i == 0:
			# print 'final', final
			# print 'i', i
			if i not in divisors:
				divisors.append(i)
			# check += 1

	num += 1
	print 'num', num
	final += num
print divisors
# print len(divisors)
print final

# def visTriangle(num):
# 	final = 0
# 	for i in range(1, num+1):
# 		final += i
# 		# print final
# 		# print i
# 	print 'final', final

# 	divisors = 0
# 	for i in range(1, final + 1):
# 		if final % i == 0:
# 			divisors += 1

# 	print 'divisors', divisors



# visTriangle(40000)


#---------------------------------------------------------
elapsed = time.time() - start
print 'time taken', elapsed