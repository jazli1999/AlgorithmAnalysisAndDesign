import math
from tree import Node


class Solution:

    __slots__ = ('points', 'solutions', 'tree', 'weights', 'best', 'mat')

    def __init__(self, points, mat, init):
        self.points = points
        self.solutions = []
        self.tree = Node(init)
        self.best = [[], math.inf]
        self.weights = []
        self.mat = mat

    def construct_tree(self):
        left = list(self.points)
        expand_child(self.tree, left)

    def solve(self):
        self.construct_tree()
        self.solutions = self.tree.depth_traversal()
        self.calculate_weight()
        self.print_solution()

    def print_solution(self):
        counter = 0
        for solution, weight in zip(self.solutions, self.weights):
            counter += 1
            print('{0}\t{1}\t{2}'.format(counter, solution, weight))

        print('\n{0}\t{1}\t{2}'.format('★', self.best[0], self.best[1]))

    def calculate_weight(self):
        for solution in self.solutions:
            weight = 0
            solution.pop(0)
            for i in range(0, len(self.mat) - 1):
                weight += self.mat[solution[i]][solution[i + 1]]

            weight += self.mat[solution[-1]][0]
            self.weights.append(weight)

            if weight < self.best[1]:
                self.best[0] = solution
                self.best[1] = weight


def expand_child(root, left):
    if len(left) > 0:
        for point in left:
            cur = Node(point)
            root.children.append(cur)
            new_left = list(left)
            new_left.remove(point)

            expand_child(cur, new_left)
    else:
        return


if __name__ == '__main__':
    cities = [0, 1, 2, 3]
    matrix = [[math.inf, 3, 6, 7],
           [12, math.inf, 2, 8],
           [8, 6, math.inf, 2],
           [3, 7, 6, math.inf]]

    key = Solution(cities, matrix, '#')
    key.solve()
