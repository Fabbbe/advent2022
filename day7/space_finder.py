
if __name__ == '__main__':
    f = open('./input', 'r')
    lines = f.readlines()
    f.close()

    dirs = [] # List of all dirs as strings
    dir_sizes = [] # This is the total size of all files and dirs
    dir_direct_sizes = [] # This is the size of all files directly in the dir

    cur_dir = '/' # Start at root
    for line in lines:
        split_line = line.split(' ')
        if split_line[0] == '$': # This is a command
            if 'cd' in split_line[1]:
                new_dir = split_line[2][:-1] # Removes newline
                if new_dir == '/': 
                    cur_dir = '/'
                elif '..' in new_dir:
                    cur_dir = cur_dir[0:cur_dir.rindex('/')] # Finds the last '/'
                else:
                    if cur_dir != '/':
                        cur_dir = cur_dir + '/' + new_dir 
                    else: 
                        cur_dir = cur_dir + new_dir 

                if cur_dir == '': # This is a special case so that cur_dir does not get empty
                    cur_dir = '/'

                # Append zeroes to the sizes to that the indexes exist for later
                if not cur_dir in dirs:
                    dirs.append(cur_dir)
                    dir_direct_sizes.append(0)
                    dir_sizes.append(0)
                
        elif split_line[0] == 'dir': # We ignore dir lines
            pass
        else: # Add all the files in cur_dir to the list
            dir_direct_sizes[dirs.index(cur_dir)] += int(split_line[0])

    # Sum all subdirectories
    for i in range(len(dirs)):
        for j in range(len(dirs)):
            if dirs[i] in dirs[j]: # This is a real subdirectory
                dir_sizes[i] += dir_direct_sizes[j]
    
    sum_p1 = 0
    for size in dir_sizes:
        if size <= 100000:
            sum_p1 += size

    total_space = 70000000  # 70 000 000
    needed_space = 30000000 # 30 000 000
    used_space = dir_sizes[dirs.index('/')] # "/" Includes all other dirs
    unused_space = total_space - used_space
    space_to_delete = needed_space - unused_space

    smallest_size = total_space # Every dir is smaller than this
    for dir_size in dir_sizes:
        if smallest_size > dir_size and dir_size > space_to_delete:
            smallest_size = dir_size

    # Print results
    print('Sum of dirs smaller than 100k: ' + str(sum_p1))
    print('Smallest dir to delete: ' + str(smallest_size))
