#!/bin/python3

if __name__ == '__main__':
    f = open('./input', 'r')
    content = f.read()
    f.close()

    box_lines = []
    move_lines = []

    box_content, move_content = content.split('\n\n')
    box_lines = box_content.split('\n')
    move_lines = move_content.split('\n')
    box_lines.pop() # Remove the index line
    move_lines.remove('') # Remove any empty lines

    box_lines.reverse()

    boxes_p1 = [[],[],[],[],[],[],[],[],[]]
    boxes_p2 = [[],[],[],[],[],[],[],[],[]]

    for i in range(len(box_lines)):
        for j in range(9):
            index = j*4+1
            if box_lines[i][index] != ' ':
                boxes_p1[j].append(box_lines[i][index])
                boxes_p2[j].append(box_lines[i][index])

    # Crane moves one box at a time
    for line in move_lines:
        lst = line.split(' ')
        count = int(lst[1])
        from_index = int(lst[3]) -1
        to_index = int(lst[5]) -1
        
        from_len = len(boxes_p1[from_index])
        for i in range(count):
            boxes_p1[to_index].append(boxes_p1[from_index][from_len-i-1])
            boxes_p1[from_index].pop(from_len-i-1)

    print('Part 1:')
    for i in range(len(boxes_p1)):
        print(boxes_p1[i][-1], end='')
    print()

    # Crane moves all the boxes at once
    for line in move_lines:
        lst = line.split(' ')
        count = int(lst[1])
        from_index = int(lst[3]) -1
        to_index = int(lst[5]) -1
        
        from_len = len(boxes_p2[from_index])
        for i in range(count):
            boxes_p2[to_index].append(boxes_p2[from_index][from_len-count])
            boxes_p2[from_index].pop(from_len-count)
        

    print('Part 2:')
    for i in range(len(boxes_p2)):
        print(boxes_p2[i][-1], end='')
    print()
