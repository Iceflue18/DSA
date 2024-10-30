def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    #a=sorted(a)
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j+1]<a[j]:
                a[j],a[j+1]=a[j+1],a[j]
        # return a[i],a
    return a[n-2],a[1]