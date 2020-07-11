def interpolation_search(data, start, end, target):
    while start <= end and target >= data[start] and target <= data[end]:
        if start == end:
            if data[start] == target:
                return start
            return -1

        pos = start + \
            int(((float(end - start) /
                  (data[end]-data[start]))*(target - data[start])))

        if data[pos] == target:
            return pos

        if data[pos] < target:
            start = pos + 1

        else:
            end = pos - 1


data =  [10, 12, 13, 16, 18, 19, 20, 21]
target = 16

index = interpolation_search(data,0,len(data)-1,target)

if index != -1:
    print("{} is found at {}".format(target,index))
else:
    print("{} not found".format(target))
