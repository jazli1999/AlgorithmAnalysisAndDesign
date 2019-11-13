import copy

class Node:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
        self.capacity = None
        self.items = []
        self.solutions = []
        self.best = None

    def solve(self):
        node = Node()
        node.value = [0, 0, []]
        self.seek(node.value, node, 0, 0)
        self.print_solutions() 

    def seek(self, pre_value, node, item, level):
        cur_value = [pre_value[0], pre_value[1], list(pre_value[2])]
        cur_value[0] += self.items[item][1]                  # weight
        cur_value[1] += self.items[item][2]                  # value

        if item > 0:
            cur_value[2].append(self.items[item][0])         # item_id 

        node.value = cur_value

        if cur_value[0] > self.capacity:
            return
        
        else:
            if level < len(self.items) - 1:
                # if still some item remains
                node.left = Node()
                self.seek(node.value, node.left, level + 1, level + 1)
            
                node.right = Node()
                self.seek(node.value, node.right, 0, level + 1)
            
            else:
                # all traversaled
                self.solutions.append(node.value)
                if self.best == None:
                    self.best = node.value
                else:
                    if self.best[1] < node.value[1]:
                        self.best = node.value

    def print_solutions(self):
        counter = 0
        print('\nNo\tSolution\tWeight\tValue')
        for solution in self.solutions:
            counter += 1
            print('%d\t%-15s\t%d\t%d' % (counter, solution[2], solution[0], solution[1]))

        print('\n%s\t%-15s\t%d\t%d' % ('★', self.best[2], self.best[0], self.best[1]))


if __name__ == '__main__':          
    items = [[0, 0, 0], [1, 20, 20], [2, 15, 30], [3, 10, 25]]
    # [item_id, weight, value]

    tree = Tree()
    tree.items = items
    tree.capacity = 25
    tree.solve()
