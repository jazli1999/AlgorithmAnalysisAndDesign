from copy import deepcopy

class Node():
    def __init__(self, value):
        self.value = value
        self.children = []
        self.eval = None
        self.route = None

class Solution():
    def __init__(self, initial, target):
        self.initial = initial
        self.root = Node(initial)
        self.solution = None
        self.target = target

    def solve(self):
        self.root.route = []
        self.root.eval = self.evaluate(self.root)
        self.seek(self.root)
        self.print_solution()

    def seek(self, node):
        if node.value == self.target:
            self.solution = node.route
            return True

        directions = ['u', 'd', 'l', 'r']
        counter = -1
        for direction in directions:
            next_move = move(deepcopy(node.value), direction)
            if next_move:
                # valid move
                if self.not_orrured(next_move, node.route):
                    # hadn't appear this one
                    counter += 1
                    new_node = Node(next_move)
                    new_node.route = deepcopy(node.route)
                    new_node.route.append(counter)
                    new_node.eval = self.evaluate(new_node)         
                    node.children.append(new_node)
        
        if len(node.children) > 0:
            node.children.sort(key=sort_key)
            mini = node.children[0].eval
            for i, child in enumerate(node.children):
                child.route[-1] = i
                if child.eval == mini:
                    if self.seek(child):
                        return True

    def not_orrured(self, square, route):
        node = self.root
        if square == node.value:
            return False
        else:
            for num in route:
                node = node.children[num]
                if square == node.value:
                    return False
        return True

    def evaluate(self, node):
        count = 0
        current = node.value
        for row_c, row_t in zip(current, self.target):
            for num_c, num_t in zip(row_c, row_t):
                if num_c != num_t: 
                    count += 1
        count += len(node.route)
        return count
    
    def print_solution(self):
        node = self.root
        print_square(node.value)
        for num in self.solution:
            node = node.children[num]
            print_square(node.value)

    
def print_square(square):
    for row in square:
        print(row)
    print()

def sort_key(value):
    return value.eval

def move(square, direction):
    zero = [-1, -1]
    for i, row in enumerate(square):
        for j, num in enumerate(row):
            if num == 0:
                zero = [i, j]
                break
        if zero[0] > -1:
            break

    if direction == 'u':
        if i+1 > 2:
            return False
        else:
            square[i][j] = square[i+1][j]
            square[i+1][j] = 0

    elif direction == 'd':
        if i-1 < 0:
            return False
        else:
            square[i][j] = square[i-1][j]
            square[i-1][j] = 0
    
    elif direction == 'l':
        if j+1 > 2:
            return False
        else:
            square[i][j] = square[i][j+1]
            square[i][j+1] = 0

    else:
        if j-1 < 0:
            return False
        else:
            square[i][j] = square[i][j-1]
            square[i][j-1] = 0 

    return square

if __name__ == '__main__':
    original = [[2, 8, 3],
                [1, 6, 4],
                [7, 0, 5]]
    final = [[1, 2, 3],
             [8, 0, 4],
             [7, 6, 5]]
    solution = Solution(original, final)
    solution.solve()