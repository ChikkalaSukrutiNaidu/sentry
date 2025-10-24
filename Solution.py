from functools import lru_cache

class Solution:
    def climbStairs(self, n: int) -> int:

        # on the paper it looks like fibonacci
        @lru_cache
        def fibo(n):
            if n == 1: return 1
            elif n == 2: return 1
            else: return fibo(n-1)+fibo(n-2)

        return fibo(n+1)

        # be careful ! ! ! become smarter ! ! !  ;-)
        # w/o lru_cache it returns
        # time limit exceeded for n > 40
        
