def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    max1=[]
    i=0
    while i<len(data):
        if data[i]%2==1:
            max1.append(data[i])
        i+=1
    max2=max1[0]
    j=0
    while j<len(max1):
        if max2>max1[j]:
            max2=max1[j]
        j+=1
    return max2
print(find_min_odd([7, 8, 4, 3, 5]))

