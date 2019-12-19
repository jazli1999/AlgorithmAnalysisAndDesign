def p(j):
    for i in range(j, -1, -1):
        if tasks[i][2] <= tasks[j][1]:
            return i

def solve():
    optimals = []
    for i, task in enumerate(tasks):
        if i == 0:
            optimals.append(task[0])
            continue
        j = p(i)  
        op_in = optimals[j] + task[0]
        op_ex = optimals[i-1]
        optimals.append(max(op_in, op_ex))

    return optimals

def find_path(opt):
    j = len(opt) - 1
    while j > 0:
        if tasks[j][0] + opt[p(j)] > opt[j-1]:
            path.append(j) 
            j = p(j)
        else:
            j -= 1

def key(value):
    return value[2]

tasks = [[0, 0, 0], [2, 0, 6], [6, 2, 8], [3.5, 7, 11],
         [7, 3, 16], [8, 12, 17], [1.1, 14, 19]]
# tasks = [[0, 0, 0], [10, 0, 3], [2, 0, 7], [4, 0, 3], [3, 4, 7], [7, 4, 10], [15, 8, 11]]
path = []
# [weight, start time, finish time]
if __name__ == '__main__':
    tasks.sort(key=key)
    opt = solve()
    print(opt)

    find_path(opt)
    print([tasks[i] for i in path])
