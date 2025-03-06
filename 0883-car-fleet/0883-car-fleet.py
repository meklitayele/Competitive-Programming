class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #sort them by position
        # array1 = sorted([(position[i],i) for i in range(len(position))])
        # print(array1)
        pairs = sorted([[p,s] for p , s in zip(position,speed)],reverse = True)
        # print(pairs)

        store = []
        for p , s in pairs:
            time = (target - p) / s
            store.append(time)

            if len(store) >= 2 and store[-1] <= store[-2]:
                store.pop()

        return len(store)

            

        