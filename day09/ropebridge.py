def get_sign(x):
    return 1 if x >= 0 else -1

if __name__ == '__main__':
    lines =  []
    with open('./input', 'r') as f:
        lines = f.readlines()
     
    # X and Y for head and tail
    head_pos = [0, 0]
    tail_pos = [0, 0]

    unique_positions_p1 = [[0, 0]] # NEEDS TO BE FIXED

    for line in lines:
        split_line = line.split(' ')

        # Determine the next head position
        if split_line[0] == 'R':
            head_pos[0] += int(split_line[1])
        elif split_line[0] == 'L':
            head_pos[0] -= int(split_line[1])
        elif split_line[0] == 'U':
            head_pos[1] += int(split_line[1])
        elif split_line[0] == 'D':
            head_pos[1] -= int(split_line[1])

        while True:
            pos_diff = [head_pos[0]-tail_pos[0], head_pos[1]-tail_pos[1]]

            # Check if touching
            if pos_diff[0] <= 1 and pos_diff[0] >= -1 and pos_diff[1] <= 1 and pos_diff[1] >= -1:
                    break;

            # If not we should move diagonally first
            if pos_diff[0] != 0 and pos_diff[1] != 0:
                tail_pos[0] += get_sign(pos_diff[0])
                tail_pos[1] += get_sign(pos_diff[1])
            elif pos_diff[0] != 0:
                tail_pos[0] += get_sign(pos_diff[0])
            elif pos_diff[1] != 0:
                tail_pos[1] += get_sign(pos_diff[1])
            # I DO NOT LIKE THIS
            deep_copy = [0,0]
            deep_copy[0] = tail_pos[0]
            deep_copy[1] = tail_pos[1]
            if not deep_copy in unique_positions_p1: 
                unique_positions_p1.append(deep_copy)

    head_pos = [0,0]
    tail_pos = [ # 9 other knots
        [0,0], # 0
        [0,0], # 1
        [0,0], # 2
        [0,0], # 3
        [0,0], # 4
        [0,0], # 5
        [0,0], # 6
        [0,0], # 7
        [0,0]  # 8
    ]

    

    unique_positions_p2 = [[0, 0]] 

    for line in lines:
        split_line = line.split(' ')

        # Determine the next head position
        if split_line[0] == 'R':
            head_pos[0] += int(split_line[1])
        elif split_line[0] == 'L':
            head_pos[0] -= int(split_line[1])
        elif split_line[0] == 'U':
            head_pos[1] += int(split_line[1])
        elif split_line[0] == 'D':
            head_pos[1] -= int(split_line[1])

        tail_pos_moved = [ 
            True, # 0
            True, # 1
            True, # 2
            True, # 3
            True, # 4
            True, # 5
            True, # 6
            True, # 7
            True  # 8
        ]
        while True in tail_pos_moved:
            for i in range(9): # UPDATE ONE AT A TIME
                pos_diff = []
                if i == 0:
                    pos_diff = [head_pos[0]-tail_pos[i][0], head_pos[1]-tail_pos[i][1]]
                else: # if not first, check against the last piece of the tail
                    pos_diff = [tail_pos[i-1][0]-tail_pos[i][0], tail_pos[i-1][1]-tail_pos[i][1]]

                # Check if touching
                if pos_diff[0] <= 1 and pos_diff[0] >= -1 and pos_diff[1] <= 1 and pos_diff[1] >= -1:
                    tail_pos_moved[i] = False
                    pass;
                else:
                    # If not we should move diagonally first
                    if pos_diff[0] != 0 and pos_diff[1] != 0:
                        tail_pos[i][0] += get_sign(pos_diff[0])
                        tail_pos[i][1] += get_sign(pos_diff[1])
                    elif pos_diff[0] != 0:
                        tail_pos[i][0] += get_sign(pos_diff[0])
                    elif pos_diff[1] != 0:
                        tail_pos[i][1] += get_sign(pos_diff[1])
                    if i == len(tail_pos)-1: # last element
                        deep_copy = [0,0]
                        deep_copy[0] = tail_pos[i][0]
                        deep_copy[1] = tail_pos[i][1]
                        if not deep_copy in unique_positions_p2: 
                            unique_positions_p2.append(deep_copy)


            
    print('Part 1: '+str(len(unique_positions_p1)))
    print('Part 2: '+str(len(unique_positions_p2)))
