# shortenLongRuns(L, k) [15 pts]
# Write the non-destructive function shortenLongRuns(L, k) that takes a list L and a positive integer k, and
# non-destructively returns a similar list, only without any run of k consecutive equal values in L. This means that
# any values that would otherwise produce a consecutive run of k elements are not present.
# For example:
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 2) == [2, 3, 5, 3])
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 3) == [2, 3, 5, 5, 3])
# Note: your function may not just create a copy of L and call the destructive version of this function (below) on
# that copy and return it. Instead, you must directly construct the result here.

def shortenlongruns(L, k):
    c = 1
    for i in range(0, len(L)-1):
        if(L[i] == L[i+1]):
            c = c+1
    count = 1
    res = []
    for j in range(0, len(L)-1):
        if(L[j] == L[j+1]):
            count = count+1
            if(count >= k):
                continue
            res.append(L[j])
        elif L[j] != L[j+1]:
            res.append(L[j])
    res.append(L[-1])
    return res
