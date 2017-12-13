def find_lines_with_no_repetitions(lines):
    s = 0
    for line in lines:
        if len(line) == len(set(line)):
            s += 1
    return s

if __name__ == '__main__':
    with open('input.txt') as fd:
        not_stripped_lines = fd.read().splitlines()
        stripped_lines = [t.split(' ') for t in not_stripped_lines]
        print(find_lines_with_no_repetitions(stripped_lines))
