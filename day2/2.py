def find_sum_of_max_diffs():
    with open('input.txt') as fd:
        not_stripped_lines = fd.readlines()
        lines = [list(map(lambda x: int(x), t.split('\n')[0].split('\t'))) for t in not_stripped_lines]

    s = 0
    for line in lines:
        s += max(line) - min(line)
    return s

if __name__ == '__main__':
    print(find_sum_of_max_diffs())
