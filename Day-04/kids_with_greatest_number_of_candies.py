class Solution:
    def kidsWithCandies(self, candies, extraCandies):

        result = []
        max_candies = max(candies)

        for candy in candies:
            result.append(candy + extraCandies >= max_candies)

        return result
