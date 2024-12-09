from copy import deepcopy
from enum import Enum
from typing import Tuple, List


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


def setup(input: str) -> Tuple[List[List[str]], Tuple[int, int]]:
    """
    Generates the matrix and returns the starting guard position
    """
    matrix = [
        list(line)
        for line in input.split('\n')
    ]
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == '^':
                return matrix, (x, y)
    return None


def track_path(input: str) -> str:
    matrix, (guard_x, guard_y) = setup(input)
    max_x = len(matrix)
    max_y = max(len(line) for line in matrix)
    range_x = range(0, max_x)
    range_y = range(0, max_y)
    guard = Direction.UP
    while guard_x in range_x and guard_y in range_y:
        next_x = guard_x
        next_y = guard_y
        match guard:
            case Direction.UP:
                next_x -= 1
            case Direction.DOWN:
                next_x += 1
            case Direction.LEFT:
                next_y -= 1
            case Direction.RIGHT:
                next_y += 1
        try:
            if matrix[next_x][next_y] == '#':
                # Update the Guard direction
                guard = Direction((guard.value + 1) % 4)
                continue
        except IndexError:
            pass
        # Otherwise, move the guard and put an X where they used to be
        matrix[guard_x][guard_y] = 'X'
        try:
            matrix[next_x][next_y] = 'G'
        except IndexError:
            pass
        guard_x = next_x
        guard_y = next_y
    return '\n'.join(''.join(line) for line in matrix)


def test_path_with_new_obstacle(matrix: List[List[str]], guard_pos: Tuple[int, int], new_obstacle_pos: Tuple[int, int]) -> bool:
    """
    If the guard hits the same obstacle twice, return True
    Otherwise we haven't made a loop
    """
    matrix = deepcopy(matrix)
    guard_x, guard_y = guard_pos
    new_obs_x, new_obs_y = new_obstacle_pos
    matrix[new_obs_x][new_obs_y] = 'O'
    max_x = len(matrix)
    max_y = max(len(line) for line in matrix)
    range_x = range(0, max_x)
    range_y = range(0, max_y)
    guard = Direction.UP
    on_same_path = False
    steps_on_same_path = 0
    while (guard_x in range_x and guard_y in range_y):
        next_x = guard_x
        next_y = guard_y
        match guard:
            case Direction.UP:
                next_x -= 1
            case Direction.DOWN:
                next_x += 1
            case Direction.LEFT:
                next_y -= 1
            case Direction.RIGHT:
                next_y += 1
        try:
            if matrix[next_x][next_y] in {'#', 'O'}:
                # Update the Guard direction
                guard = Direction((guard.value + 1) % 4)
                continue
        except IndexError:
            pass
        # Otherwise, move the guard and put an X where they used to be
        matrix[guard_x][guard_y] = 'X'
        try:
            if matrix[next_x][next_y] == 'X':
                if not on_same_path:
                    on_same_path = True
                if on_same_path:
                    steps_on_same_path += 1
                    if steps_on_same_path > 10000:
                        # Infinite loop early escape
                        return True
            else:
                on_same_path = False
                steps_on_same_path = 0
            matrix[next_x][next_y] = 'G'
        except IndexError:
            pass
        guard_x = next_x
        guard_y = next_y
        
    return False


def get_part_1_answer(input: str) -> int:
    return track_path(input).count('X')


def get_part_2_answer(input: str) -> int:
    positions = 0
    matrix, guard = setup(input)
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            # Ignore right in front of the guard
            if (x + 1) == guard[0] and y == guard[1]:
                continue
            # Ignore also the existing positions of obstacles
            if matrix[x][y] == '#':
                continue
            print(x, y)
            if test_path_with_new_obstacle(matrix, guard, (x, y)):
                print('  valid')
                positions += 1
    return positions


if __name__ == '__main__':
    test_message = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".strip()
    assert setup(test_message)[1] == (6, 4)
    assert get_part_1_answer(test_message) == 41
    assert get_part_2_answer(test_message) == 6
    with open('input.txt') as f:
        message = f.read().strip()
    print(f'Answer for part 1: {get_part_1_answer(message)}')
    print(f'Answer for part 2: {get_part_2_answer(message)}')

