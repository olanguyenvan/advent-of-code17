d = {0: {
    0: 1
}}


indexes = {
    'x': 1,
    'y': 0,
}


def is_there_something_on_the_left():
    y_values = d.get(indexes['x'] - 1, False)
    return y_values and y_values.get(indexes['y'], False)


def is_there_something_on_the_right():
    y_values = d.get(indexes['x'] + 1, False)
    return y_values and y_values.get(indexes['y'], False)


def is_there_something_down():
    y_values = d.get(indexes['x'], False)
    return y_values and y_values.get(indexes['y'] - 1, False)


def is_there_something_up():
    y_values = d.get(indexes['x'], False)
    return y_values and y_values.get(indexes['y'] + 1, False)


neighbours_indexes = [
    lambda x, y:  (x - 1, y - 1),
    lambda x, y:  (x - 1, y ),
    lambda x, y:  (x - 1, y + 1),
    lambda x, y:  (x, y + 1),
    lambda x, y:  (x, y - 1),
    lambda x, y:  (x + 1, y - 1),
    lambda x, y:  (x + 1, y),
    lambda x, y:  (x + 1, y + 1),
]


def get_sum_of_neighbours():
    s = 0
    for n_i in neighbours_indexes:
        x, y = n_i(indexes['x'], indexes['y'])
        try:
            s += d[x][y]
        except KeyError:
            pass
    return s


sum_of_neighbours = 0
while sum_of_neighbours <= 312051:
    y_values = d.get(indexes['x'], None)
    if not y_values:
        d[indexes['x']] = {}
        y_values = d[indexes['x']]

    sum_of_neighbours = get_sum_of_neighbours()
    y_values[indexes['y']] = sum_of_neighbours

    if is_there_something_on_the_left() and not is_there_something_up():
        indexes['y'] += 1
    elif not is_there_something_on_the_left() and is_there_something_down():
        indexes['x'] += -1
    elif is_there_something_on_the_right() and not is_there_something_down():
        indexes['y'] += -1
    else:
        indexes['x'] += 1

print(sum_of_neighbours)