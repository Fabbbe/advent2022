
# CRT is 40 by 6 pixels
# X register is the position of the middle of a 3px wide sprite
def draw_pixel(clock_cycle, x):
    if (clock_cycle-1)%40 == 0:
        print()
    if (clock_cycle-1)%40>=x-1 and (clock_cycle-1)%40<=x+1:
        print('#', end='')
    else:
        print('.', end='')


if __name__ == '__main__':
    lines = []
    with open('./input', 'r') as f:
        #lines = f.readlines()
        # rstrip to remove newlines
        lines = [x.rstrip() for x in f.readlines()]

    clock_cycle = 1
    x = 1
    sum = 0
    for line in lines:
        split_line = line.split(' ')

        if (clock_cycle+20) % 40 == 0:
            sum += x*clock_cycle

        if split_line[0] == 'noop':
            clock_cycle += 1
            pass
        else: # addx
            clock_cycle += 1
            if (clock_cycle+20) % 40 == 0:
                sum += x*clock_cycle

            x += int(split_line[1])
            clock_cycle += 1

    print(sum)

    clock_cycle = 1
    x = 1
    for line in lines:
        split_line = line.split(' ')

        draw_pixel(clock_cycle, x)

        if split_line[0] == 'noop':
            clock_cycle += 1
            pass
        else: # addx
            clock_cycle += 1
            draw_pixel(clock_cycle, x)

            x += int(split_line[1])
            clock_cycle += 1

    print()
