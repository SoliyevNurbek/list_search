def find_min_count(data):
    """
    Given the list of numbers, Find count of minimum numbers in the list
    args:
        data: list of numbers
    returns: count of minimum numbers in the list
    """
    max1=data[0]
    i=0
    while i<len(data):
        if max1>data[i]:
            max1=data[i]
        i+=1
    return data.count(max1)
print(find_min_count([1, 8, 3, 8, 5]))
