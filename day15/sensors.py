def pos_diff(a, b):
    return [a[0]-b[0], a[1]-b[1]]

def manhattan_distance(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

# Returns:
# 1: if pos is covered
# 2: distance to right edge
def is_covered(sensors, distances, pos):
    sensor_num = len(distances)
    for i in range(sensor_num):
        manhattan = manhattan_distance(sensors[i], pos)
        if manhattan <= distances[i]:
            diff = pos_diff(sensors[i], pos)

            return (True, diff[0] + (distances[i]-abs(diff[1])))
    return (False, 0)
    

if __name__ == '__main__':
    lines = []
    with open('./input', 'r') as f:
        lines = f.readlines()

    # each index in the sensor list corresponds to a beacon
    sensor_coords = []
    beacon_coords = []
    distances = []
    for line in lines:
        # split and clean
        split_line = line.translate({ord(i): None for i in 'xy=,:\n'}).split(' ')
        
        sensor_coord = [int(split_line[2]), int(split_line[3])]
        beacon_coord = [int(split_line[8]), int(split_line[9])]

        sensor_coords.append(sensor_coord)
        beacon_coords.append(beacon_coord)
        distance = manhattan_distance(sensor_coord, beacon_coord)
        distances.append(distance)
    sensor_num = len(sensor_coords)

    extreme_coords = [10**10, -10**10] # something really big
    # find the extreme x coordinates of what area are covered
    for i in range(len(sensor_coords)):
        manhattan = manhattan_distance(sensor_coords[i], beacon_coords[i])
        if extreme_coords[0] > sensor_coords[i][0] - manhattan:
            extreme_coords[0] = sensor_coords[i][0] - manhattan
        if extreme_coords[1] < sensor_coords[i][0] + manhattan:
            extreme_coords[1] = sensor_coords[i][0] + manhattan

    sum_p1 = 0
    y = 2_000_000
    x = extreme_coords[0]
    while x < extreme_coords[1]:
        covered, distance_to_right = is_covered(sensor_coords, distances, [x,y])
        if covered:
            sum_p1 += distance_to_right+1
            x += distance_to_right+1
        else:
            x += 1
    for x in range(extreme_coords[0], extreme_coords[1]):
        if [x,y] in beacon_coords:
            sum_p1 -= 1
    print('Part 1:',sum_p1)

    start = 0
    end = 4_000_000
    found_pos = []
    stop = False
    for y in range(start, end):
        # This took me a while, so this should remove some suffering
        if y%100_000 == 0: 
            print('y:',y)
        x = start
        while x < end:
            covered, distance_to_right = is_covered(sensor_coords, distances, [x,y])
            if covered:
                x += distance_to_right+1
            else:
                found_pos = [x,y]
                stop = True
                break
        if stop:
            break

    print('Part 2:',found_pos[0]*4_000_000 + found_pos[1])
