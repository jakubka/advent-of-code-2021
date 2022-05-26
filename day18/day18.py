from pprint import pprint
from math import ceil


def debug(txt):
    if False:
        print(txt)


class Node:
    def __init__(self, left_or_number, right=None) -> None:
        if right is not None:
            self.left = left_or_number
            self.right = right
            self.number = None
        else:
            self.left = None
            self.right = None
            self.number = left_or_number

    def is_pair(self):
        return self.number is None

    def is_regular(self):
        return not self.is_pair()

    def split(self):
        if self.is_regular():
            if self.number >= 10:
                debug(f"Spliting {self.visualise()}")
                self.left = Node(int(self.number / 2))
                self.right = Node(int(ceil(self.number / 2)))
                self.number = None
                return True
            return False
        else:
            return self.left.split() or self.right.split()

    def explode(self, current_depth=1):
        if self.is_regular():
            return False
        if current_depth > 4 and self.left.is_regular() and self.right.is_regular():
            debug(f"Exploding {self.visualise()}")
            r = {
                "add_left": self.left.number,
                "add_right": self.right.number,
            }
            self.number = 0
            self.left = self.right = None
            return r
        r = self.left.explode(current_depth + 1)
        if r is not False:
            if r is True:
                return True
            if "add_right" in r:
                self.right.add_to_leftmost(r["add_right"])
            if "add_left" in r:
                return {"add_left": r["add_left"]}
            return True
        r = self.right.explode(current_depth + 1)
        if r is not False:
            if r is True:
                return True
            if "add_left" in r:
                self.left.add_to_rightmost(r["add_left"])
            if "add_right" in r:
                return {"add_right": r["add_right"]}
            return True
        return False

    def add_to_rightmost(self, n):
        if self.is_regular():
            self.number += n
        else:
            self.right.add_to_rightmost(n)

    def add_to_leftmost(self, n):
        if self.is_regular():
            self.number += n
        else:
            self.left.add_to_leftmost(n)

    def get_magnitude(self):
        if self.is_regular():
            return self.number
        return 3 * self.left.get_magnitude() + 2 * self.right.get_magnitude()

    def visualise(self):
        if self.is_regular():
            return self.number
        return f"[{self.left.visualise()},{self.right.visualise()}]"


def add_and_reduce_nodes(left, right):
    new_node = Node(left, right)
    debug(f"After addition: {new_node.visualise()}")
    reduce_all(new_node)
    return new_node


def add_and_reduce_lists(l1, l2):
    return add_and_reduce_nodes(create_node_from_list(l1), create_node_from_list(l2))


def reduce_all(node):
    while True:
        exploded = node.explode() is not False
        if exploded:
            debug(f"After explode: {node.visualise()}")
            pass
        if not exploded:
            if node.split():
                debug(f"After split: {node.visualise()}")
                pass
            else:
                break


def create_node_from_list(list):
    if type(list) == int:
        return Node(list)
    else:
        return Node(create_node_from_list(list[0]), create_node_from_list(list[1]))


def add_lists_to_node(n, lists):
    if len(lists) == 0:
        return n
    else:
        new_node = add_and_reduce_nodes(n, create_node_from_list(lists[0]))
        print(f"After addition and reduce: {new_node.visualise()}")
        return add_lists_to_node(new_node, lists[1:])


lists = [
    [[6, [[9, 4], [5, 1]]], [[[6, 5], [9, 4]], 2]],
    [[7, 3], [[3, [5, 5]], 8]],
    [8, [[5, 0], [[0, 2], 3]]],
    [[[8, 7], [[2, 0], [7, 5]]], 1],
    [[[2, [6, 1]], [7, [6, 1]]], [[7, 3], 1]],
    [[2, [9, [0, 0]]], [[[9, 7], 1], 0]],
    [[[[8, 4], [2, 3]], [[6, 4], 4]], 0],
    [[[1, 3], 1], [[3, 8], [[2, 3], [9, 5]]]],
    [[7, [5, 9]], [[7, [9, 1]], [3, [9, 6]]]],
    [[[5, 3], 5], [[[8, 8], [5, 6]], [6, 5]]],
    [3, [[4, 1], 3]],
    [[[5, [2, 0]], [[9, 5], [9, 2]]], [[[1, 7], [6, 9]], [[6, 3], [8, 6]]]],
    [[[[9, 3], [2, 4]], [6, 9]], [[[9, 7], 1], [[1, 9], [2, 9]]]],
    [3, [[6, 1], 8]],
    [[[[8, 8], 8], [[3, 9], [9, 3]]], [[8, 8], [[7, 1], [6, 5]]]],
    [[[8, 9], [[2, 7], 6]], [[[2, 9], [8, 4]], [1, 6]]],
    [[4, [[4, 4], 0]], [[8, [1, 8]], [9, [7, 3]]]],
    [[[[3, 0], [7, 2]], [[9, 5], [9, 5]]], [5, [0, [5, 7]]]],
    [5, [1, [[4, 0], [8, 5]]]],
    [[0, 0], [[[9, 8], 1], [[5, 2], [4, 6]]]],
    [[5, 8], [6, [[5, 2], 1]]],
    [[1, [[1, 4], 8]], 8],
    [[[[1, 7], [7, 1]], [4, [8, 0]]], 0],
    [[[[5, 9], 0], [0, 8]], [2, [[6, 2], 2]]],
    [2, [4, 3]],
    [[[[4, 0], [2, 2]], 7], [[8, 7], [[8, 1], 1]]],
    [[[[6, 0], [1, 6]], [2, [6, 2]]], [[9, 6], [7, [8, 2]]]],
    [[3, 5], [[9, [4, 0]], [[6, 5], [1, 0]]]],
    [[[[6, 0], 7], [8, [0, 1]]], [[7, 6], [[7, 1], [9, 6]]]],
    [[3, [[6, 4], 4]], [0, [[3, 5], [8, 6]]]],
    [[8, [[1, 8], 0]], [1, [[0, 1], [6, 2]]]],
    [[6, [5, [5, 4]]], 9],
    [[[[0, 7], 3], [[7, 7], [1, 2]]], [8, [2, 1]]],
    [[[7, [1, 4]], [5, [9, 8]]], [1, 8]],
    [[[0, 7], [[3, 6], [2, 4]]], [[7, 4], 1]],
    [[[5, [8, 2]], [[4, 9], [5, 3]]], 4],
    [[5, [[3, 3], 0]], 8],
    [7, [2, 1]],
    [[3, 8], [[[5, 3], 8], [[3, 4], 6]]],
    [[[2, [0, 9]], [0, 5]], 0],
    [[6, [7, 6]], [[[2, 6], 2], [[8, 9], 5]]],
    [[[0, 0], [[1, 9], [0, 6]]], [[5, [8, 8]], [[6, 9], [3, 7]]]],
    [[[[4, 6], [8, 4]], [2, [3, 8]]], [8, 0]],
    [[0, 0], [2, [[6, 2], 6]]],
    [[[6, 0], 3], 8],
    [[[[6, 1], [4, 8]], [2, [3, 0]]], 7],
    [[[0, [1, 8]], [[8, 1], 6]], 3],
    [2, [0, 2]],
    [[[[9, 6], 8], [[1, 9], [7, 8]]], [[[0, 6], [8, 8]], [6, [2, 3]]]],
    [[0, [6, [7, 4]]], [[[0, 9], [2, 3]], [[8, 8], 0]]],
    [[[0, 1], [7, [4, 9]]], [[3, 9], 8]],
    [[[1, 9], 7], [[0, 5], [5, [7, 9]]]],
    [[[9, [2, 5]], 2], [7, [1, [7, 7]]]],
    [[[[0, 4], [7, 3]], 2], 5],
    [[8, [7, 4]], [[[8, 2], [7, 3]], [1, [7, 8]]]],
    [[[0, 4], [[3, 7], 9]], 6],
    [[5, [[9, 2], [7, 0]]], [[8, 2], [[1, 4], 9]]],
    [2, [[[9, 6], 9], [2, 3]]],
    [[5, [[3, 5], [3, 8]]], [4, [2, 9]]],
    [[[5, 2], [4, [4, 1]]], [[[1, 0], [8, 7]], [[8, 7], 8]]],
    [[4, [4, [0, 9]]], [[1, 8], 4]],
    [[[3, [4, 0]], [[8, 8], [1, 6]]], [[4, 0], [1, 2]]],
    [[[1, [1, 8]], 2], [[6, 2], [9, [8, 5]]]],
    [9, [[[8, 8], [8, 3]], [3, [1, 3]]]],
    [[[2, [4, 5]], [4, 1]], [1, [[8, 6], [1, 5]]]],
    [[0, [5, [7, 6]]], [[8, 6], [[9, 9], 1]]],
    [[[5, [5, 2]], 2], [[[1, 4], [3, 7]], [4, 3]]],
    [[5, [[9, 8], 0]], [7, [[0, 8], [7, 8]]]],
    [[[[8, 0], 6], [2, 1]], [[[6, 3], [3, 1]], [[7, 6], [7, 2]]]],
    [[[3, 3], 6], [2, [[8, 4], 5]]],
    [[[6, [5, 3]], [[6, 4], 3]], [[[4, 8], 0], [[0, 6], [1, 4]]]],
    [[[3, [6, 4]], 2], [[[8, 8], 4], [[8, 6], 6]]],
    [[[[6, 9], 1], [3, 8]], [[5, [4, 6]], 2]],
    [[5, 6], 3],
    [[[5, [8, 6]], [[4, 2], [1, 1]]], [[[0, 7], [6, 3]], [9, [7, 7]]]],
    [[7, [[4, 0], 6]], [[4, [6, 4]], 8]],
    [[5, [[2, 0], [9, 4]]], [[[4, 6], 1], [[2, 8], [8, 5]]]],
    [[[[3, 5], [0, 4]], [[5, 0], 3]], [[1, [8, 9]], 7]],
    [[[[6, 6], 6], [[6, 6], [4, 3]]], 0],
    [[5, [2, 5]], [6, [[7, 8], 2]]],
    [[[7, [5, 5]], [[7, 4], [6, 7]]], 0],
    [[[3, 3], 3], [[1, 9], [0, [9, 2]]]],
    [[9, [4, 1]], [6, [2, [9, 6]]]],
    [[4, 7], [9, [3, 0]]],
    [[[8, 2], [[9, 8], [4, 2]]], [[2, [3, 7]], [7, [3, 1]]]],
    [[[[1, 8], 2], [0, [6, 5]]], [[[2, 7], [8, 6]], [[8, 9], [8, 5]]]],
    [[[7, [2, 9]], [9, 0]], 5],
    [[5, [2, [1, 5]]], [0, 7]],
    [4, [[0, [0, 3]], [[0, 5], [9, 0]]]],
    [0, [[4, 4], [[8, 4], [3, 8]]]],
    [[[[4, 9], 0], [[4, 4], 9]], [[[6, 1], [8, 9]], [7, [2, 3]]]],
    [[[[4, 2], [7, 4]], 0], [[5, [0, 6]], [[0, 5], 4]]],
    [[[1, 0], 8], [[[2, 8], [2, 9]], 3]],
    [[6, [1, [9, 9]]], [2, 2]],
    [[[8, [6, 7]], [6, [6, 6]]], [[[2, 3], 5], 0]],
    [[[7, [6, 9]], [[7, 8], [2, 8]]], [[4, [5, 1]], 5]],
    [[[[6, 3], [1, 4]], 7], [[9, 1], [3, 1]]],
    [5, [[8, 5], [[7, 5], 4]]],
    [[4, [[4, 0], 0]], [6, [1, 1]]],
    [[[5, [9, 2]], [9, 0]], [[5, [5, 7]], 4]],
]
n = add_lists_to_node(create_node_from_list(lists[0]), lists[1:])
# n = add_and_reduce_lists(lists[0], lists[1])
print(n.visualise())
print(f"Magni {n.get_magnitude()}")
