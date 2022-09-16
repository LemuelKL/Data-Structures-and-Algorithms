# check, for every word, if it is a prefix of another word W.
# if it is, then it is a bad set, and print W.
# if multiple of so W exist, print the first one.
# if not, then it is a good set.

# this solution implements a trie


class Node:
    def __init__(self, ch, children):
        self.ch = ch
        self.children = children
        self.end = False


root = Node(None, [])


def add2Tree(word):
    l = len(word)
    idx = 0
    node = root
    while idx < l:
        next_node = None
        for child in node.children:
            if child.ch == word[idx]:
                next_node = child
                break

        if next_node:
            node = next_node
        else:
            next_node = Node(word[idx], [])
            node.children.append(next_node)
            node = next_node

        idx += 1

    node.end = True


def checkWord(word):
    node = root
    for c in word:
        next_node = None
        for child in node.children:
            if child.ch == c:
                next_node = child
                break
        if next_node:
            if next_node.end:
                return False
            node = next_node
            continue
        else:
            return True


def noPrefix(words):
    for w in words:
        if not checkWord(w):
            print("BAD SET")
            print(w)
            return
        add2Tree(w)

    print("GOOD SET")


if __name__ == "__main__":
    noPrefix(["aab", "defgab", "abcde", "aabcde", "bbbbbbbbbb", "jabjjjad"])
