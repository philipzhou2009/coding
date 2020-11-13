# https://leetcode.com/problems/product-of-array-except-self/

from typing import List

logger = print if True else lambda *arg: None


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        nLen = len(nums)
        
        list1 = []
        list2 = []
        
        counter = 0
        last = 1
        while counter < nLen:
            value = last * nums[counter] if counter> 0 else nums[0]
            last = value
            list1.append(value)
            counter+=1
        
        counter = nLen - 1
        last = 1
        while counter > -1:
            value = last * nums[counter] if counter < nLen-1 else nums[nLen-1]
            last = value
            list2.append(value)
            counter -= 1
        
        logger("list1=", list1)
        logger("list2=", list2)
        
        result = []
        
        for idx, value in enumerate(nums):
            
            if idx == 0:
                tmp = list2[nLen-1-1]
                
            elif idx == nLen -1:
                tmp = list1[nLen-1-1]
                
            else:
                tmp = list1[idx-1] * list2[nLen- idx-1-1 ] 
                
            
            logger("idx=%s,value=%s,tmp=%s" % (idx, value, tmp))
            result.append(tmp)
        pass

    
solution = Solution()
# solution.productExceptSelf([1, 2, 3, 4])
solution.productExceptSelf([5 ,10 ,15])