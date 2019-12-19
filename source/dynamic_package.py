from numpy import zeros
def find_path(m, items):
    path = []
    i = len(m) - 1
    j = len(m[0]) - 1
    
    while m[i][j] > 0:
        if m[i][j] > m[i-1][j]:
            path.append(i)
        else: 
            j -= items[i][0]
        i -= 1

    return path

def table(items, capacity):
    v = zeros([len(items)+1, capacity+1])
    items.insert(0, [0, 0])

    for i, row in enumerate(v):
        for j, unit in enumerate(row):
            if i == 0 or j == 0:
                continue
            item = items[i]

            if j >= item[0]:
                op_in = v[i-1][j-item[0]] + item[1]
                v[i][j] = max(v[i-1][j], op_in)
            else:
                v[i][j] = v[i-1][j]
    return v

def print_solution(solution, items):
    print('Solution:')
    print('Item Numbers: {0}'.format(solution))
    print('Total Weight: {0}'.format(sum(items[i][0] for i in solution)))
    print('Total Value: {0}'.format(sum(items[i][1] for i in solution)))


if __name__ == '__main__':
    demo = [[2, 6], [2, 3], [6, 5], [5, 4], [4, 6]]
    v_d = table(demo, 10)
    print('Value Table:\n{0}'.format(v_d))
    solution = find_path(v_d, demo)
    print_solution(solution, demo)
