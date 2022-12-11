import sys
import numpy

class Monkey:
    items: []
    operator: int # 0 is * and 1 is +
    number: int
    test_divisor: int
    true_monkey: int
    false_monkey: int
    total_thrown: int

    def __init__(self, starting_items: [], operation: str, test_divisor: int, true_monkey: int, false_monkey: int):
        self.items = starting_items

        if operation.split(' ')[1] == '*':
            self.operator = 0
        else:
            self.operator = 1

        if operation.split(' ')[2].strip() == 'old':
            self.number = -1
        else:
            self.number = int(operation.split(' ')[2].strip())
            
        self.test_divisor = test_divisor
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.total_thrown = 0

def read_monkeys(path: str):
    monkeys_data = []
    with open(path, 'r') as f:
        monkeys_data = f.read().split('\n\n')

    monkeys = []
    for monkey_data in monkeys_data:
        # Create monkeys
        monkey_data_lines = monkey_data.split('\n')
        starting_items_string = monkey_data_lines[1].split(':')[1].split(',')
        starting_items = []
        for starting_item_string in starting_items_string:
            starting_items.append(int(starting_item_string))
        #print(starting_items)

        operation = monkey_data_lines[2].split('=')[1].strip()
        #print(operation) # should find a better way to format this

        test_divisor = int(monkey_data_lines[3].split(' ')[5].strip())
        #print(test_divisor)
        true_monkey = int(monkey_data_lines[4].split(' ')[9].strip())
        #print(true_monkey)
        false_monkey = int(monkey_data_lines[5].split(' ')[9].strip())
        #print(false_monkey)
        
        monkey = Monkey(starting_items, operation, test_divisor, true_monkey, false_monkey)

        monkeys.append(monkey)

    return monkeys

if __name__ == '__main__':

    sys.set_int_max_str_digits(1280000)

    monkeys = read_monkeys('./input')

    for i in range(20):
        for monkey in monkeys:
            for j in range(len(monkey.items)):
                old = monkey.items[0]
                new = 0

                number = 0
                if monkey.number == -1:
                    number = old
                else:
                    number = monkey.number

                if monkey.operator == 0:
                    new = old * number
                else:
                    new = old + number
                new = new // 3
                #print(new)

                if new % monkey.test_divisor == 0:
                    monkeys[monkey.true_monkey].items.append(new)
                    monkey.items.pop(0)
                else:
                    monkeys[monkey.false_monkey].items.append(new)
                    monkey.items.pop(0)

                monkey.total_thrown += 1

    list_p1 = [monkey.total_thrown for monkey in monkeys]
    largest_p1 = sorted(list_p1, reverse=True)[0:2]

    print('Part 1:')
    print(largest_p1)
    print(largest_p1[0]*largest_p1[1])

    # Reload monkeys
    monkeys = read_monkeys('./input')

    # find all divisors without duplicates
    divisors_all = [m.test_divisor for m in monkeys]
    divisors = []
    [divisors.append(x) for x in divisors_all if x not in divisors]
    divis = numpy.prod(divisors)

    for i in range(10000):
        #print(i)
        for monkey in monkeys:
            for j in range(len(monkey.items)):
                old = monkey.items[0]
                new = 0

                number = 0
                if monkey.number == -1:
                    number = old
                else:
                    number = monkey.number

                if monkey.operator == 0:
                    new = old * number
                else:
                    new = old + number

                new = new % divis

                if new % monkey.test_divisor == 0:
                    monkeys[monkey.true_monkey].items.append(new)
                    monkey.items.pop(0)
                else:
                    monkeys[monkey.false_monkey].items.append(new)
                    monkey.items.pop(0)

                monkey.total_thrown += 1

    list_p2 = [monkey.total_thrown for monkey in monkeys]
    largest_p2 = sorted(list_p2, reverse=True)[0:2]

    print('Part 2:')
    print(largest_p2)
    print(largest_p2[0]*largest_p2[1])
