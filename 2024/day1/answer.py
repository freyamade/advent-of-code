def get_part_1_answer(input: str) -> int:
    # Split each line and add numbers to each list
    left_side = []
    right_side = []
    for line in input.split('\n'):
        l, r = line.split()
        left_side.append(int(l))
        right_side.append(int(r))

    # Sort the lists and calc the difference between the elements in the array
    left_side.sort()
    right_side.sort()
    distance = 0
    for l, r in zip(left_side, right_side):
        distance += abs(l - r)
    return distance


def get_part_2_answer(input: str) -> int:
    left_side = []
    right_side = []
    for line in input.split('\n'):
        l, r = line.split()
        left_side.append(int(l))
        right_side.append(int(r))

    similarity = 0
    for item in left_side:
        similarity += item * (right_side.count(item))
    return similarity


if __name__ == '__main__':
    test_message = """
3   4
4   3
2   5
1   3
3   9
3   3""".strip()
    assert get_part_1_answer(test_message) == 11
    assert get_part_2_answer(test_message) == 31
    with open('input.txt') as f:
        message = f.read().strip()
    print(f'Answer for part 1: {get_part_1_answer(message)}')
    print(f'Answer for part 2: {get_part_2_answer(message)}')

