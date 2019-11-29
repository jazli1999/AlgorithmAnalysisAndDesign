from math import ceil

class Solution:
    # find the minimal number and its index
    def __init__(self, nums):
        self.all = nums
        self.minimal = None
        self.pos = None
    
    def solve(self):
        self.minimal, self.pos = self.devide(self.all, 0, len(self.all))
        print('Minimal {0} at index {1}'.format(self.minimal, self.pos))

    def devide(self, nums, l, r):
        if r - l > 2:
            mid = ceil(l + (r - l) / 2)

            left = list(self.all[l: mid])
            right = list(self.all[mid: r])

            l_min, l_pos = self.devide(left, l, mid)
            r_min, r_pos = self.devide(right, mid, r)

            if l_min < r_min:
                return l_min, l_pos
            else:
                return r_min, r_pos
        else:
            if self.all[l] < self.all[l+1]:
                return self.all[l], l
            else:
                return self.all[l+1], l+1
        
            
if __name__ == '__main__':
    demo = [10, 8, 2, 4, 5, 3, 9, 1]
    solution = Solution(demo)
    solution.solve()