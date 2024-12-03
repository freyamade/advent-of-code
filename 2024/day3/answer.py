import re
PART_1_PATTERN = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
PART_2_PATTERN = re.compile(r"(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))")


def get_part_1_answer(input: str) -> int:
    total = 0
    for a, b in PART_1_PATTERN.findall(input):
        total += int(a) * int(b)
    return total


def get_part_2_answer(input: str) -> int:
    total = 0
    enabled = True
    for mul, do, dont in PART_2_PATTERN.findall(input):
        if do:
            enabled = True
        if dont:
            enabled = False
        if mul:
            if not enabled:
                continue
            match = PART_1_PATTERN.match(mul)
            a = int(match.group(1))
            b = int(match.group(2))
            total += a * b
    return total


if __name__ == '__main__':
    assert get_part_1_answer('xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))') == 161
    assert get_part_2_answer("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))") == 48
    with open('input.txt') as f:
        message = f.read().strip()
    print(f'Answer for part 1: {get_part_1_answer(message)}')
    print(f'Answer for part 2: {get_part_2_answer(message)}')

