class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = nums
        self.target = target

        """                   
        original submitted fully working code
        [runtime: 5064ms// faster than 13% python submission,memory usage: 14MB// less than 97% python submission]
        """      
        """
        theAnswerList = []

        firstNum = -1
        secondNum = 1

        for theNumbers in nums:
            firstNum += 1
            secondNum = firstNum + 1
            if len(theAnswerList) == 2:
                break
            else:
                for nextNumbers in nums[secondNum:len(nums)]:
                    if len(theAnswerList) == 2:
                        break
                    else:
                        if theNumbers + nextNumbers == target:
                            theAnswerList.insert(0,firstNum)                                    
                            theAnswerList.insert(1,secondNum)
                    secondNum += 1               
        
        return theAnswerList
        """
        
        """    
        learned code[runtime: 40ms// faster than 93.63% python submission,memory usage: 14.3MB// less than 48.54% python submission]
        """        
        discovered = {}
        
        for count, value in enumerate(nums):
            undiscovered = target - nums[count]
            if undiscovered in discovered:
                return [count,discovered[undiscovered]]
            discovered[value] = count
            
        """
        Basically, it will store discovered nums value in discovered{}
        when target-nums[count] exists in discovered,
        return the current count for the recent discovery and the previously discovered in discovered{}
        
        [1,3,5,7], target = 8
        
        discovered = {}
        
        8 - 1 = 7 discovered {1}
        8 - 3 = 5 discovered {1,3}
        8 - 5 = 3 
        
        result of 8 - 5 = 3 is in discovered {1,3} <---- where index is 1
        8 - 5 = 3 happens when count = 2, (count starts from 0 NOT 1)!
        return [1,2] which is [count,discovered[undiscovered]]

        (https://www.code-recipe.com/post/two-sum)
        """ 

nums = [1,3,5,7]
target = 8

s = Solution() 
print(s.twoSum(nums,target))       