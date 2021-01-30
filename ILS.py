import math
from random import randint

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


def calculate_route_length(solution, distances):
    length, i = 0, 0
    for i in range(len(solution) - 1):
        if (solution[i], solution[i + 1]) not in distances:
            length += distances[solution[i + 1], solution[i]]
        else:
            length += distances[solution[i], solution[i + 1]]
    if (solution[0] > solution[i + 1]):
        length += distances[solution[i + 1], solution[0]]
    else:
        length += distances[solution[0], solution[i + 1]]
    return length


def two_opt_swap(solution, i, j):
    return solution[:i+1] + solution[j-1:i:-1] + solution[j:]



def perturbation(solution):
    i = randint(0, len(solution) - 1)
    j = randint(0, len(solution) - 1)
    solution[i], solution[j] = solution[j], solution[i]
    return solution


def two_opt(solution, distances, route_length):
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            new_solution = two_opt_swap(solution, i, j)
            new_route_length = calculate_route_length(new_solution, distances)
            if (new_route_length < route_length):
                solution = new_solution
                route_length = new_route_length
    return solution        


def euclid_cout_distace(vert):
    ids = [key for key in vert.keys()]
    distances = dict()
    for id_1 in ids:
        for id_2 in ids:
            if (id_2, id_1) not in distances and id_1 != id_2:
                distances[id_1, id_2] = math.sqrt((vert[id_1][0] - vert[id_2][0])**2 +
                                                  (vert[id_1][1] - vert[id_2][1])**2)
    return ids, distances


def ILS(ids, distances):
    initial_solution = greedy_algorithm_tsp(ids, distances)
    solution = two_opt(initial_solution,distances,
                       calculate_route_length(initial_solution, distances))
    route_length = calculate_route_length(solution, distances)
    for i in solution:
        tmp_sol = [items for items in solution]
        new_solution = perturbation(tmp_sol)
        new_solution = two_opt(new_solution, distances,
                               calculate_route_length(new_solution, distances))
        new_route_length = calculate_route_length(new_solution, distances)
        if (new_route_length < route_length):
            route_length = new_route_length
            solution = [items for items in new_solution]
    return solution


def convert(num):
    vert = dict()
    for i in range(num):
        temp = input().split(' ')
        vert[int(temp[0])] = [int(temp[1]), int(temp[2])]
    return vert


if __name__ == "__main__":
    vert = convert(int(input()))
    ids, distances = euclid_cout_distace(vert)
    tmp = ILS(ids, distances)
    for i in tmp: print(i, end = " ")