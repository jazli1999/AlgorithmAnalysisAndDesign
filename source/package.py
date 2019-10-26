from tree import Node


class Solution:
    __slots__ = ('solutions', 'tree', 'capacity', 'items', 'values', 'weights', 'best')

    def __init__(self, capacity, items, init):
        self.solutions = []
        self.tree = Node(init)
        self.capacity = capacity
        self.items = items
        self.values = []
        self.weights = []
        self.best = [[], capacity, 0]

    def solve(self):
        self.construct_tree()
        self.solutions = self.tree.depth_traversal()
        self.calculate_roi()
        self.print_solution()

    def construct_tree(self):
        queue = [self.tree]
        item_list = list(item for i, item in enumerate(self.items))
        for i, item in enumerate(item_list):
            queue_next = []
            for j, parent in enumerate(queue):
                conclude = Node(item)
                exclude = Node(0)
                parent.children.append(conclude)
                queue_next.append(conclude)
                parent.children.append(exclude)
                queue_next.append(exclude)

            queue = queue_next

    def calculate_roi(self):
        for solution in self.solutions:

            while 0 in solution:
                solution.remove(0)

            weight = sum(list(self.items[no][0] for no in solution))
            value = sum(list(self.items[no][1] for no in solution))
            self.weights.append(weight)
            self.values.append(value)

            if (weight <= self.capacity) and (value > self.best[2]):
                self.best[0] = solution
                self.best[1] = weight
                self.best[2] = value

    def print_solution(self):
        counter = 0
        print('\nNo\tSolution\tWeight\tValue')
        for solution, weight, value in zip(self.solutions, self.weights, self.values):
            counter += 1
            print('%d\t%-15s\t%d\t%d' % (counter, solution, weight, value))

        print('\n%s\t%-15s\t%d\t%d' % ('★', self.best[0], self.best[1], self.best[2]))


if __name__ == '__main__':
    given = {1: [7, 42], 2: [3, 12], 3: [4, 40], 4: [5, 25]}
    key = Solution(10, given, 0)
    key.solve()
