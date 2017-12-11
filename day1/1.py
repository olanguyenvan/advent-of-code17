
def count_repetitions(n):
    n_str = str(n)
    s = 0
    size_of_n = len(n_str)
    for i in range(size_of_n - 1):
        s += int(n_str[i] == n_str[i + 1]) * int(n_str[i])

    s += int(n_str[-1] == n_str[0]) * int(n_str[0])

    return s

if __name__ == '__main__':
    print(count_repetitions(1122))
    print(count_repetitions(1111))
    print(count_repetitions(1234))
    print(count_repetitions(91212129))
    print(count_repetitions(0))

