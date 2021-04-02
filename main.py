
def uniform_cost_search(goal, start):
    global graph, cost
    answer = []
    queue = []  # create a priority queue

    for i in range(len(goal)): # set the answer vector to max value
        answer.append(2 ** 7 )
    queue.append([0, start])
    # insert the starting index
    # map to store visited node
    visited = {}
    count = 0

    while (len(queue) > 0):   # while the queue is not empty

        queue = sorted(queue)
        p = queue[-1]
        del queue[-1]
        p[0] *= -1  # get the original value

        if (p[1] in goal):  # check if the element is part of the goal list

            index = goal.index(p[1])

            if (answer[index] == 2 ** 7):
                count += 1

            if (answer[index] > p[0]):
                answer[index] = p[0]
            del queue[-1]

            queue = sorted(queue)
            if (count == len(goal)):
                return answer
        if (p[1] not in visited):
            for i in range(len(graph[p[1]])):
                queue.append([(p[0] + cost[(p[1], graph[p[1]][i])]) * -1, graph[p[1]][i]])
        print(p[1])
        visited[p[1]] = 1
    return answer



graph, cost = [[] for i in range(6)], {}

graph[1].append(2)
graph[1].append(3)
graph[2].append(4)
graph[2].append(5)
graph[3].append(6)
graph[3].append(7)

 # add the cost
cost[(1, 2)] = 3
cost[(1, 3)] = 2
cost[(2, 4)] = 4
cost[(2, 5)] = 1
cost[(3, 6)] = 6
cost[(3, 7)] = 2

goal = []
goal.append(7)

# get the answer
print("\n\t\tUniform Search Cost\n")

print("The visited nodes are :")
answer = uniform_cost_search(goal, 1)
print("\nMinimum cost from node 1 to 7 is = ", answer[0])

