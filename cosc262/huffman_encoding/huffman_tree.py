import heapq

class HuffmanTree:
    def __init__(self, root=None):
        self.root = root

    def build_from_freqs(self, freqs):
        priority_queue = []

        for key, freq in freqs.items():
            leaf = Leaf(key, freq)
            heapq.heappush(priority_queue, leaf)

        while len(priority_queue) > 1:
            left = heapq.heappop(priority_queue)
            right = heapq.heappop(priority_queue)

            node = Node(left, right)
            heapq.heappush(priority_queue, node)

        self.root = heapq.heappop(priority_queue)

    def encode(self, string):
        keys = recursive_encode(self.root)
        map_dict = {}

        for char, map in keys:
            map_dict[char] = map

        encoded_string = ""
        for ch in string:
            encoded_string += map_dict[ch]
        return encoded_string

    def decode(self, encoded_string):
        node = self.root
        decoded_string = ""
        for ch in encoded_string:
            if ch == "0":
                node = node.left
            else:
                node = node.right

            if type(node) == Leaf:
                decoded_string += node.char
                node = self.root

        return decoded_string


    def __repr__(self):
        return repr(self.root)

class Node:
    def __init__(self, left, right):
        self.leaf = False
        self.freq = left.get_freq() + right.get_freq()
        self.left = left
        self.right = right
        self.min_char = min(left.min_char, right.min_char)

    def get_freq(self):
        return self.freq

    def is_leaf(self):
        return self.leaf

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.min_char < other.min_char

        return self.freq < other.freq

    def __repr__(self, indent=0):
        return "  " * indent + f"Node({self.freq}," + "\n" + \
                self.left.__repr__(indent+1) + "," + "\n" + \
                self.right.__repr__(indent + 1) + ")"

class Leaf:
    def __init__(self, freq, char):
        self.leaf = True
        self.char = char
        self.min_char = char
        self.freq = freq

    def is_leaf(self):
        return self.leaf

    def get_freq(self):
        return self.freq

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.min_char < other.min_char

        return self.freq < other.freq

    def __repr__(self, indent=0):
        return "  " * indent + f"Leaf({self.freq}, '{self.char}')"

def recursive_encode(tree, current_string = ''):
    if tree.is_leaf():
        return [(tree.char, current_string)]
    else:
        return [] + recursive_encode(tree.left, current_string = current_string + '0') + recursive_encode(tree.right, current_string = current_string + '1')