def find_ms_for_x(matrix, i, j):
    max_i = len(matrix)
    max_j = len(matrix[0])
    neighbours = [
        (i-1, j-1), (i-1, j), (i-1, j+1),
        (i, j-1), (i, j+1),
        (i+1, j-1), (i+1, j), (i+1, j+1),
    ]
    ms = []
    for ni, nj in neighbours:
        if ni < 0 or nj < 0 or ni >= max_i or nj >= max_j:
            continue
        if matrix[ni][nj] == 'M':
            ms.append((ni, nj))
    return ms


def get_part_1_answer(input: str) -> int:
    matrix = [list(line) for line in input.split('\n')]
    words = []
    changed = True
    max_i = len(matrix)
    max_j = len(matrix[0])
    while changed:
        changed = False
        # Go through the matrix, see if each letter has the next letter it needs anywhere around it, and if not replace it with a dot
        for i in range(max_i):
            for j in range(max_j):
                char = matrix[i][j]
                if char != 'X':
                    continue
                # If it is an X, find all the Ms
                m_neighbours = find_ms_for_x(matrix, i, j)
                
                # If we have neighbours we need to follow it out to the point where we either finish the word, or break the word
                for mi, mj in m_neighbours:
                    idir, jdir = (mi - i, mj - j)
                    ai, aj = mi + idir, mj + jdir
                    si, sj = ai + idir, aj + jdir
                    if ai < 0 or aj < 0 or si < 0 or sj < 0:
                        continue
                    if ai >= max_i or aj >= max_j or si >= max_i or sj >= max_j:
                        continue
                    if matrix[ai][aj] == 'A' and matrix[si][sj] == 'S':
                        pos = f'{i}{j}{mi}{mj}{ai}{aj}{si}{sj}'
                        words.append(pos)

    return len(words)


def get_part_2_answer(input: str) -> int:
    matrix = [list(line) for line in input.split('\n')]
    centers = []
    changed = True
    max_i = len(matrix)
    max_j = len(matrix[0])
    while changed:
        changed = False
        # Go through the matrix internally (avoiding the outer rows)
        for i in range(1, max_i - 1):
            for j in range(1, max_j - 1):
                char = matrix[i][j]
                if char != 'A':
                    continue
                # Get all the M neighbours of this A
                ms = set(find_ms_for_x(matrix, i, j))
                # Get the intersection of the set of m positions with the 4 diagonals
                diagonals = {
                    (i-1, j-1),
                    (i-1, j+1),
                    (i+1, j-1),
                    (i+1, j+1),
                }
                m_diags = ms & diagonals
                # We need to have exactly 2 Ms on the diagonals to potentially be a valid solution
                if len(m_diags) != 2:
                    continue
                # If the Ms are across from eachother then it's also invalid
                opposites = {
                    (i-1, j-1): (i+1, j+1),
                    (i-1, j+1): (i+1, j-1),
                }
                valid = True
                for x, y in opposites.items():
                    if matrix[x[0]][x[1]] == 'M' and matrix[y[0]][y[1]] == 'M':
                        valid = False
                if not valid:
                    continue

                # if the remaining two diagonals are S then the A is valid
                s_diags = diagonals - m_diags
                valid = True
                for si, sj in s_diags:
                    if matrix[si][sj] != 'S':
                        valid = False
                if valid:
                    centers.append((i, j))
    return len(centers)


if __name__ == '__main__':
    test_message = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".strip()
    assert get_part_1_answer(test_message) == 18
    assert get_part_2_answer(test_message) == 9, get_part_2_answer(test_message)
    with open('input.txt') as f:
        message = f.read().strip()
    print(f'Answer for part 1: {get_part_1_answer(message)}')
    print(f'Answer for part 2: {get_part_2_answer(message)}')

