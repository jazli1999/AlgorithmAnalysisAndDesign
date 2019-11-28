from copy import deepcopy
from math import inf, ceil

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.lb = None

class Solution:
    def __init__(self, cost):
        self.cost = cost
        self.solutions = []
        self.best = [inf, []]
        self.root = None
        self.down = None
        self.up = None

    def solve(self):
        self.greedy()
        self.root = Node([0])
        self.root.lb = self.down
        self.expand(self.root)
        print(self.best[0])
        for best in self.best[1]:
            print(best)
    
    def expand(self, node):
        remain = [i for i in range(0, len(self.cost)) if i not in node.value]

        if len(remain) == 0:
            self.solutions.append(node.value)
            if node.lb < self.best[0]:
                self.best = [node.lb, [node.value]]
            elif node.lb == self.best[0]:
                self.best[1].append(node.value)
            return

        for city in remain:
            new_list = list(node.value)
            new_list.append(city)
            new_node = Node(new_list)
            node.children.append(new_node)
            new_node.lb = self.calculate_lb(new_list)

            if self.down <= new_node.lb <= self.up:
                self.expand(new_node)

    def greedy(self):
        # lower boundary
        total = 0.0
        for row in self.cost:
            new_row = list(row)
            total += min(new_row)
            new_row.remove(min(new_row))
            total += min(new_row)
            new_row.remove(min(new_row))

        self.down = ceil(total / 2)

        # upper boundary
        total = 0
        cities = [True for i in range(0, len(self.cost))]
        last_one = 0
        cities[0] = False

        while True in cities:
            next_one = None
            remain = [i for i in range(0, len(self.cost)) if cities[i]]
            for i in remain:
                if next_one == None:
                    next_one = i
                elif self.cost[last_one][next_one] > self.cost[last_one][i]:
                    next_one = i
                
            # add to total cost; move to the next one; mark next one
            total += self.cost[last_one][next_one]
            last_one = next_one
            cities[last_one] = False

        # go back to the initial city
        total += self.cost[last_one][0]
        self.up = total     

    def calculate_lb(self, past):
        total = 0.0
        remain = [i for i in range(0, len(self.cost)) if i not in past]
        for i in range(len(past) - 1):
            total += (2 * self.cost[past[i]][past[i+1]])
        
        total += min([self.cost[past[0]][j] for j in range(len(self.cost)) if j != past[1]])
        total += min([self.cost[past[-1]][j] for j in range(len(self.cost)) if j != past[-2]])

        for i in remain:
            new_row = list(self.cost[i])
            total += min(new_row)
            new_row.remove(min(new_row))
            total += min(new_row)
            new_row.remove(min(new_row)) 
        
        return ceil(total / 2)

if __name__ == '__main__':
    cost = [[inf, 3, 1, 5, 8],
            [3, inf, 6, 7, 9],
            [1, 6, inf, 4, 2],
            [5, 7, 4, inf, 3],
            [8, 9, 2, 3, inf]]

    solution = Solution(cost)
    solution.solve()

    