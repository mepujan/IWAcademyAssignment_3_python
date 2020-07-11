def insertion_sort(data):
    for i in range(1,len(data)):
        key= data[i]
        j=i-1
        while j >=0 and key < data[j]:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key

data =[5,3,2,6,4,1,3,7]
print("Before Sorting = ",data)
insertion_sort(data)
print("After Sorting= ",data)