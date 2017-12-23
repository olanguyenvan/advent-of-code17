import re
from collections import defaultdict


list_of_names = []

comparisons = {
    '<': lambda a, b: a < b,
    '>': lambda a, b: a > b,
    '==': lambda a, b: a == b,
    '>=': lambda a, b: a >= b,
    '<=': lambda a, b: a <= b,
    '!=': lambda a, b: a != b,
}

if __name__ == '__main__':
    with open('input.txt') as fd:
        instructions = fd.read().splitlines()

        pattern = '(?P<register>([a-z])*)\s(?P<dec_or_inc>inc|dec|)\s(?P<value_to_change>-?\d*)' + \
                  '\sif\s(?P<cond_register>([a-z])*)\s(?P<cond_type>>|<|>=|<=|==|!=)\s(?P<cond_value>-?\d*)'

    registers = defaultdict(lambda: 0)

    tmp_max = 0
    for instruction in instructions:
        result = re.match(pattern, instruction)
        if comparisons[result.group('cond_type')](registers[result.group("cond_register")], int(result.group("cond_value"))):
            value = int(result.group('value_to_change'))
            registers[result.group("register")] += value if result.group("dec_or_inc") == 'inc' else -value
            tmp_max = max(tmp_max, registers[result.group("register")])
        
    print("The maximum value after all instructions is %s" % max(registers.values()))
    print("The maximum value in between instructions was %s" % tmp_max)
