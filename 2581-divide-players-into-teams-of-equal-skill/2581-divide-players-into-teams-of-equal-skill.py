class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        team = n // 2
        skill.sort()
        ans = []
        pro = 0
        i , j = 0 , len(skill)-1

        while i < j:
            res = [skill[i] , skill[j]]
            if len(ans) >= 1 and sum(res) == sum(ans[-1]):
                ans.append(res)
                pro += skill[i] * skill[j]
                print(pro)
            elif len(ans) < 1:
                pro += skill[i] * skill[j]
                ans.append(res)
            i += 1
            j -= 1
        a = 0
        print(ans)
        print(pro)
        if len(ans) == team:
            return pro
        else:
            return -1


        