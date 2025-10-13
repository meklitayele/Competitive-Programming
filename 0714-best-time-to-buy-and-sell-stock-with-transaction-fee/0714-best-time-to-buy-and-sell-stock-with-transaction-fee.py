class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        #min fee and max profit 
        dp = {}
        n = len(prices)
        def calc(idx,holding):
            if idx == n:
                return 0
            if (idx,holding) in dp:
                return dp[(idx,holding)]
            exclude = calc(idx+1,holding)
            if holding == 0:
                buy = calc(idx+1,1) - prices[idx]
                res = max(buy,exclude)
            else:
                sell = calc(idx+1,0) + prices[idx] - fee
                res = max(sell,exclude)
            dp[(idx,holding)] = res
            return res
        return calc(0,0)

            

        