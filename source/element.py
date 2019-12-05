from copy import deepcopy

class Solution:
    # find the minimal number and its index
    def __init__(self, nums, kth):
        self.all = nums
        self.process = deepcopy(nums)
        self.map = {}
        self.kth = kth
        self.answer = None
        self.pos = None
    
    def solve(self):
        if self.kth < 1 or self.kth > len(self.process):
            print('Illegal parameter {0}'.format(self.kth))

        else:
            # record original index
            self.update()
            self.answer = self.devide(0, len(self.process)-1, self.kth)
            print('No.{0} Smallest of {1} is {2} at index {3}'.format(self.kth, self.all, self.answer, self.map[self.answer]))

    def devide(self, l, r, k):
        if l >= r:
            return self.process[min(l, r)]

        pivot = self.process[l]
        i = l
        j = r
        while True:
            while self.process[j] > pivot and i < j:
                j -= 1

            if i != j:
                self.process[i] = self.process[j]

            while self.process[i] < pivot and i < j:
                i += 1
            
            if i != j:
                self.process[j] = self.process[i]

            if i == j:
                self.process[i] = pivot

                if j-l+1 == k:
                    return self.process[j]
                elif j-l+1 > k:
                    return self.devide(l, i-1, k)
                else:
                    return self.devide(i+1, r, k+l-i-1)

    def update(self):
        for i, num in enumerate(self.process):
            self.map[num] = i


if __name__ == '__main__':
    demo = [10, 8, 2, 4, 5, 3, 9, 1]
    for k in range(0, 10):
        solution = Solution(demo, k)
        solution.solve()