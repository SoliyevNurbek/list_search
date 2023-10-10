def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    max1=min1=data[0]
    i=0
    while i<len(data):
        if max1<data[i]:
            max1=data[i]
        if min1>data[i]:
            min1=data[i]
        i+=1
    return max1+min1
print(find_max_min_sum([1223,555,77777,898,78,9999]))
