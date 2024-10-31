def isSorted(n: int,  a: [int]) -> int:
    # if a==sorted(a):
    #     return 1
    # else:
    #     return 0
    for i in range(n-1):
        if a[i+1]<a[i]:
            return 0
    return 1
