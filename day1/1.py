
def count_repetitions(n_str, get_index_to_compare):
    s = 0
    size_of_n = len(n_str)
    for i in range(size_of_n):
        s += int(n_str[i] == n_str[get_index_to_compare(i)]) * int(n_str[i])

    return s


def get_index_after_half_length(size_of_n):
    return lambda index: index - size_of_n // 2


if __name__ == '__main__':
    with open('input.txt') as fd:
        n = fd.readline().replace('\n', '')

    print(count_repetitions(n, lambda index: index - 1))
    print(count_repetitions(n, get_index_after_half_length(len(n))))

