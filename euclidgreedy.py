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


def swap_2_opt(current_solution, i, k):
    new_solution = list()
    for j in range(i):
        new_solution.append(current_solution[j])
    for j in reversed(range(i, k + 1)):
        new_solution.append(current_solution[j])
    for j in range(k + 1, len(current_solution)):
        new_solution.append(current_solution[j])

    return new_solution


if __name__ == '__main__':
    vertexes = {0: [4, 5], 1: [2, 3], 2: [0, 8]}
    pure_ids, distances = euclid_counts_distance(vertexes)
    print(pure_ids)
    for i in distances.items():
        print(i)
    solution = greedy_algorithm_tsp(pure_ids, distances)
    print(swap_2_opt(solution, 1, 2))
