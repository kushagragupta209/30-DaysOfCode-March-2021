class Solution:
    def kidCandies(self, candies:list[int], extraCandies: int):
        k=[]
        for i in candies:
            i+extraCandies
            if i+extraCandies>=max(candies):
                k.append(True)
            if i+extraCandies<max(candies):
                k.append(False)
        return k
