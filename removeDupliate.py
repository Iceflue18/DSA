def removeDuplicates(arr,n):
    # num=list(set(arr))
    # return len(num)
    dup=[]
    for i in range(n):

        if arr[i] not in dup:
            dup.append(arr[i])
        else:
            continue
    return len(dup)
