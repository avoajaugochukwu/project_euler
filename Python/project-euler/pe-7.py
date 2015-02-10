import time
start = time.time()

sum_of_square = 0
square_of_sum = 0
#---------------------------------------------------------
num = 3
prime_num = 3
not_prime = 0
count = 2
while count < 10001:
    num += 2
    sqrt = int(num ** 0.5 +1)
## you only have to check the odd numbers up to the square root of the number you are testing
## this way you will save time
    for i in range(3,sqrt,2):
        if num % i == 0:
            not_prime = num
    if not_prime != num:
        prime_num = num
        count += 1
print(prime_num)
#---------------------------------------------------------
elapsed = time.time() - start
print 'time taken', elapsed
