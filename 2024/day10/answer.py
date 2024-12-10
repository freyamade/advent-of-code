def get_all_zero_heights(matrix: list[list[int]]):
    positions = []
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == 0:
                positions.append((x, y))
    return positions


def get_values_around_position(matrix: list[list[int]], x, y, value):
    positions = []
    pairs = [
        (x-1, y),
        (x, y-1),
        (x, y+1),
        (x+1, y),
    ]
    for test_x, test_y in pairs:
        if test_x not in range(len(matrix)) or test_y not in range(len(matrix[test_x])):
            continue
        if matrix[test_x][test_y] == value:
            positions.append((test_x, test_y))
    return positions


def follow_trail(matrix, x, y, value = 0):
    endings = set()
    if value == 9:
        return {(x, y)}
    # Otherwise, do recursion
    for test_x, test_y in get_values_around_position(matrix, x, y, value+1):
        for output in follow_trail(matrix, test_x, test_y, value+1):
            endings.add(output)
    return endings


def rate_trail(matrix, x, y, value = 0):
    score = 0
    if value == 9:
        return 1
    # Otherwise, do recursion
    for test_x, test_y in get_values_around_position(matrix, x, y, value+1):
        score += rate_trail(matrix, test_x, test_y, value+1)
    return score


def get_part_1_answer(input: str) -> int:
    matrix = [
        list(map(lambda x: int(x), line))
        for line in input.split('\n')
    ]
    # Find all the 0s then recursively search them for their trailhead score
    score = 0
    for x, y in get_all_zero_heights(matrix):
        score += len(follow_trail(matrix, x, y))
    return score


def get_part_2_answer(input: str) -> int:
    matrix = [
        list(map(lambda x: int(x), line))
        for line in input.split('\n')
    ]
    # Find all the 0s then recursively search them for their trailhead score
    score = 0
    for x, y in get_all_zero_heights(matrix):
        score += rate_trail(matrix, x, y)
    return score


if __name__ == '__main__':
    test_message = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""".strip()
    assert get_part_1_answer(test_message) == 36
    assert get_part_2_answer(test_message) == 81
    with open('input.txt') as f:
        message = f.read().strip()
    print(f'Answer for part 1: {get_part_1_answer(message)}')
    print(f'Answer for part 2: {get_part_2_answer(message)}')

