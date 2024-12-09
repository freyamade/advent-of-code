from itertools import product


def get_part_1_answer(input: str) -> int:
    output = 0
    for line in input.split('\n'):
        test, inputs = line.split(': ')
        test = int(test)
        inputs = [int(x) for x in inputs.split()]
        gaps = len(inputs) - 1
        potential_gap_fills = product('+*', repeat=gaps)
        for fillers in potential_gap_fills:
            test_value = inputs[0]
            for i in range(1, len(inputs)):
                op = fillers[i-1]
                if op == '+':
                    test_value += inputs[i]
                else:
                    test_value *= inputs[i]

            if test_value == test:
                output += test
                break
    return output


def get_part_2_answer(input: str) -> int:
    output = 0
    for line in input.split('\n'):
        test, inputs = line.split(': ')
        test = int(test)
        inputs = [int(x) for x in inputs.split()]
        gaps = len(inputs) - 1
        potential_gap_fills = product(['+', '*', '||'], repeat=gaps)
        for fillers in potential_gap_fills:
            test_value = inputs[0]
            for i in range(1, len(inputs)):
                op = fillers[i-1]
                if op == '+':
                    test_value += inputs[i]
                elif op == '||':
                    test_value = int(str(test_value) + str(inputs[i]))
                else:
                    test_value *= inputs[i]

            if test_value == test:
                output += test
                break
    return output


if __name__ == '__main__':
    test_message = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
""".strip()
    assert get_part_1_answer(test_message) == 3749
    assert get_part_2_answer(test_message) == 11387
    with open('input.txt') as f:
        message = f.read().strip()
    print(f'Answer for part 1: {get_part_1_answer(message)}')
    print(f'Answer for part 2: {get_part_2_answer(message)}')

