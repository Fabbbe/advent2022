from functools import cmp_to_key
from ast import literal_eval

''' 
The main function that implements the actual comparisons. 
The base case if both input variables are integers, then we compare.
If not then both should be lists, and if so we loop through them.
And lastly if both aren't lists, make them both lists
'''
def less_than(left, right):
    # First different value in left should be larger than right
    if isinstance(left, int) and isinstance(right, int):
        return left < right

    # Both are lists
    elif isinstance(left, list) and isinstance(right, list):
        shortest_len = min(len(left), len(right))
        for i in range(shortest_len):
            if less_than(left[i], right[i]):
                return True
            elif less_than(right[i], left[i]):
                return False

        # If loop fails
        return len(left) < len(right)
            
    # Only left is list
    elif isinstance(left, list):
        return less_than(left, [right])

    # Only right is list
    elif isinstance(right, list):
        return less_than([left], right)

    exit() # fail, should never get here

def compare_strings(left, right):
    if left == right:
        return 0
    elif less_than(literal_eval(left), literal_eval(right)):
        return -1
    return 1

def signal_order_check(signal):
    left = literal_eval(signal[0])
    right = literal_eval(signal[1])
    return less_than(left, right)

if __name__ == '__main__':
    # PART 1
    # ------
    signal_data = []
    with open('./input', 'r') as f:
        lines = f.read().split('\n\n')
        for line in lines:
            signal_data.append(line.split('\n'))

    sum = 0
    for i in range(len(signal_data)):
        if(signal_order_check(signal_data[i])): 
            sum += i + 1 # +1 since indices start at 1 (very bad)

    print('Part 1:', sum)

    # PART 2
    # ------
    
    # We redefine signal_data since we read the data differently from part 1
    signal_data = []
    with open('./input', 'r') as f:
        signal_data = [line for line in f.read().split('\n') if len(line) != 0]
    signal_data.append('[[2]]')
    signal_data.append('[[6]]')

    sorted_signal = sorted(signal_data, key=cmp_to_key(compare_strings) )

    # + 1 since the indices start at 1
    decoder_part_1 = sorted_signal.index('[[2]]') + 1
    decoder_part_2 = sorted_signal.index('[[6]]') + 1

    print('Part 2:',decoder_part_1*decoder_part_2)
