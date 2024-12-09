from collections import defaultdict
import math
from typing import Dict, List, Tuple


def get_all_antennae(matrix: List[List[str]]) -> Dict[str, List[Tuple[int, int]]]:
    positions = defaultdict(list)
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == '.':
                continue
            positions[matrix[x][y]].append((x, y))
    return positions


def find_inline(antennae, x, y) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    """
    Returns pairs of antennae we're inline with, of the same frequency
    """
    inlines = []
    for freq, positions in antennae.items():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                ipos = positions[i]
                jpos = positions[j]

                if (ipos[0] - x) * (jpos[1] - y) == (jpos[0] - x) * (ipos[1] - y):
                    inlines += [(ipos, jpos)]
    return inlines


def get_part_1_answer(input: str) -> int:
    matrix = [list(line) for line in input.split('\n')]
    antennae = get_all_antennae(matrix)
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            # Find all antennae positions we're in line with
            in_line_antennae = find_inline(antennae, x, y)
            for in_line_pair in in_line_antennae:
                (ant1_x, ant1_y), (ant2_x, ant2_y) = in_line_pair
                # Get distances between our current position and both antennae
                ant1_distance = math.sqrt((ant1_x - x) ** 2 + (ant1_y - y) ** 2)
                ant2_distance = math.sqrt((ant2_x - x) ** 2 + (ant2_y - y) ** 2)
                if (ant1_distance == 2 * ant2_distance) or (ant2_distance == 2 * ant1_distance):
                    matrix[x][y] = '#'
    townmap = '\n'.join(''.join(line) for line in matrix)
    return townmap.count('#')


def get_part_2_answer(input: str) -> int:
    matrix = [list(line) for line in input.split('\n')]
    antennae = get_all_antennae(matrix)
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            # Find all antennae positions we're in line with
            in_line_antennae = find_inline(antennae, x, y)
            if in_line_antennae:
                matrix[x][y] = '#'
    townmap = '\n'.join(''.join(line) for line in matrix)
    return townmap.count('#')


if __name__ == '__main__':
    test_message = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............""".strip()
    matrix = [list(line) for line in test_message.split('\n')]
    assert get_all_antennae(matrix) == {
        '0': [(1, 8), (2, 5), (3, 7), (4, 4)],
        'A': [(5, 6), (8, 8), (9, 9)],
    }
    assert find_inline(get_all_antennae(matrix), 0, 11) == [((1, 8), (2, 5))]
    assert get_part_1_answer(test_message) == 14
    assert get_part_2_answer(test_message) == 34
    with open('input.txt') as f:
        message = f.read().strip()
    print(f'Answer for part 1: {get_part_1_answer(message)}')
    print(f'Answer for part 2: {get_part_2_answer(message)}')

