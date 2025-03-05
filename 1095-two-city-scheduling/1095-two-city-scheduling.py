class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        arr = []
        for a , b in costs :
            arr.append([a-b,a,b])

        arr.sort()
        ans = 0
        print(arr)
        for i in range(len(arr)):
            if i < len(arr) //2:
                ans += arr[i][1]
            else:
                ans += arr[i][2]

        return ans

    

        