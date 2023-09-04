from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]):
        n = len(nums)
        l, r = 1, n - 1
        while l <= r:
            mid = (l + r) // 2
            cn = 0
            for i in range(0, n):
                cn += nums[i] <= mid
            if cn <= mid:
                l = mid + 1
            else:
                r = mid - 1
                ans = mid
        return ans


if __name__ == "__main__":
    nums = [3,1,3,4,2]
    sol = Solution()
    print(sol.findDuplicate(nums=nums))
