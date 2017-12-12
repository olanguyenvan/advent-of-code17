import math


def find_steps_count_from(n):

    innser_square_length = math.sqrt(n) // 1
    if innser_square_length % 2 == 0:
        innser_square_length += - 1

    diff = n - innser_square_length * innser_square_length
    if diff == 0:
        return innser_square_length - 1

    steps_in_side_to_pass = diff % (innser_square_length + 1)
    return innser_square_length // 2 + 1 + math.fabs(innser_square_length // 2 + 1 - steps_in_side_to_pass)

if __name__ == '__main__':
    print(find_steps_count_from(312051))
