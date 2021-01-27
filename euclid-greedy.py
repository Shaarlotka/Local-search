import math

def greedy_algorithm_tsp(pure_ids, distances):
    temp = dict(item for item in distances.items())
    temp_list = [pure_ids[i+1] for i in range(len(pure_ids) - 1)]
    solution = list()
    i = pure_ids[0]
    solution.append(i)
    while temp_list:
        print(solution)
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
    for id1 in pure_ids:
        for id2 in pure_ids:
            if not ((id1, id2) in distances or (id2, id1) in distances) and \
                    (id1 != id2):
                distances[id1, id2] = \
                    math.sqrt((vertexes[id1][0] - vertexes[id2][0])**2 +
                              (vertexes[id1][1] - vertexes[id2][1])**2)
    return pure_ids, distances


def opt_2(solution, pure_ids, ):
    return


def guided_local_search(solution, pure_ids, distances):
    return


if __name__ == '__main__':
    vertexes = {0: [4, 5], 1: [2, 3], 2: [0, 8]}
    pure_ids, distances = euclid_counts_distance(vertexes)
    print(pure_ids)
    for i in distances.items():
        print(i)
    print(greedy_algorithm_tsp(pure_ids, distances))
