
# I probably overcomplicated this :-)
# A = Rock     1pt
# B = Paper    2pt
# C = Scissor  3pt
# X = Rock     1pt
# Y = Paper    2pt
# Z = Scissor  3pt
points = {
    'A' : 1,
    'B' : 2,
    'C' : 3,
    'X' : 1,
    'Y' : 2,
    'Z' : 3,
}

if __name__ == '__main__':
    f = open('./input', 'r')
    lines = f.readlines()
    f.close()

    elf_p1 = 0
    me_p1 = 0
    elf_p2 = 0
    me_p2 = 0

    for line in lines:
        # Loose        0pt
        # Draw         3pt
        # Win          6pt
        elf_p1 += points[line[0]]
        me_p1 += points[line[2]]

        if points[line[0]] == points[line[2]]:
            elf_p1 += 3
            me_p1 += 3
        elif (points[line[0]]+1 == points[line[2]]) or (line[0] == 'C' and line[2] == 'X'):
            elf_p1 += 0
            me_p1 += 6
        else:
            elf_p1 += 6
            me_p1 += 0

    for line in lines:
        elf_p2 += points[line[0]]

        if line[2] == 'X':
            elf_p2 += 6
            me_p2 += 0
            
            if points[line[0]]-1 != 0:
                me_p2 += points[line[0]]-1
            else:
                me_p2 += 3

        elif line[2] == 'Y':
            elf_p2 += 3
            me_p2 += 3 + points[line[0]]
        else:
            elf_p2 += 0
            me_p2 += 6

            if points[line[0]]+1 != 4:
                me_p2 += points[line[0]]+1
            else:
                me_p2 += 1


    print(elf_p1)
    print(me_p1)
    print(elf_p2)
    print(me_p2)
