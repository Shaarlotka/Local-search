import euclidgreedy as egg
import tkinter


def indicator(current_solution, feature):
    if 0 in feature and feature[1] in current_solution:
        if current_solution.index(feature[1]) in (1, len(current_solution) - 1):
            return 1
    elif feature[0] in current_solution and feature[1] in current_solution:
       if abs(current_solution.index(feature[0]) - \
               current_solution.index(feature[1])) == 1:
            return 1
    return 0


def guided_local_search(best_solution, pure_ids, distances):
    features = [key for key in distances.keys()]
    penalties = dict()
    for key in distances.keys():
        penalties[key] = 0
    new_cost = dict(item for item in distances.items())
    route = egg.calculate_route(best_solution, distances)
    print("route", route)

    while True:
        new_solution = egg.two_opt(best_solution, new_cost)
        utilities = list()
        num_of_features = 0
        for edge in features:
            util_i = indicator(new_solution, edge) * new_cost[edge] / \
                     (1 + penalties[edge])
            if utilities and util_i > max(utilities):
                num_of_features = 1
            elif utilities and util_i == max(utilities):
                num_of_features += 1
            utilities.append(util_i)
        util_max = max(utilities)
        print(util_max, new_solution)
        print(egg.calculate_route(new_solution, distances))
        shift = 0
        while util_max in utilities:
            current_index = utilities.index(util_max) + shift
            print("Rise cost for", current_index)
            print("feature", features[current_index])
            penalties[features[current_index]] += 1
            print("penalty", penalties[features[current_index]])
            shift += 1
            utilities.remove(util_max)
        for i in new_cost.keys():
            new_cost[i] += indicator(new_solution, i) * egg.calculate_route(new_solution, distances) \
                           / num_of_features * penalties[i]
        if (egg.calculate_route(new_solution, distances) < route):
            best_solution = new_solution
            route = egg.calculate_route(new_solution, distances)

    return new_solution


if __name__ == '__main__':
    #vertexes = {0: [4, 5], 1: [2, 3], 2: [0, 8]}
    vertexes = {0: [2, 5], 1: [23, 3], 2: [3, 8], 3: [4, 15], 4: [35, 13], 5: [23, 54], 6: [54, 6], 7: [5, 8]}
    pure_ids, distances = egg.euclid_counts_distance(vertexes)
    print(pure_ids)
    for i in distances.items():
        print(i)
    solution = egg.greedy_algorithm_tsp(pure_ids, distances)
    print(egg.swap_2_opt(solution, 1, 2))
    print(egg.calculate_route([0, 2, 7, 3, 5, 6, 4, 1], distances))
    #twindow = tkinter.Tk()
    #canvas = tkinter.Canvas(twindow,width=600,height=600,bg="gray",
    #          cursor="pencil")
    #canvas.pack()
    #sol = [[2, 5], [23, 3], [3, 8], [4, 15], [35, 13], [23,54], [54,6], [5,8]]
    #canvas.create_polygon(sol, fill="gray", outline="yellow")
    #twindow.mainloop()
    guided_local_search(solution, pure_ids, distances)