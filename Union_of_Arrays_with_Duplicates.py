class Solution:    
    def findUnion(self, a, b):
        combined_arr = a + b
        
        seen = set()
        union_num = []
        for num in combined_arr:
            if num not in seen:
                union_num.append(num)
                seen.add(num)
        return union_num

# combine the two arrays 
# make a set 
# initiate a empty union array
# then iterate through the combined array and then check if its in seen if not add it to the  empty union array and also to the seen set as well
# return the union array