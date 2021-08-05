class Solution: 
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return ( n & -n ) == n
        # using 2's complement 
        # Time Complexity: O(1)
