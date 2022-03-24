# A Greedy algorithm makes greedy choices at each step to ensure that the objective function is optimized. The Greedy
# algorithm has only one shot to compute the optimal solution so that it never goes back and reverses the decision.
# cam I proof for spaceship problem that it cant solved by greedy algo ?

# Examples for problem


# 1. minimum whiting time - n-log-n

def minimumWaitingTime(queries):
    queries.sort()
    time = 0
    for i in range(1, len(queries)):
        time += queries[i - 1]
        queries[i] = queries[i] + queries[i - 1]
    return time


# 2. task assigment min waiting time
def taskAssignment(tasks):
    res = []
    temp = [[i, num] for i, num in enumerate(tasks)]
    n = len(temp)
    temp.sort(key=lambda x: x[1])

    for i in range(n // 2):
        res.append([temp[i][0], temp[n - i - 1][0]])
    return res


# input - [] distances, [] fuel in each city, MPG mail per gallon... the array of the cities is circular...
# output which city should we start ..
# explain - wll search the city that if we start at  any point wll have the min amount of fuel and we should start
# in that city ...
def validStartingCity(distances, fuel, mpg):
    miles_left = 0
    min_miles = 0
    min_city = 0

    for i in range(1, len(distances)):
        miles_left += mpg * fuel[i - 1]
        miles_left -= distances[i - 1]
        if miles_left < min_miles:
            min_miles = miles_left
            min_city = i

    return min_city
