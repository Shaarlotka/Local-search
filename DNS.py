
def expand_clusters(solution):
    return 0

def combine_clusters(solution):
    return 0

def change_machine_cluster(solution):
    return 0

def change_parts_cluster(solution):
    return 0

def greedy_algorithm():
    return 0

def optimal_solution(solution):
    return 0

def GDNS():
    shaking_structures = [expand_clusters, combine_clusters]
    neighdorhood_structure = [change_machine_cluster, change_parts_cluster]
    final_solution = greedy_algorithm()
    k = 0
    while k != range(len(shaking_structures)):
        solution = shaking_structures[k](final_solution)
        l = 0
        while l != range(len(neighdorhood_structure)):
            new_solution = neighdorhood_structure[l](solution)
            if (optimal_solution(solution) <= optimal_solution(new_solution)):
                solution = new_solution
                l = 1
            else:
                l += 1
        if (optimal_solution(solution) >= optimal_solution(final_solution)):
            final_solution = solution
            k = 1
        else:
            k += 1
    return final_solution


if __name__ == "__main__":
    pass