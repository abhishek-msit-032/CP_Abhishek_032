# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def property309(n):
	t=["0","1","2","3","4","5","6","7","8","9"]
	c=0
	r=n**5
	r=str(r)
	r1=set(r)

	r2=list(r1)
	r2.sort()

	for i in range(len(r2)):
	    if r2[i] in t:
	        c=c+1
	if c==10:
	    return True
	return False


def nthwithproperty309(n):

	c=0
	i=0
	while(c<=n):
		if property309(i):
			c+=1
		i=i+1
	return i-1