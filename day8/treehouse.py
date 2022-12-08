
def visible(trees, x, y):
    #print(str(x)+' '+str(y))
    height = len(trees)
    width = len(trees[0])

    left_smaller = True
    right_smaller = True
    up_smaller = True
    down_smaller = True

    for i in range(0, x):
        if trees[i][y] >= trees[x][y]:
            left_smaller = False
            break

    for i in range(x+1, width):
        if trees[i][y] >= trees[x][y]:
            right_smaller = False
            break

    for i in range(0, y):
        if trees[x][i] >= trees[x][y]:
            up_smaller = False
            break

    for i in range(y+1, height):
        if trees[x][i] >= trees[x][y]:
            down_smaller = False
            break

    if left_smaller or right_smaller or up_smaller or down_smaller:
        return True
    return False

def score_tree(trees, x, y):
    height = len(trees)
    width = len(trees[0])
    
    left_visible = 0
    right_visible = 0
    up_visible = 0
    down_visible = 0

    for i in reversed(range(0, x)):
        left_visible += 1
        if trees[i][y] >= trees[x][y]:
            break
    for i in range(x+1, width):
        right_visible += 1
        if trees[i][y] >= trees[x][y]:
            break
    for i in reversed(range(0, y)):
        up_visible += 1
        if trees[x][i] >= trees[x][y]:
            break
    for i in range(y+1, height):
        down_visible += 1
        if trees[x][i] >= trees[x][y]:
            break

    return left_visible*right_visible*up_visible*down_visible

if __name__ == '__main__':
    lines = []
    with open('./input', 'r') as f:
        lines = f.read().splitlines()
    
    height = len(lines)
    width = len(lines[0])

    # All trees around the forest are known visible
    visible_tree_count = width*2 + height*2 - 4

    # iterate through all trees
    for y in range(1, height-1):
        for x in range(1, width-1):
            visible_tree_count += 1 if visible(lines, x, y) else 0

    highest_tree_score = 0
    for y in range(1, height-1):
        for x in range(1, width-1):
            new_score = score_tree(lines, x, y)
            highest_tree_score = new_score if new_score > highest_tree_score else highest_tree_score


    print('Part 1: '+str(visible_tree_count))
    print('Part 2: '+str(highest_tree_score))
