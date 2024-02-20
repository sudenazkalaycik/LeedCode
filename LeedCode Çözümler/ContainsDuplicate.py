# https://leetcode.com/problems/contains-duplicate/description/

class Solution(object):
    def containsDuplicate(self, nums):
        Liste = []
        for i in range(len(nums)):
            if nums[i] in Liste:
                return True
            else:
                Liste.append(nums[i])
            
        return False 
# doğru çözüm fakat uzun sürüyor ve gereken zaman içerisinde çalışmıyor




class Solution:
    def containsDuplicate(self, nums):
        
        if len(nums) == len(set(nums)): # burada eğer uzunluğu setli haline eş çıkarsa listede her sayıdan 1 kez kullanılmış demektir.
            return False
        return True 
# en kısa ve doğru çözüm


