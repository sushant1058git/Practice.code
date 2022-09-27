#1. Two Sum
from math import fabs


nums=[2,7,11,15]
target=9
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
                
c=Solution()
print(c.twoSum(nums,target))

#2. Palindrome Number
class Solution:
    def isPalindrome(self, x):
        if str(x)==str(x)[::-1]:
            return True
        
c=Solution()
print(c.isPalindrome(121))


#3. Container With Most Water
height=[2,3,4,5,6]
class Solution:
    def maxArea(self, height) -> int:
        max_area=0
        area=0
        for i in range(0,len(height)):
            for j in range(i+1,len(height)):
                area=min(height[i],height[j])*(j-i)
                max_area=max(max_area,area)
        return max_area
            
c=Solution()
print(c.maxArea(height))


#4.Valid parenthesis Problem

string="()[({)}]"
opening=['(','{','[']
stack=[]

def isValid(string):
    for i in string:
        if i in opening:
            stack.append(i)
        elif stack==[]:
            return False
        elif i==')' and stack.pop()!='(' or i=='}' and stack.pop()!='{' or i==']' and stack.pop() != '[':
            return False
    return not stack
        
        
a=isValid(string)
print(a)
        