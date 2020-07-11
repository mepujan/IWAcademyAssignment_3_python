def linear_search(data,value):
    for item in range(len(data)):
        if data[item] == value:
            return item
    return -1

data=[4,5,7,8,9,20,18,30]
index=linear_search(data,3)
if index == -1:
    print('Element is not found')
else:
    print("Element is found at index : ",index)
        