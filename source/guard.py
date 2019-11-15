from copy import deepcopy
from numpy import zeros

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
    
class Solution:
    def __init__(self, m, n):
        self.directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        self.root = Node([0, -1])
        self.m = m
        self.n = n
        self.solutions = []
        self.best = []
        
    def solve(self):
        self.expand(self.root, zeros((self.m, self.n), dtype=int), [])
        self.print_solution()

    def expand(self, node, watched, stack):
        for i in range(0, self.m):
            for j in range(0, self.n):
                if watched[i][j] == 0:
                    # The first unwatched unit in the scan

                    if i < self.m - 1 and j < self.n - 1:
                        if watched[i][j+1] - watched[i+1][j] >= 0:
                            new_node = Node([i+1, j])
                            node.children.append(new_node)
                        
                        if watched[i+1][j] - watched[i][j+1] >= 0:
                            new_node = Node([i, j+1])
                            node.children.append(new_node)
                            
                    elif i == self.m - 1 and j < self.n - 1:
                        if watched[i][j+1] == 1:
                            new_node = Node([i, j])
                        else:
                            new_node = Node([i, j+1])
                        node.children.append(new_node)

                    elif i < self.m - 1 and j == self.n - 1:
                        if watched[i+1][j] == 1:
                            new_node = Node([i, j])
                        else:
                            new_node = Node([i+1, j])
                        node.children.append(new_node)
                    
                    else:
                        new_node = Node([i, j])
                        node.children.append(new_node)

                    for child in node.children:
                        new_stack = deepcopy(stack)
                        new_stack.append(child.value)

                        new_watched = deepcopy(watched)
                        new_watched[child.value[0]][child.value[1]] = 1
                        for direction in self.directions:
                            x = child.value[0] + direction[0]
                            y = child.value[1] + direction[1]
                            if -1 < x < self.m and -1 < y < self.n:
                                new_watched[x][y] = 1 

                        self.expand(child, new_watched, new_stack)
                    return
                
                else:
                    if i == self.m - 1 and j == self.n - 1:
                        self.solutions.append(stack)

                        if len(self.best) == 0 or len(stack) == len(self.best[0]):
                            self.best.append(stack)
                        
                        elif len(stack) > len(self.best[0]):
                            self.best = [stack]
                
                        return          

    
    def print_solution(self):
        counter = 0
        for solution in self.best:
            counter += 1
            print('\nNo. {0} Guards needed: {1}'.format(counter, len(solution)))
            guards = zeros((self.m, self.n), dtype=int)
            for point in solution:
                guards[point[0]][point[1]] = 1
        
            print(guards)

                                          
if __name__ == '__main__':
    m, n = map(int, input().split(' '))
    solution = Solution(m, n)
    solution.solve()
