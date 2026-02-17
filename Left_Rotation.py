def rotateLeft(d, arr):
    
    d = d % len(arr)

    start = arr[d:]
    end = arr[:d]
    result = start + end 
    
    return result
