# https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s, t):
        Liste_s = []
        Liste_t = []

        for i in s:
            Liste_s.append(i)
        
        for j in t:
            Liste_t.append(j)


        Liste_t.sort() # liste sort() ile str ise alfabetik olarak int ise büyüklüğe göre sıralandı
        Liste_s.sort()
        
        # sort() bir değer döndürmez sadece orijinal listeyi sıralar ve listenin kendisine atar. sort() return ile hep none döndürür.
        
        # Liste_t.sort() == Liste_s.sort() burada her daim değer karşılığı none olacağından her daim birbirlerine eşit olacaklar!
        
        # Bu yüzden Liste_t.sort() == Liste_s.sort() sorgulaması yerine önce listeleri sort() ile sıraladık  
        # ve son hali alfabetik olarak sıralanmış olan listeleri karşılaştırdık.
       
        
        if Liste_t  == Liste_s  :
            return True
        else:
            return False

    #hash table ile de çözüm dene!