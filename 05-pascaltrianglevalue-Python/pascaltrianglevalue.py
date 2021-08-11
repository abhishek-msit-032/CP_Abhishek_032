# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 


def nCr(n, r):
    return (fact(n) / (fact(r) * fact(n - r)))
 
def fact(n):
    res = 1 
    for i in range(2, n+1):
        res = res * i      
    return res

def fun_pascaltrianglevalue(row, col):
	return int(nCr(row,col))