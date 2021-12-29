class Solution(object):
    def longestCommonPrefix(self, strs):
        
        if strs[0] == "":
            return ""
        elif len(strs) < 2:
            return strs[0]
        else:
            lengthOfFirstString = len(strs[0])
            theWord = strs[0]
            combinations = []
            
            while lengthOfFirstString != 0:
                lengthOfFirstString = lengthOfFirstString - 1
                combinations.append(theWord)
                theWord = theWord[:-1]

            totalLengthOfArray = len(strs)
            amountFound = 0  
            valueFound = False
            
            for i, combValue in enumerate(combinations):
                if valueFound == True:
                    break
                else:
                    for j, oriValue in enumerate(strs):
                        while combValue < oriValue:
                            oriValue = oriValue[:-1]
                        if combValue == oriValue:
                            amountFound = amountFound + 1
                        else:
                            break
                    if amountFound == totalLengthOfArray:
                        valueFound = True
                        print(combValue)
                        return combValue
                    else:
                        amountFound = 0
            
            if valueFound == False:
                return ""
                    

strs = ["aa","ab"]

s = Solution()
s.longestCommonPrefix(strs)