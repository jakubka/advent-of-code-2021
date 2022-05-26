# target area: x=281..311, y=-74..-54
# target area: x=20..30, y=-10..-5

import pprint
import math
from collections import defaultdict
from itertools import product


target_x_from = 281
target_x_to = 311
target_y_from = -54
target_y_to = -74


def get_x_stop(velocity):
    return int((velocity + 1) * velocity / 2)


def get_min_x_velocity(target_x_from):
    first_try = math.ceil(math.sqrt(target_x_to))
    return next(
        v for v in range(first_try, first_try + 100) if get_x_stop(v) >= target_x_from
    )


def get_distance_after_steps_x(velocity, steps):
    return int((velocity + max(velocity - steps, 0) + 1) * min(steps, velocity) / 2)


def get_distance_after_steps_y(velocity, steps):
    if velocity > 0:
        if steps < velocity * 2 + 1:
            raise Exception("unsupported")
        remaining_steps_below_y = steps - (velocity * 2 + 1)
        return -int(
            (velocity + 1 + velocity + remaining_steps_below_y)
            * remaining_steps_below_y
            / 2
        )
    elif velocity <= 0:
        return int((velocity + (velocity - steps + 1)) * steps / 2)


min_x_velocity = get_min_x_velocity(target_x_from)

max_y_velocity = -target_y_to - 1
max_steps = max_y_velocity * 2 + 1 + 1

# print(get_min_x_velocity(281))
# print(get_x_stop(25))
# print(get_distance_after_steps_x(10, 3))


possibilities_for_steps_x = defaultdict(list)

for v in range(min_x_velocity, target_x_to + 1):
    for steps in range(1, max_steps + 1):
        distance = get_distance_after_steps_x(v, steps)
        if distance <= target_x_to and distance >= target_x_from:
            possibilities_for_steps_x[steps].append(v)

possibilities_for_steps_y = defaultdict(list)

for v in range(target_y_to, max_y_velocity + 1):
    for steps in range(1, max_steps + 1):
        if steps < v * 2 + 1:
            continue
        distance = get_distance_after_steps_y(v, steps)
        if distance >= target_y_to and distance <= target_y_from:
            possibilities_for_steps_y[steps].append(v)
pprint.pprint(possibilities_for_steps_x)
pprint.pprint(possibilities_for_steps_y)

products = [
    (i, list(product(possibilities_for_steps_x[i], possibilities_for_steps_y[i])))
    for i in range(1, max_steps + 1)
]
pprint.pprint(products)

print("-----")
for i, pairs in products:
    for pair in sorted(pairs):
        print(pair)
print("-----")
print(sum(len(pairs) for i, pairs in products))
all_pairs = {pair for i, pairs in products for pair in pairs}
print(len(all_pairs))


def test_1():
    print(get_distance_after_steps_y(100, 205) == 101 + 102 + 103 + 104)
    print(get_distance_after_steps_y(100, 205))


def test_2():
    print(get_distance_after_steps_y(-5, 4) == -5 + -6 + -7 + -8)
    print(get_distance_after_steps_y(-5, 10))


def test_3():
    print(get_distance_after_steps_y(0, 4) == 0 + -1 + -2 + -3)
    print(get_distance_after_steps_y(0, 4))


# test_1()
# test_2()
# test_3()
