def get_part_1_answer(input: str) -> int:
    return 0


def get_part_2_answer(input: str) -> int:
    return 0


if __name__ == '__main__':
    with open('input.txt') as f:
        message = f.read().strip()
    print(f'Answer for part 1: {get_part_1_answer(message)}')
    print(f'Answer for part 2: {get_part_2_answer(message)}')

