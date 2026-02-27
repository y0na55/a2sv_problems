def countingSort(arr):
    maxx = 100
    count = [0] * maxx
    
    for x in arr:
        count[x] += 1
    
    return count


