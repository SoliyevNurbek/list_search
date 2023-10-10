def find_max(data):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """
    max1=data[0]
    i=0
    s=[]
    while i<len(data):
        if max1<data[i]:
            max1=data[i]
        data.pop(i)
        i+=1
    s.append(max1)
    return s
print(find_max([1223,555,77777,898,78,9999]))
    