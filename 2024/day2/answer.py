def get_safety(report: list) -> bool:
    diff = None
    for i in range(len(report) - 1):
        x = report[i]
        y = report[i+1]
        curr_diff = y - x

        if abs(curr_diff) not in range(1, 4):
            return False

        # Check if it's the same direction as the last one
        if diff is None:
            diff = curr_diff
        elif diff * curr_diff < 0:
            # -*- or +*+ are always +
            return False
    return True


def get_part_1_answer(input: str) -> int:
    safe = 0
    for line in input.split('\n'):
        report = list(map(lambda x: int(x), line.split()))
        if get_safety(report):
            safe += 1
    return safe


def get_part_2_answer(input: str) -> int:
    safe = 0
    for line in input.split('\n'):
        report = list(map(lambda x: int(x), line.split()))
        if get_safety(report):
            safe += 1
        else:
            # Test the safety removing each element in the list
            found = False
            for i in range(len(report)):
                if get_safety(report[:i] + report[i+1:]):
                    found = True
                    break
            if found:
                safe += 1
    return safe


if __name__ == '__main__':
    test_message = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".strip()
    # assert get_part_1_answer(test_message) == 2
    assert get_part_2_answer(test_message) == 4, get_part_2_answer(test_message)
    with open('input.txt') as f:
        message = f.read().strip()
    print(f'Answer for part 1: {get_part_1_answer(message)}')
    print(f'Answer for part 2: {get_part_2_answer(message)}')
