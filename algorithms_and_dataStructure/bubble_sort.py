def bubble_sort(data):
    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
                
    print('Sorted Data = ',data)


data = [3,5,2,9,1,7]
print("Before Sorting: ", data
)
bubble_sort(data)
