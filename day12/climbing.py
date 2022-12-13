
def fix_value(value):
    if value == 'S': 
        return 'a'
    if value == 'E': 
        return 'z'
    return value

def get_neighbors(node, data):
    neighbors = []

    width = len(data)
    height = len(data[0])

    if node[0]-1 >= 0:
        neighbors.append([node[0]-1, node[1]])
    if node[0]+1 < width:
        neighbors.append([node[0]+1, node[1]])
    if node[1]-1 >= 0:
        neighbors.append([node[0],   node[1]-1])
    if node[1]+1 < height:
        neighbors.append([node[0],   node[1]+1])

    return neighbors
    
def get_good_neighbors(node, data):
    neighbors = []

    width = len(data)
    height = len(data[0])

    curr_data = data[node[0]][node[1]]

    if node[0]-1 >= 0 and not (data[node[0]-1][node[1]] - curr_data >= 2):
        neighbors.append([node[0]-1, node[1]])
    if node[0]+1 < width and not (data[node[0]+1][node[1]] - curr_data >= 2):
        neighbors.append([node[0]+1, node[1]])
    if node[1]-1 >= 0 and not (data[node[0]][node[1]-1] - curr_data >= 2):
        neighbors.append([node[0], node[1]-1])
    if node[1]+1 < height and not (data[node[0]][node[1]+1] - curr_data >= 2):
        neighbors.append([node[0], node[1]+1])

    return neighbors

if __name__ == '__main__':
    elevation_data_string = [] 
    with open('./input', 'r') as f:
        elevation_data_string = [x.strip() for x in f.readlines()]


    width = len(elevation_data_string[0])
    height = len(elevation_data_string)

    start = [0,0]
    end = [0,0]

    visited_nodes = []
    tentative_distances = []
    elevation_data = []

    # Process data
    for x in range(width):
        visited_temp = []
        distance_temp = []
        elevation_temp = []
        for y in range(height):

            if elevation_data_string[y][x] == 'S':
                start = [x, y]
                visited_temp.append(1) # we have visited the start
                distance_temp.append(0) # start has a distance of 0

            elif elevation_data_string[y][x] == 'E':
                end   = [x, y]
                visited_temp.append(0) # all other nodes are unvisited
                distance_temp.append(10**10) # something REALLY BIG

            else:
                visited_temp.append(0) # all other nodes are unvisited
                distance_temp.append(10**10) # something REALLY BIG

            elevation_temp.append(ord(fix_value(elevation_data_string[y][x])) - ord('a'))

        visited_nodes.append(visited_temp)
        tentative_distances.append(distance_temp) # something REALLY BIG
        elevation_data.append(elevation_temp)
                

    # PART 1
    # ------

    path_found = False

    open_nodes = get_good_neighbors(start, elevation_data)

    while not path_found:
        num_open_nodes = len(open_nodes)
        for i in range(num_open_nodes):
            curr = open_nodes[0]
            curr_data = elevation_data[curr[0]][curr[1]]
            
            shortest_neighboring_distance = 10**10

            neighbors = get_neighbors(curr, elevation_data)

            for neighbor in neighbors:
                #neighbor_data = fix_value(elevation_data[neighbor[1]][neighbor[0]])
                neighbor_data = elevation_data[neighbor[0]][neighbor[1]]
                if visited_nodes[neighbor[0]][neighbor[1]]: 
                    if not curr_data - neighbor_data  >= 2:
                        shortest_neighboring_distance = min(tentative_distances[neighbor[0]][neighbor[1]], shortest_neighboring_distance)
                elif not neighbor_data - curr_data >= 2:
                    if not neighbor in open_nodes:
                        open_nodes.append(neighbor)
                    
            
            tentative_distances[curr[0]][curr[1]] = shortest_neighboring_distance + 1
            #print(curr, tentative_distances[curr[0]][curr[1]])

            visited_nodes[curr[0]][curr[1]] = 1

            # ADD NEW OPEN NODES

            open_nodes.pop(0)
            
        if visited_nodes[end[0]][end[1]] == 1:
            path_found = True


    print('Part 1:',tentative_distances[end[0]][end[1]])        

    # PART 2
    # ------

    # LOOP

    starting_nodes = []
    for x in range(width):
        for y in range(height):
            if elevation_data[x][y] == 0:
                starting_nodes.append([x,y])

    best_start_path = 10**10

    for start_node in starting_nodes:
        end = [0,0]

        # RESET ALL DATA
        visited_nodes = []
        tentative_distances = []

        for x in range(width):
            visited_temp = []
            distance_temp = []
            for y in range(height):

                if elevation_data_string[y][x] == 'E':
                    end   = [x, y]
                    visited_temp.append(0) # all other nodes are unvisited

                if [x,y] == start_node:
                    distance_temp.append(0) # start has a distance of 0
                    visited_temp.append(1) # we have visited the start
                else:
                    distance_temp.append(10**10) # something REALLY BIG
                    visited_temp.append(0) # all other nodes are unvisited

            visited_nodes.append(visited_temp)
            tentative_distances.append(distance_temp) # something REALLY BIG

        path_found = False
        open_nodes = get_good_neighbors(start_node, elevation_data)

        # Check so no start open node jumps a wall
        '''
        for open_node in open_nodes:
            open_data = fix_value(elevation_data[open_node[1]][open_node[0]])
            start_data = fix_value(elevation_data[start_node[1]][start_node[0]])
            if ord(open_data) - ord(start_data) >= 2:
                open_nodes.remove(open_node)
        '''

        while not path_found:
            num_open_nodes = len(open_nodes)
            for i in range(num_open_nodes):
                curr = open_nodes[0]

                curr_data = elevation_data[curr[0]][curr[1]]
                
                shortest_neighboring_distance = 10**10

                neighbors = get_neighbors(curr, elevation_data)

                for neighbor in neighbors:
                    neighbor_data = elevation_data[neighbor[0]][neighbor[1]]
                    if visited_nodes[neighbor[0]][neighbor[1]]: # CHECK FOR ELEVATION diff
                        if not curr_data - neighbor_data  >= 2:
                            shortest_neighboring_distance = min(tentative_distances[neighbor[0]][neighbor[1]], shortest_neighboring_distance)
                    elif not neighbor_data - curr_data >= 2:
                        if not neighbor in open_nodes:
                            open_nodes.append(neighbor)
                        
                
                tentative_distances[curr[0]][curr[1]] = shortest_neighboring_distance + 1
                
                visited_nodes[curr[0]][curr[1]] = 1

                # ADD NEW OPEN NODES

                open_nodes.pop(0)
                
            if visited_nodes[end[0]][end[1]] == 1:
                path_found = True
            if len(open_nodes) == 0:
                path_found = True

        best_start_path = min(tentative_distances[end[0]][end[1]], best_start_path)

    print('Part 2:',best_start_path)

