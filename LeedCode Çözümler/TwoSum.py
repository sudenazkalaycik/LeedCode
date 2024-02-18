# https://leetcode.com/problems/two-sum/description/  

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums) - 1): # Bu döngü her i elemanını geziyor
            for j in range(i + 1, len(nums)): # Bu döngü ise i' nin bir fazlasından başlayarak j değerleri alıyor
                control = nums[i] + nums[j]
                if control == target: 
                    return [i,j]
                
"""Burada yaptığımız şey önce listenin içinde son index hariç gezmek (her index i) ve başka bir döngü ile i değeri sbt iken
i indeksinden 1 fazla indexten başlayarak listenin son indexine kadar gezmek. Yani bu fonksiyon i değeri ile i den sonraki değerleri (j) tek tek toplar ve 
hedef sayıya eşit ise i ve j indexlerini döndürür"""

# Diğer bir çözüm 
#python3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # key -> value

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap: 
                return [prevMap[diff], i]  # Listede birden fazla hedef sayıyı sağlayan ikililer de olacaktır ama daima ilk değer döndürülecektir.
            prevMap[n] = i  # burada eğer diff prevMap in içerinde yoksa n i key value ikilisi oluşturulur
            
            
"""Burada ise privMap adında bir kütüphane oluşturuyoruz. Her  Farklı olarak enumerate() fonksiyonu kullandık. Enumarate liste demek içeridindeki elemanların indexlerini ve
değerlerini birlikte almamızı sağlar. Ör: enumerate([a,d,f,r,z]) dersek çıktısı: a,0   d,1  f,2  r,3  z,4   şeklinde olacaktır."""
            
            
            