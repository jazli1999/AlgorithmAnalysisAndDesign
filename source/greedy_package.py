class Solution:
    def __init__(self, items, capacity):
        self.items = items
        self.capacity = capacity
        self.solution = [[], capacity, 0]   # itemlist, weight, value

    def solve(self):
        self.update_items()
        remain = self.capacity

        for item in self.items:
            # [id, weight, value, per]
            if item[1] <= remain:
                self.solution[0].append(item[0])
                self.solution[1] += item[1]
                self.solution[2] += item[2]
                
                remain -= item[1]
            else:
                self.print_solution()
                return

    def print_solution(self):
        print('Items: {0}\n\nTotal Weight: {1}\n\nTotal Value: {2}\n\n'
                .format(self.solution[0], self.solution[1], self.solution[2]))

    def update_items(self):
        for item in self.items:
            item.append(item[1] / item[0])
            # [weight, value, per]

        for i, item in enumerate(self.items):
            item.insert(0, i)
            # [id, weight, value, per]

        self.items.sort(reverse=True, key = sort_key)

def sort_key(item):
    return item[3]

if __name__ == '__main__':
    demo = [[20, 60], [30, 120], [10, 50]]
    solution = Solution(demo, 50)
    solution.solve()