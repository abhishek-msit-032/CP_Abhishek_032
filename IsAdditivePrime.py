def IsAdditivePrime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return False
                break
        else:
            num = str(num)
            sum = 0
            for i in num:
                sum += int(i)
            if sum > 1:
                for i in range(2, int(sum/2)+1):
                    if (sum % i) == 0:
                        return False
                        break
                else:
                    return True

            else:
                return False

    else:
        return False
print(IsAdditivePrime(13))