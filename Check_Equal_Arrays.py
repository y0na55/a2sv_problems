class Solution:
    def checkEqual(self, a, b) -> bool:
        a.sort()
        b.sort()
        
        if len(a) != len(b):
            return False
        
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True
    
# sort the two arrays
# if then len of the arrays dont match return false
# iterate through one of the array and check each element matches 
