import copy

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


class Solution:
    def __init__(self, maze, begin, over):
        self.choices = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        self.solutions = []
        self.maze = maze
        self.over = over
        self.begin = begin
        self.root = Node(begin)
        self.best = []
    
    def solve(self):
        new_maze = copy.deepcopy(self.maze)
        new_maze[self.begin[0]][self.begin[1]] = 0
        self.seek(self.root, [self.begin], new_maze)
        # self.print_solutions()
        print(self.best)


    def seek(self, node, stack, maze):                    # The same effect as Stack.top()
        if node.value == self.over:
            self.solutions.append(stack)
            if len(self.best) == 0:
                self.best = stack
            else:
                if len(self.best) > len(stack):
                    self.best = stack
            return

        for choice in self.choices:
            new_pos = [node.value[0] + choice[0], node.value[1] + choice[1]]

            if maze[new_pos[0]][new_pos[1]] == 1:
                new_node = Node(new_pos)
                node.children.append(new_node)

                new_maze = copy.deepcopy(maze)
                new_stack = copy.deepcopy(stack)

                new_maze[new_pos[0]][new_pos[1]] = 0
                new_stack.append(new_pos)

                self.seek(new_node, new_stack, new_maze)

    def print_solutions(self):
        for solution in self.solutions:
            print(solution)


if __name__ == '__main__':
    cur_maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 0, 1, 1, 1, 0, 1, 0],
                [0, 1, 1, 0, 1, 1, 1, 0, 1, 0],
                [0, 1, 1, 1, 1, 0, 0, 1, 1, 0],
                [0, 1, 0, 0, 0, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                [0, 1, 0, 1, 1, 1, 0, 1, 1, 0],
                [0, 1, 0, 0, 0, 1, 0, 0, 1 ,0],
                [0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    cur_begin = [1, 1]
    cur_over = [8, 8]
    solution = Solution(cur_maze, cur_begin, cur_over)

    solution.solve()