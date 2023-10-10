def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    max1=data[0]
    i=0
    while i<len(data):
        if max1<data[i]:
            max1=data[i]
        i+=1
    return data.count(max1)
print(find_max_count([1223,555,77777,898,78,9999,77777]))
