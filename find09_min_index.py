def find_min_index(data):
    """
    Given the list of numbers, return the index of minimum number in the list
    args:
        data: list of numbers
    returns: index of minimum number in the list
    """
    max1=data[0]
    i=0
    while i<len(data):
        if max1>data[i]:
            max1=data[i]
        i+=1
    return data.index(max1)
print(find_min_index([1, 2, -3, 4, 5]))

