from collections import Counter

with open("input_small.txt", "r") as input_file:
    lines = input_file.read().strip().split("\n")

template_dict = {
    (l[0], l[1]): r for l, r in (l.split(" -> ") for l in lines if "->" in l)
}


class Node:
    def __init__(self, right, char):
        self.right = right
        self.char = char

    def get_as_iter(self):
        node = self
        while node is not None:
            yield node.char
            node = node.right

    def get_as_iter_nodes(self):
        node = self
        while node is not None:
            yield node
            node = node.right

    def get_len(self):
        return sum(1 for _ in self.get_as_iter())

    def count_char(self, char):
        return sum(1 for c in self.get_as_iter() if c == char)

    def print(self):
        print("".join(self.get_as_iter()))


def get_polymer_from_str(polymer_str):
    polymer_start = Node(None, polymer_str[0])
    current = polymer_start
    for c in polymer_str[1:]:
        node = Node(None, c)
        current.right = node
        current = node
    return polymer_start


def iterate(polymer):
    node = polymer
    while node.right is not None:
        pair = node.char, node.right.char
        new_char = template_dict[pair]
        new_node = Node(node.right, new_char)
        next_node = node.right
        node.right = new_node
        node = next_node


def print_counts(polymer):
    counter = Counter(polymer.get_as_iter())
    most = counter.most_common()[0]
    least = counter.most_common()[-1]
    print({most[0]: most[1], least[0]: least[1]})


def iterate_x(polymer, x):
    print(f"Iteration 0 done, length: {polymer.get_len()}")
    previous = 1
    for i in range(1, x + 1):
        iterate(polymer)
        print(f"Iteration {i} done, length: {polymer.get_len()}")
        current = polymer.count_char('S')
        if previous != 0:
            print(current/previous)
        previous = current
        # print_counts(polymer)


# all_letters = set(item for pair in template_dict.keys() for item in pair)
# print(all_letters)

polymer = get_polymer_from_str("NNCB")

iterate_x(polymer, 20)

# pairs = set(
#     (n.char, n.right.char) for n in polymer.get_as_iter_nodes() if n.right is not None
# )
# print(pairs)
# print(len(pairs))
