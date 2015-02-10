import time
start = time.time()

sum_of_square = 0
square_of_sum = 0
#---------------------------------------------------------
for i in range(1, 101):
	sum_of_square += i**2

	square_of_sum += i


print sum_of_square
print square_of_sum**2
solution = square_of_sum**2 - sum_of_square
print solution

#---------------------------------------------------------
elapsed = time.time() - start
print 'time taken', elapsed
