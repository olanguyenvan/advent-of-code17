def count_steps_until_redistribution_loop(memory_banks_int):
    redistribution_steps = 0
    cached_states = []

    def add_to_cache(bank_states):
        str_bank_states = list(map(lambda i: str(i), bank_states))
        concatenated_bank_state = ';'.join(str_bank_states)
        if concatenated_bank_state in cached_states:
            print('seen again after %s steps' % (len(cached_states) - cached_states.index(concatenated_bank_state)))
            return True
        cached_states.append(concatenated_bank_state)

    while True:
        redistribution_steps += 1

        value_to_distribute = max(memory_banks_int)
        index_of_value_to_distribute = memory_banks_int.index(value_to_distribute)
        memory_banks_int[index_of_value_to_distribute] = 0

        index_to_increment = (index_of_value_to_distribute + 1) % len(memory_banks_int)

        while value_to_distribute > 0:
            memory_banks_int[index_to_increment] += 1
            index_to_increment = (index_to_increment + 1) % len(memory_banks_int)
            value_to_distribute += -1

        if add_to_cache(memory_banks_int):
            return redistribution_steps


if __name__ == '__main__':
    with open('input.txt') as fd:
        memory_banks_str = fd.read().replace('\n', '').split('\t')
    memory_banks_int = list(map(lambda s: int(s), memory_banks_str))
    print(count_steps_until_redistribution_loop(memory_banks_int))
