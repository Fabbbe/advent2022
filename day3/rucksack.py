#!/bin/python3

priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

if __name__ == '__main__':
    f = open('./input', 'r')
    lines = f.readlines()
    lines = [line[:-1] for line in lines]
    sum_p1 = 0
    for line in lines:
        middle = int(len(line)/2)
        first = line[0:middle]
        last = line[middle:]
        for c in first:
            if c in last:
                sum_p1 += priority.index(c)+1
                break
    
    sum_p2 = 0
    for i in range(0, len(lines), 3):
        for c in lines[i]:
            if c in lines[i+1] and c in lines[i+2]:
                sum_p2 += priority.index(c)+1
                break;

    print("Part 1: " + str(sum_p1))
    print("Part 2: " + str(sum_p2))

