""" 树实现为嵌套的 Python list
"""


class SubtreeIndexError(ValueError):
    pass


def Tree(data, *subtrees):
    return [data].extend(subtrees)


def is_empty_Tree(tree):
    return tree is None


def root(tree):
    return tree[0]


def subtree(tree, i):
    if i < 1 or i > len(tree):
        raise SubtreeIndexError
    return tree[i + 1]


def set_root(tree, data):
    tree[0] = data


def set_subtree(tree, i, subtree):
    if i < 1 or i > len(tree):
        raise SubtreeIndexError
    tree[i+1] = subtree



if __name__ == '__main__':
    tree1 = Tree('+', 1, 2, 3)
    tree2 = Tree('*', tree1, 6, 8)

    print(tree1)
    print(tree2)

