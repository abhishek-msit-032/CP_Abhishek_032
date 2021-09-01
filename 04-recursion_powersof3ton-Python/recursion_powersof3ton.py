# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

def recursion_powersof3ton(n):
	# Your code goes here
	
	if (n<1):
		return None
	if (n==1):
		return [1]
	else:
		r=[]
		i=0
		out=0
		while(out<=n):
			out=3**i
			if out<=n:
				r.append(out)
			else:
				continue
			i=i+1
		return r
