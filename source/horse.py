from copy import deepcopy
from numpy import zeros

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

class Solution:
    def __init__(self, size, start):
        self.size = size
        self.start = start
        self.solution = None
        self.root = Node(start)
        self.choices = [[-1, -2], [-2, -1], [-2, 1], [-1, 2],
                           [1, -2], [2, -1], [2, 1], [1, 2]]

    def solve(self):
        been = zeros((self.size, self.size), dtype=int)
        been[self.start[0]][self.start[1]] = 1

        for choice in self.choices:
            move = [self.root.value[0] + choice[0], self.root.value[1] + choice[1]]
            if -1 < move[0] < self.size and -1 < move[1] < self.size:
                if been[move[0]][move[1]] == 0:
                    # never has been there
                    new_node = Node(move)
                    self.root.children.append(new_node)
        
        self.root.children.sort(key = sort_movements) 

        self.step(self.root, been, [self.start])
        self.print_solution()

    def step(self, node, been, stack):
        if len(node.children) == 0:
            return False
        
        for child in node.children:
            for choice in self.choices:
                move = [child.value[0] + choice[0], child.value[1] + choice[1]]
                if -1 < move[0] < self.size and -1 < move[1] < self.size:
                    if been[move[0]][move[1]] == 0:
                        # never has been there
                        new_node = Node(move)
                        child.children.append(new_node)

        node.children.sort(key = sort_movements) 

        for child in node.children:        
            new_been = deepcopy(been)
            new_stack = deepcopy(stack)

            new_been[child.value[0]][child.value[1]] = 1
            # now the horse has been there
            new_stack.append(child.value)

            if not(0 in new_been):
                self.solution = new_stack
                return True

            if self.step(child, new_been, new_stack):
                return True

        return False
    
    def print_solution(self):
        if self.solution == None:
            print('No proper solution exists')
        else:
            for point in self.solution:
                no = point[0] * self.size + point[1] + 1
                print(no, end=' ')
            print()
        print(len(self.solution))

def sort_movements(node):
    return len(node.children)


if __name__ == '__main__':
    # size, x, y = map(int, input().split(' '))
    size = 8
    x = 3
    y = 4
    solution = Solution(size, [x, y])
    solution.solve()
