# Write the function nth_happy_number(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# assert(nth_happy_number(1) == 1)
# assert(nth_happy_number(2) == 7)
# assert(nth_happy_number(3) == 10)
# assert(nth_happy_number(4) == 13)
# assert(nth_happy_number(5) == 19)
# assert(nth_happy_number(6) == 23)
# assert(nth_happy_number(7) == 28)
# assert(nth_happy_number(8) == 31)

def square(n):
	r = 0
	while(n):
		r += (n % 10) * (n % 10)
		n = int(n / 10)
	return r

def isHappynumber(n):
    t = n
    f = n
    while(True):
        t = square(t)
        f = square(square(f))
        if(t != f):
            continue
        else:
            break
    return (t == 1)


def nth_happy_number(n):
	c=2
	i=2
	while(c<=n):
		if isHappynumber(i):
			c+=1
		i=i+1
	return i-1
