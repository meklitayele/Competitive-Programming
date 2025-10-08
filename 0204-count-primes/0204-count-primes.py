class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        if n == 1 or n == 0:
            return 0
        def sieve(num):
            is_prime = [True] * (num+1)
            is_prime[0] = False
            is_prime[1] = False

            i = 2
            while i * i <= num:
                if is_prime[i]:
                    j = i * i
                    while j <= num:
                        is_prime[j] = False
                        j += i
                i += 1
            return is_prime

        ans = sieve(n)
        count = 0
        for i in range(2,len(ans)-1):
            if ans[i] == True:
                count += 1
        
        return count

        # def checker(num):
        #     start = 2
        #     while start * start <= num:
        #         if num % start == 0:
        #             return False
        #         start += 1
        #     return True
        
        
        # count = 0
        # for i in range(2,n):
        #     if checker(i) == True:
        #         count += 1
        # return (count)



        
        