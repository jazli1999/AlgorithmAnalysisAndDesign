from copy import deepcopy

class Solution:
    def __init__(self, jobs):
        self.jobs = jobs
        self.solutions = {}
        self.best = [0, []]
    
    def solve(self):
        self.solutions['es'] = self.earliest_start()
        self.solutions['si'] = self.shortest_interval()
        self.solutions['ef'] = self.earliest_finish()
        self.solutions['fc'] = self.fewewt_conflicts()

        self.print_solutions()


    def greedy(self, tasks):
        end = max(job[2] for job in self.jobs)
        slots = [[0, '-'] for i in range(0, end)]

        for task in tasks:
            needed = [slot[0] for slot in slots[task[1]: task[2]]]
            if 1 not in needed:
                slots[task[1]: task[2]] = [[1, task[0]] for i in range(task[1], task[2])]
        
        return slots

    def earliest_start(self):
        tasks = deepcopy(self.jobs)
        tasks.sort(key=start)
        return self.greedy(tasks)

    def shortest_interval(self):
        tasks = deepcopy(self.jobs)
        for task in tasks:
            task.append(task[2] - task[1])
        tasks.sort(key=extra)

        return self.greedy(tasks)

    def earliest_finish(self):
        tasks = deepcopy(self.jobs)
        tasks.sort(key=finish)
        return self.greedy(tasks)

    def fewewt_conflicts(self):
        tasks = deepcopy(self.jobs)
        counter = 0

        for task in tasks:
            for compared in tasks:
                if task[1] <= compared[1] <= task[2] or compared[1] <= task[1] <= compared[2]:
                    counter += 1
            task.append(counter)
            counter = 0
        
        tasks.sort(key=extra)
        return self.greedy(tasks)

    def print_solutions(self):
        for solution in self.solutions:
            vision = [slot[1] for slot in self.solutions[solution]]
            total = len(set(vision)) - 1
            print('{0}: {1}\t{2}'.format(solution, vision, total))
            if total > self.best[0]:
                self.best[0] = total
                self.best[1] = vision
        
        print('\nProper solution:\n{0}\t{1}'.format(self.best[1], self.best[0]))

def start(job):
    return job[1]

def extra(job):
    return job[3]

def finish(job):
    return job[2]


if __name__ == '__main__':
    demo = [['a', 0, 6], ['b', 1, 4], ['c', 3, 5], ['d', 3, 8], 
            ['e', 4, 7], ['f', 5, 9], ['g', 6, 10], ['h', 8, 11]]
    solution = Solution(demo)
    solution.solve()
