import math


def find_steps_count_from(n):
    inner_square_length = math.sqrt(n) // 1
    if inner_square_length % 2 == 0:
        inner_square_length += - 1

    diff = n - inner_square_length ** 2
    if diff == 0:
        return inner_square_length - 1

    steps_in_side_to_pass = diff % (inner_square_length + 1)
    return inner_square_length // 2 + 1 + math.fabs(inner_square_length // 2 + 1 - steps_in_side_to_pass)


if __name__ == '__main__':
    print(find_steps_count_from(312051))
