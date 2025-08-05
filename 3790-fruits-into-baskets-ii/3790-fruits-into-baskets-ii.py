class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        checked = set()
        count = len(fruits)
        
        for f in fruits:
            for i , v in enumerate(baskets):
                if v >= f and (i,v) not in checked:
                    count -= 1
                    checked.add((i,v))
                    break

        return count
        




        