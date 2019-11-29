from math import ceil

class Solution:
    def __init__(self, nums):
        self.nums = nums
        self.maxsub = 0

    def solve(self):
        self.maxsub = self.devide(0, len(self.nums))
        print('{0}: {1}'.format(self.nums, self.maxsub))

    def devide(self, l, r):
        if r - l > 2:
            mid = ceil(l + (r - l) / 2)
            left = self.devide(l, mid)
            right = self.devide(mid, r)
            
            lefts = rights = s1 = s2 = 0
            for i in range(mid-1, l-1, -1):
                lefts += self.nums[i]
                s1 = lefts if lefts > s1 else s1
            for i in range(mid, r):
                rights += self.nums[i]
                s2 = rights if rights > s2 else s2
            
            return max(left, max(right, s1+s2))
    
        else:
            if l+1 < r:
                add = self.nums[l] + self.nums[l+1]
                best_out = max(self.nums[l+1], add)
                if best_out < 0:
                    best_out = 0
                best_in = max(self.nums[l], best_out)
            else:
                best_in = self.nums[l] if self.nums[l]>0 else 0

            return best_in


if __name__ == '__main__':
    demo = [-20, 11, -4, 13, -5, -2]
    solution = Solution(demo)
    solution.solve()
