from collections import defaultdict


def generate_order_mapping(input: str) -> dict[str, list[str]]:
    order_mapping = defaultdict(list)
    for line in input.split('\n'):
        if '|' not in line:
            continue
        page, required = line.split('|')
        order_mapping[page].append(required)
    return order_mapping


def is_valid(order_mapping: dict[str, list[str]], pages: list[str]) -> bool:
    for index in range(len(pages)):
        for back_index in (range(index - 1, -1, -1)):
            if pages[back_index] in order_mapping[pages[index]]:
                return False
    return True


def get_part_1_answer(input: str) -> int:
    order_mapping = generate_order_mapping(input)
    valid_updates = []
    for line in input.split('\n'):
        if ',' not in line:
            continue
        pages = line.split(',')
        if is_valid(order_mapping, pages):
            valid_updates.append(pages)
    output = 0
    for update in valid_updates:
        output += int(update[len(update) // 2])
    return output


def get_part_2_answer(input: str) -> int:
    order_mapping = generate_order_mapping(input)
    invalid_updates = []
    for line in input.split('\n'):
        if ',' not in line:
            continue
        pages = line.split(',')
        if not is_valid(order_mapping, pages):
            invalid_updates.append(pages)
    output = 0
    for update in invalid_updates:
        # Fix it first
        while not is_valid(order_mapping, update):
            for index in range(len(update)):
                for back_index in (range(index - 1, -1, -1)):
                    if update[back_index] in order_mapping[update[index]]:
                        update[index], update[back_index] = update[back_index], update[index]
                        break
        print('fixed', update)
        output += int(update[len(update) // 2])
    return output


if __name__ == '__main__':
    test_message = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""".strip()
    assert get_part_1_answer(test_message) == 143
    assert get_part_2_answer(test_message) == 123
    with open('input.txt') as f:
        message = f.read().strip()
    print(f'Answer for part 1: {get_part_1_answer(message)}')
    print(f'Answer for part 2: {get_part_2_answer(message)}')

