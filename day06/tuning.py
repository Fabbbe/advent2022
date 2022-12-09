
# find the start of package marker
def find_sop(message, length):
    sop = 0
    
    # length has to be subtracted so index i+j does not grow too big
    for i in range(len(message)-length):
        found = [] # list of chars found in message at index
        for j in range(length):

            if message[i+j] in found:
                break
            else:
                found.append(message[i+j])

        if len(found) == length:
            sop = i+length
            break

    return sop

if __name__ == '__main__':
    f = open('./input', 'r')
    message = f.read()
    f.close()
    
    start_of_package = find_sop(message, 4)
    start_of_message = find_sop(message, 14)

    print(start_of_package)
    print(start_of_message)
