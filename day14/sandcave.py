
def print_data(data, start_x, start_y, end_x, end_y):
    for y in range(start_y, end_y):
        for x in range(start_x, end_x):
            if x == 500 and y == 0:
                print('x', end='') 
            elif data[x][y] == 0:
                print('.', end='') 
            elif data[x][y] == 1:
                print('#', end='') 
            elif data[x][y] == 2:
                print('o', end='') 
        print()
    print()

def write_line(data, start_coord, end_coord):
    x_range = sorted([start_coord[0], end_coord[0]])
    y_range = sorted([start_coord[1], end_coord[1]])
    
    for x in range(x_range[0], x_range[1]+1):
        data[x][start_coord[1]] = 1
    for y in range(y_range[0], y_range[1]+1):
        data[start_coord[0]][y] = 1

def process_data(file_path):
    cave_file_data = []
    with open(file_path, 'r') as f:
        cave_file_data = [line.strip() for line in f.readlines()]

    # in cave data 0 is air, 1 is rock and 2 is sand
    # The arrys is 1000x200
    cave_data = [[0 for _ in range(200)] for _ in range(1000)] 
    #print(cave_data)

    # process data
    for line in cave_file_data:
        cave_data_coords_strings = [coords.split(',') for coords in line.split('->')]
        cave_data_coords = [[int(coords[0]), int(coords[1])] for coords in cave_data_coords_strings]

        line_count = len(cave_data_coords)
        cur_coord = cave_data_coords[0]
        for i in range(1,line_count):
            next_coord = cave_data_coords[i]
            write_line(cave_data, cur_coord, next_coord)
            cur_coord = next_coord
    return cave_data

def process_data_p2(file_path):
    cave_file_data = []
    with open(file_path, 'r') as f:
        cave_file_data = [line.strip() for line in f.readlines()]

    # in cave data 0 is air, 1 is rock and 2 is sand
    # The arrys is 1000x200
    cave_data = [[0 for _ in range(200)] for _ in range(1000)] 
    largest_y = 0
    # process data
    for line in cave_file_data:
        cave_data_coords_strings = [coords.split(',') for coords in line.split('->')]
        cave_data_coords = [[int(coords[0]), int(coords[1])] for coords in cave_data_coords_strings]

        line_count = len(cave_data_coords)
        cur_coord = cave_data_coords[0]
        for i in range(1,line_count):
            next_coord = cave_data_coords[i]
            write_line(cave_data, cur_coord, next_coord)
            if largest_y < max(cur_coord[1], next_coord[1]):
                largest_y = max(cur_coord[1], next_coord[1])
                
            cur_coord = next_coord

    for i in range(1000):
        cave_data[i][largest_y+2] = 1
    return cave_data

def move_sand(data, pos):
    if data[pos[0]][pos[1]+1] == 0:
        return [pos[0], pos[1]+1]
    if data[pos[0]-1][pos[1]+1] == 0:
        return [pos[0]-1, pos[1]+1]
    if data[pos[0]+1][pos[1]+1] == 0:
        return [pos[0]+1, pos[1]+1]
    return pos

if __name__ == '__main__':
    cave_data = process_data('./input')

    sum_p1 = 0
    lower_border = 199 # when to stop
    simulation_running = True
    while simulation_running:
        sand_pos = [500, 0] # spawning position
        
        settled = False
        while not settled:
            old_sand_pos = sand_pos
            sand_pos = move_sand(cave_data, sand_pos)

            if old_sand_pos == sand_pos: # no movement
                settled = True 
                cave_data[sand_pos[0]][sand_pos[1]] = 2
                sum_p1 += 1
            elif sand_pos[1] >= lower_border: # end
               simulation_running = False
               break

    #print_data(cave_data, 350, 0, 650, 200)
    print(sum_p1)

    sum_p2 = 0
    
    cave_data = process_data_p2('./input')
    simulation_running = True
    while simulation_running:
        sand_pos = [500, 0] # spawning position
        
        settled = False
        while not settled:
            old_sand_pos = sand_pos
            sand_pos = move_sand(cave_data, sand_pos)
            

            if old_sand_pos == sand_pos: # no movement
                settled = True 
                sum_p2 += 1
                cave_data[sand_pos[0]][sand_pos[1]] = 2

                if sand_pos == [500,0]:
                    simulation_running = False
                    break

    #print_data(cave_data, 350, 0, 650, 200)
    print(sum_p2)


