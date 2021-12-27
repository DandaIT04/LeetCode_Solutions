class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        valueToReturn = 0
        
        ivLetter = s.count("IV")
        while ivLetter != 0:
            ivLetter = ivLetter - 1
            valueToReturn = valueToReturn + 4
            s = s.replace("IV","")
        
        ixLetter = s.count("IX")
        while ixLetter != 0:
            ixLetter = ixLetter - 1
            valueToReturn = valueToReturn + 9
            s = s.replace("IX","")
            
        xlLetter = s.count("XL")
        while xlLetter != 0:
            xlLetter = xlLetter - 1
            valueToReturn = valueToReturn + 40
            s = s.replace("XL","")
            
        xcLetter = s.count("XC")
        while xcLetter != 0:
            xcLetter = xcLetter - 1
            valueToReturn = valueToReturn + 90
            s = s.replace("XC","")
        
        cdLetter = s.count("CD")
        while cdLetter != 0:
            cdLetter = cdLetter - 1
            valueToReturn = valueToReturn + 400
            s = s.replace("CD","")        
        
        cmLetter = s.count("CM")
        while cmLetter != 0:
            cmLetter = cmLetter - 1
            valueToReturn = valueToReturn + 900
            s = s.replace("CM","")        
        
        iLetter = s.count("I")
        while iLetter != 0:
            iLetter = iLetter - 1
            valueToReturn = valueToReturn + 1
            s = s.replace("I","")   
            
        vLetter = s.count("V")
        while vLetter != 0:
            vLetter = vLetter - 1
            valueToReturn = valueToReturn + 5
            s = s.replace("V","")   
            
        xLetter = s.count("X")
        while xLetter != 0:
            xLetter = xLetter - 1
            valueToReturn = valueToReturn + 10
            s = s.replace("X","")   
            
        lLetter = s.count("L")
        while lLetter != 0:
            lLetter = lLetter - 1
            valueToReturn = valueToReturn + 50
            s = s.replace("L","")   
            
        cLetter = s.count("C")
        while cLetter != 0:
            cLetter = cLetter - 1
            valueToReturn = valueToReturn + 100
            s = s.replace("C","")   
            
        dLetter = s.count("D")
        while dLetter != 0:
            dLetter = dLetter - 1
            valueToReturn = valueToReturn + 500
            s = s.replace("D","")   
            
        mLetter = s.count("M")
        while mLetter != 0:
            mLetter = mLetter - 1
            valueToReturn = valueToReturn + 1000
            s = s.replace("M","")
            
        return valueToReturn

theSolution = Solution()

s = "LVIII"

print(theSolution.romanToInt(s))
            
        