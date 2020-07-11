def merge_sort(data,start,end):
    if start < end:
        mid_value = (start + end)//2
        merge_sort(data,start,mid_value)
        merge_sort(data,mid_value+1,end)
        merge(data,start,mid_value,end)

def merge(data,start,mid_value,end):
    new_data = list(range(end-start+1))
    x,y,k= start, mid_value + 1 , 0
    while x <= mid_value and y <= end:
        if data[x] <= data [y]:
            new_data[k] = data[x]
            x += 1
            k += 1
        else:
            new_data[k] = data[y]
            y += 1
            k += 1
    while x <= mid_value:
        data[k] = data[x]
        x += 1
        k += 1
    while y <= end:
        new_data[k] = data[y]
        y += 1
        k +=1
    for i in range(start,end):
        data[i] = new_data[i-start]
            
data = [3,2,4,1,7,5,0]
merge_sort(data,0,len(data)-1)
print(data)
