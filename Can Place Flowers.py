class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        flowerbed = [0] + flowerbed + [0]
        c = 0
        for  i in range(1, len(flowerbed)-1):
            if flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                c = c+1
                flowerbed[i] = 1
        if c >= n :
            return True
        else: 
            return False