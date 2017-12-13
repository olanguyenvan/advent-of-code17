def count_jumps(maze_length, jump_offsets):
    jump_counts = 0
    index = 0
    while True:
        jump_counts += 1
        jump_step = jump_offsets[index]
        jump_offsets[index] += 1

        index += jump_step
        if index < 0 or index >= maze_length:
            return jump_counts


if __name__ == '__main__':
    with open('input.txt') as fd:
        jump_offsets_from_input = fd.read().splitlines()
        jump_offsets_from_input = list(map(lambda x: int(x), jump_offsets_from_input))

    test_jump_offsets = [0, 3, 0, 1, -3]
    print(count_jumps(len(test_jump_offsets), test_jump_offsets))
    print(count_jumps(len(jump_offsets_from_input), jump_offsets_from_input))
