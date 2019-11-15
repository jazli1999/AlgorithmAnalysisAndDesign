class Node:
    def __init__(self):
        self.value = None
        self.children = []

class Tree:
    def __init__(self):
        self.root = None
        self.connect = None
        self.cities = None
        self.best = 1
        self.prove  = None
        self.solutions = []  

    def solve(self):
        node = Node()
        node.value = [0, []]
        self.root = node
        self.expand(node, node.value[1], 1, 1)
        self.print_solutions()

    def expand(self, node, pre_colors, cur_color, level):
        # int for cur_color
        cur_colors = list(pre_colors)
        cur_colors.append(cur_color)
        node.value = [cur_color, cur_colors]

        if self.it_works(pre_colors, level, cur_color):
            # no same color on adjacent cities
            self.best = max(cur_colors)
            if level < len(self.cities):
                for i in range(1, self.best + 2):
                    # a new color choice will be tested in the end
                    # in case that the current increase could result
                    # in a latter success
                    new_node = Node()
                    node.children.append(new_node)
                    if self.expand(new_node, node.value[1], i, level + 1):
                        return True
            else:
                cur_solution = list([max(cur_colors), list(node.value[1])])
                self.solutions.append(cur_solution)
                if self.prove == None:
                    self.prove = cur_solution
                else:
                    if cur_solution[0] < self.prove[0]:
                        self.prove = cur_solution
        else:
            return False

    def it_works(self, pre_colors, level, cur_color):
        for i, pre in enumerate(self.connect[level-1]):
            if i >= level - 1:
                break
            if pre == 1 and cur_color == pre_colors[i]:
                return False
        return True

    def print_solutions(self):
        counter = 0
        print('\nNo\tSolution\tTotal')
        for solution in self.solutions:
            counter += 1
            print('%d\t%-15s\t%d' % (counter, solution[1], solution[0]))

        print('\n%s\t%-15s\t%d' % ('★', self.prove[1], self.prove[0]))


if __name__ == '__main__':
    connect = [[0, 1, 1, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 1, 0, 0, 1],
            [0, 1, 0, 0, 1],
            [0, 1, 1, 1, 0]]
    cities = ['A', 'B', 'C', 'D', 'E']

    tree = Tree()
    tree.cities = cities
    tree.connect = connect
    tree.solve()