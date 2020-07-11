def quick_sort(data,start,end):
    if start < end:
        p = partition(data,start,end)
        quick_sort(data,start,p-1)
        quick_sort(data,p+1,end)
        return p

def partition(data,start,end):
    x, y, p = start,end,data[start]

    while x < y:
        while data[x] <= p:
            x += 1
        while data[y] > p:
            y -= 1
        if x < y :
            data[x],data[y] = data[y],data[x] 
    
    data[start] = data[y]
    data[y] = p
    return y


data =[5,3,2,6,4,1,3,7,10]
print("Before Sorting= ",data)
quick_sort(data,0,len(data)-1)
print("After Sorting= ",data)
