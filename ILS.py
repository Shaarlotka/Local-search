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
    solution.append(pure_ids[0])
    return solution

def calculate_route(solution, distances):
    print(solution)
    sum = 0
    for i in range(len(solution) - 1):
        if not (solution[i], solution[i + 1]) in distances:
            sum += distances[solution[i + 1], solution[i]]
        else:
            sum += distances[solution[i], solution[i + 1]]
    print(sum)
    return sum

def swap_2_opt(current_solution, i, k):
    new_solution = list()
    new_solution.append(current_solution[:i])
    for j in reversed(range(i, k + 1)):
        new_solution.append(current_solution[j])
    new_solution.append(current_solution[k + 1:])
    return new_solution

def two_opt_swap(solution, i, j):
    solution[i], solution[j] = solution[j], solution[i]
    return solution

def two_opt(solution, distances):
    route = calculate_route(solution, distances)
    for i in range(1, len(solution) - 2):
        for j in range(i + 1, len(solution) - 1):
            new_solution = two_opt_swap(solution, i, j)
            new_route = calculate_route(new_solution, distances)
            if (new_route < route):
                solution = new_solution
                route = new_route
    return solution            


def euclid_cout_distace(vert):
    ids = [key for key in vert.keys()]
    distances = dict()
    for id_1 in ids:
        for id_2 in ids:
            if not (id_2, id_1) in distances and id_1 != id_2:
                distances[id_1, id_2] = math.sqrt((vert[id_1][0] - vert[id_2][0])**2 +
                                                  (vert[id_1][1] - vert[id_2][1])**2)
    return ids, distances


if __name__ == "__main__":
    vert = {0: [2, 5], 1: [23, 3], 2: [3, 8], 3: [4, 15], 4: [35, 13], 5: [23,54], 6: [54,6], 7: [5,8]}
    ids, distances = euclid_cout_distace(vert)
    solution = greedy_algorithm_tsp(ids, distances)
    new_solution = two_opt(solution, distances)