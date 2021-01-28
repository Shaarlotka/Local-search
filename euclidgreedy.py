import math


def greedy_algorithm_tsp(pure_ids, distances):
    temp = dict(item for item in distances.items())
    temp_list = [pure_ids[i+1] for i in range(len(pure_ids) - 1)]
    solution = list()
    i = pure_ids[0]
    solution.append(i)
    while temp_list:
        min_dist_key = (i, temp_list[0])
        min_dist = max(temp.values())
        temp_for_temp = [key for key in temp.keys()]
        for key in temp_for_temp:
            if i in key:
                if temp[key] < min_dist:
                    min_dist = temp[key]
                    min_dist_key = key
                temp.pop(key)
        j = 0
        while True:
            if min_dist_key[j] != i:
                i = min_dist_key[j]
                break
            j += 1
        temp_list.remove(i)
        solution.append(i)

    return solution


def euclid_counts_distance(vertexes):
    pure_ids = [key for key in vertexes.keys()]
    distances = dict()
    for id_1 in pure_ids:
        for id_2 in pure_ids:
            if not ((id_2, id_1) in distances) and (id_1 != id_2):
                distances[id_1, id_2] = \
                    math.sqrt((vertexes[id_1][0] - vertexes[id_2][0])**2 +
                              (vertexes[id_1][1] - vertexes[id_2][1])**2)
    return pure_ids, distances


def calculate_route(solution, distances):
    sum = 0
    i = 0
    for i in range(len(solution) - 1):
        if not (solution[i], solution[i + 1]) in distances:
            sum += distances[solution[i + 1], solution[i]]
        else:
            sum += distances[solution[i], solution[i + 1]]
    sum += distances[solution[0], solution[i + 1]]
    return sum


def swap_2_opt(current_solution, i, k):
    new_solution = list()
    for j in range(i):
        new_solution.append(current_solution[j])
    for j in reversed(range(i, k + 1)):
        new_solution.append(current_solution[j])
    for j in range(k + 1, len(current_solution)):
        new_solution.append(current_solution[j])

    return new_solution


def two_opt(solution, distances):
    route = calculate_route(solution, distances)
    for i in range(1, len(solution) - 1):
        for j in range(i + 1, len(solution)):
            new_solution = swap_2_opt(solution, i, j)
            new_route = calculate_route(new_solution, distances)
            print("In 2opt", new_solution, new_route)
            if (new_route < route):
                solution = new_solution
                route = new_route
    return solution

