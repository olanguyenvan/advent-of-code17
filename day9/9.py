import re


with open('input.txt', 'r') as f:
    stream = f.read()

pattern_find_exclamation_marks = '!.'
regex_exclamation = re.compile(pattern_find_exclamation_marks)
stream = regex_exclamation.sub('', stream)

number_of_groups = 0
level = 1
garbage = False
start_garbage = False
garbage_length = 0
for s in stream:
    if garbage:
        if s == '>':
            garbage = False
        else:
            garbage_length += 1
    else:
        if s == '{':
            number_of_groups += level * 1
            level += 1
        if s == '}':
            level += -1
        if s == '<':
            garbage = True
            start_garbage = True

print("Score is %s. \nThe total length of garbage is %s" % (number_of_groups, garbage_length))
