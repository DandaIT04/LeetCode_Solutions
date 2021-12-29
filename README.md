# LeetCode_Solutions
Decided to include my solutions for leetcode problems.

# LeetCode # 1 TwoSum

First leetcode problem and it was kind of a struggle. This is because at first i tried to ensure the number from the array cannot be larger than target number however my thoughts were invalid as negative numbers do exist in this problem. Even though i found this out, reduced a few lines of codes and ended up with a successful submission, it is still inefficient.

# LeetCode # 9 Palindrome Number

Took much longer than it could have been because codeforces and leetcode solutions are different. Codeforces require manual inputs while leetcode doesn't hence, if my provided solutions are with the mentality of codeforces solutions, leetcode solution checking will return errors

# LeetCode # 13 Roman To Integer

An hour and a half to complete. Actually spent 80% of the time using imagination/visualization about the most efficient method i could conjure to solve this method. Reached a conclusion to use count() to check if certain special roman combinations exists first e.g iv for 4, if any is found, remove the letters from the string n via replace("iv",""). After special characters are done, the normal characters will be next in line to convert to int.

The reason why my code is inefficient is because i have no clue at this time how to check if certain roman values exists and if they don't, line won't be executed or something.

Most efficient python solution adds roman numerals to dictionary(i considered this but didn't know how to implement into my solution).
Basically, start from len(n) - 1, from the last letter of string. If i = 5, where 5 is the 5th string letter, and j = i - 1, where 4 is the 4th string letter and if 4th string letter is smaller than 5th string letter, this means it is a special roman numeral combination e.g iv.

# LeetCode # 14 Longest Common Prefix

Took me 2 hours, 38 submissions. It really is difficult to find the most common prefix. Even after reading multiple efficient python solution, i still cannot understand how it can be done more efficiently, even with debugging.

# LeetCode # 20 Valid parenthesis

Probably be my last leetcode. LeetCode submissions are the only ones i always have a problem with. vscode returns correct values while leetcode doesn't. This happened twice.

# Next LeetCode when?
