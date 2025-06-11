class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        values = []

        for i in range(1<<n):
            store = []
            for j in range(n):
                if (i >> j) & 1:
                    store.append(nums[j])
            values.append(store)
       
        xo = []
        for v in values:
            start = 0
            for i in v:
                start = start | i
            xo.append(start)
        x = Counter(xo)
        maxV = 0
        ans = 0
        for key , val in x.items():
            if key > maxV:
                maxV = key
                ans = val
        print(ans)
        return ans



