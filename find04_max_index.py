def find_max_index(data):
    """
    Given the list of numbers, return the index of maximum number in the list
    args:
        data: list of numbers
    returns: index of maximum number in the list
    """
    max1=data[0]
    i=0
    while i<len(data):
        if max1<data[i]:
            max1=data[i]
        i+=1
    return data.index(max1)
print(find_max_index([1223,555,77777,898,78,9999]))
