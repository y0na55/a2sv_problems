class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        string_s = ''.join(sorted(s))
        string_t = ''.join(sorted(t))


        if string_s == string_t:
            return True

        else:
            return False


if __name__ == "__main__":
    soln = Solution()
    s = "anagram"
    t = "nagaram"
    
    result = soln.isAnagram(s, t)
    
    print(f"Is 'anagram' an anagram of 'nagaram'? \n{soln.isAnagram('anagram', 'nagaram')}")
    print(f"Is 'rat' an anagram of 'car'? \n{soln.isAnagram('rat', 'car')}")
