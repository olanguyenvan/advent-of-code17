def find_lines_with_no_anagrams(lines):
    s = 0
    for line in lines:
        sorted_words = list(''.join(sorted(word)) for word in line)
        if len(line) == len(set(sorted_words)):
            s += 1
    return s

if __name__ == '__main__':
    with open('input.txt') as fd:
        not_stripped_lines = fd.read().splitlines()
        stripped_lines = [t.split(' ') for t in not_stripped_lines]
        print(find_lines_with_no_anagrams(stripped_lines))
