class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            x = str(x)
            y = x[::-1]
            return x == y

x = input()
x = int(x)

s = Solution()

print(s.isPalindrome(x))