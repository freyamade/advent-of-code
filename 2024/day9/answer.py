import re


def expand_memory(input: str) -> list:
    """
    Turn a dense memory string into a string indicating the files and free spaces
    """
    file_id = 0
    is_file = True
    memory = []
    for char in input.strip():
        block_size = int(char)
        if is_file:
            is_file = False
            memory += [file_id] * block_size
            file_id += 1
        else:
            is_file = True
            memory += ['.'] * block_size
    return memory


def find_first_file_block(memory: list) -> int:
    index = len(memory) - 1
    while index >= 0:
        if memory[index] != '.':
            return index
        index -= 1
    return -1


def find_first_specific_file_block(memory: list, file_id: str) -> int:
    index = 0
    while index < len(memory):
        if memory[index] == file_id:
            return index
        index += 1
    return -1


def find_first_free_block(memory: list) -> int:
    index = 0
    while index < len(memory):
        if memory[index] == '.':
            return index
        index += 1
    return -1


def find_first_free_block_of_size(memory: list, size: int) -> dict:
    for i in range(len(memory) - size):
        if memory[i:i+size] == ['.'] * size:
            return i
    return -1


def get_length_of_block(memory: list, starting_index: int) -> int:
    item = memory[starting_index]
    size = 0
    for i in range(starting_index, len(memory)):
        if memory[i] != item:
            break
        size += 1
    return size


def condense_memory(memory: list):
    while len(list(filter(lambda s: s != '', ''.join(str(x) for x in memory).split('.')))) > 1:
        # Find first non-empty space at end of memory and first empty space from start
        file_index = find_first_file_block(memory)
        free_index = find_first_free_block(memory)
        file_id = memory[file_index]
        memory[free_index] = file_id
        memory[file_index] = '.'
    return memory


def condense_memory_by_files(memory: list):
    files = set(memory) - {'.'}
    files = sorted(files, reverse=True)
    for file_id in files:
        # Find the first block on the end and see how long it is
        file_index = find_first_specific_file_block(memory, file_id)
        block_size = get_length_of_block(memory, file_index)
        empty_block_index = find_first_free_block_of_size(memory, block_size)
        # If we can't find a block, or the block is to the right
        if empty_block_index == -1 or empty_block_index > file_index:
            continue

        # Otherwise make the swaps
        for i in range(block_size):
            empty_block_space = empty_block_index + i
            file_space = file_index + i
            memory[empty_block_space] = file_id
            memory[file_space] = '.'
    return memory


def get_part_1_answer(input: str) -> int:
    memory = condense_memory(expand_memory(input))
    checksum = 0
    for i in range(len(memory)):
        if memory[i] == '.':
            continue
        checksum += i * memory[i]
    return checksum


def get_part_2_answer(input: str) -> int:
    memory = condense_memory_by_files(expand_memory(input))
    checksum = 0
    for i in range(len(memory)):
        if memory[i] == '.':
            continue
        checksum += i * memory[i]
    return checksum


if __name__ == '__main__':
    test1 = '12345'
    test2 = '2333133121414131402'
    assert expand_memory(test1) == list(map(lambda x: int(x) if x != '.' else x, '0..111....22222'))
    assert expand_memory(test2) == list(map(lambda x: int(x) if x != '.' else x, '00...111...2...333.44.5555.6666.777.888899'))
    assert condense_memory(expand_memory(test1)) == list(map(lambda x: int(x) if x != '.' else x, '022111222......'))
    assert condense_memory(expand_memory(test2)) == list(map(lambda x: int(x) if x != '.' else x, '0099811188827773336446555566..............'))
    assert condense_memory_by_files(expand_memory(test2)) == list(map(lambda x: int(x) if x != '.' else x, '00992111777.44.333....5555.6666.....8888..'))
    assert get_part_1_answer(test2) == 1928
    assert get_part_2_answer(test2) == 2858

    with open('input.txt') as f:
        message = f.read().strip()
    print(f'Answer for part 1: {get_part_1_answer(message)}')
    print(f'Answer for part 2: {get_part_2_answer(message)}')

