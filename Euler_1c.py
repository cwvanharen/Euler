list_ = []
num = 0

while (num < 999):
	num += 1
	if ((num % 5) == 0 or (num % 3) == 0):
		list_.append(num)
	
print list_

total = sum(list_)

print "The sum of all the multiples of 3 or 5 below 1000 is %d." % total
