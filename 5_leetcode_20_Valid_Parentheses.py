""" As always, code works in vscode but not leetcode. I think i shouldn't use leetcode anymore to practice.
class Solution(object):
    def isValid(self, s):
        lengthS = len(s)
        if lengthS < 1:
            return False
           
        while "{}" in s:
            s = s.replace("{}","")
        while "()" in s:
            s = s.replace("()","")
        while "[]" in s:
            s = s.replace("[]","")
            
        if s == "":
            return True
        else:
            return False
            
             
s = "({})"    
    
k = Solution()

print(k.isValid(s))
"""
class Solution(object):
    def isValid(self, s):
        """ wuyi365 code NOT MINE
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n == 0:
            return True
        
        if n % 2 != 0:
            return False
            
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('{}','').replace('()','').replace('[]','')
        
        if s == '':
            return True
        else:
            return False
