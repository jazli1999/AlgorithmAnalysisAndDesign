from copy import deepcopy

class Node:
    def __init__(self, id, weight, value):
        # item id numbers tracked separately
        self.value = value
        self.weight = weight
        self.id = id
        self.ub = None
        self.left = None
        self.right = None

class Solution:
    def __init__(self, items, capacity):
        self.items = items
        self.solutions = []
        self.capacity = capacity
        self.root = None
        self.best = [0, []]
        self.down = None
        self.up = None

    def solve(self):
        self.update_items()
        self.up = self.capacity * self.items[0][2]
        self.greedy()

        self.root = Node(0, 0, 0)
        self.root.ub = self.up

        self.expand(self.root, [], 0)
        self.print_solutions()

    def expand(self, node, stack, level):
        if node.weight > self.capacity or level >= self.items[-2][0]:
            # overweighted or no left items to be added in 
            self.solutions.append([node.value, stack])

            if self.best[0] == 0 or self.best[0] < node.value:
                self.best = [node.value, stack]

            return

        item = self.items[level + 1]
        # the item to be expanded

        add_weight = node.weight + item[1]
        add_value = node.value + item[2]

        node.left = Node(item[0], add_weight, add_value) 
        node.right = Node(0, node.weight, node.value)
        # Inheritent the last node's weight and value

        node.left.ub = self.ub_calculate(node.left, item[0])
        node.right.ub = self.ub_calculate(node.right, item[0])

        if node.left.weight <= self.capacity and node.left.ub >= self.down:
            # weight below capacity && value bigger than lower boundary 
            new_stack = deepcopy(stack)
            new_stack.append(node.left.id)
            self.expand(node.left, new_stack, level + 1)
        
        if node.right.weight <= self.capacity and node.right.ub >= self.down:
            new_stack = deepcopy(stack)
            self.expand(node.right, new_stack, level + 1)            


    def ub_calculate(self, node, level):
        ub = node.value + (self.capacity - node.weight) * (self.items[level + 1][3])
        return ub

    def update_items(self):
        for item in self.items:
            item.append(item[1] / item[0])
            # [weight, value, per]

        self.items.sort(reverse=True, key = sort_key)
        self.items.insert(0, [0, 0, 0])
        self.items.append([0, 0, 0])

        for i, item in enumerate(self.items):
            item.insert(0, i)
            # [id, weight, value, per]
    
    def greedy(self):
        v = 0
        w = 0
        for item in self.items:
            w += item[1]
            if w > self.capacity:
                self.down = v
                break
            else:
                v += item[2]

    def print_solutions(self):
        counter = 0
        for solution in self.solutions:
            counter += 1
            print('{0}\t{1}\t{2}'.format(counter, solution[1], solution[0]))

        print('\n{0}\t{1}\t{2}'.format('★', self.best[1], self.best[0]))
            
def sort_key(val):
    return val[2]

if __name__ == '__main__':
    items = [[5, 25], [4, 40], [3, 12], [7, 42]]
    solution = Solution(items, 10)
    solution.solve()
