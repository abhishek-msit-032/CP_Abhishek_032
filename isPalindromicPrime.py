def isPalindromicPrime(n):
    new = str(n)
    new = new[::-1]
    new = int(new)
    if(new == n):
        if new > 1:
            for i in range(2, int(new/2)+1):
                if (new % i) == 0:
                    return False
                    break
            else:
                return True
        else:
            return False
    else:
        return False


n = int(input())
print(isPalindromicPrime(n))
