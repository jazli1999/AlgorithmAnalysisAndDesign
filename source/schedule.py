from copy import deepcopy

class Solution:
    def __init__(self, jobs):
        self.jobs = jobs
        self.solutions = []
        self.best = [0, []]
    
    def solve(self):
        print('Lectures in order of START TIME:')
        self.earliest_start()
        self.print_solutions()

        print('Lectures in order of Finish Time:')
        self.earliest_finish()
        self.print_solutions()

        print('Lectures in order of Interval:')
        self.shortest_interval()
        self.print_solutions()

        print('Lectures in order of Fewest Conflicts:')
        self.fewest_conflicts()
        self.print_solutions()


    def greedy(self, tasks):
        end = max(job[2] for job in self.jobs)
        room = [[0, '-'] for i in range(0, end)]
        rooms = [deepcopy(room)]

        for task in tasks:
            scheduled = False
            for slots in rooms:
                needed = [slot[0] for slot in slots[task[1]: task[2]]]
                if 1 not in needed:
                    slots[task[1]: task[2]] = [[1, task[0]] for i in range(task[1], task[2])]
                    scheduled = True
                    break
            if not scheduled:
               slots = deepcopy(room)
               slots[task[1]: task[2]] = [[1, task[0]] for i in range(task[1], task[2])]
               rooms.append(slots)

        self.solutions = rooms

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

    def fewest_conflicts(self):
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
            vision = [slot[1] for slot in solution]
            total = len(set(vision)) - 1
            print(vision)

def start(job):
    return job[1]

def extra(job):
    return job[3]

def finish(job):
    return job[2]


if __name__ == '__main__':
    demo = [['a', 0, 3], ['b', 0, 7], ['c', 0, 3], ['d', 4, 7], 
            ['e', 4, 10], ['f', 8, 11], ['g', 8, 11], ['h', 10, 15], ['j', 12, 15]]
    solution = Solution(demo)
    solution.solve()
