""" 用嵌套的 Python list 实现二叉树，用这种二叉树实现算术表达式和计算
"""


def BinTree(data, left=None, right=None):
    return [data, left, right]


def is_empty_BinTree(btree):
    return btree is None


def root(btree):
    return btree[0]


def left(btree):
    return btree[1]


def right(btree):
    return btree[2]


def set_root(btree, data):
    btree[0] = data


def set_left(btree, left):
    btree[1] = left


def set_right(btree, right):
    btree[2] = right

###############################################
#### Functions for ############################
#### building and manipulating ################
#### mathematical expressions  ################


def make_sum(a, b):
    return ('+', a, b)


def make_prod(a, b):
    return ('*', a, b)


def make_diff(a, b):
    return ('-', a, b)


def make_div(a, b):
    return ('/', a, b)


def is_basic_exp(a):
    return not isinstance(a, tuple)


def is_compose_exp(a):
    return isinstance(a, tuple)


def eval_exp(e):
    if is_basic_exp(e):
        return e
    op, a, b = e[0], eval_exp(e[1]), eval_exp(e[2])
    if op == '+':
        return eval_sum(a, b)
    elif op == '-':
        return eval_diff(a, b)
    elif op == '*':
        return eval_prod(a, b)
    elif op == '/':
        return eval_div(a, b)
    else:
        raise ValueError("Unknown operator:", op)


def is_number(x):
    return (isinstance(x, int) or isinstance(x, float) or
            isinstance(x, complex))


def eval_sum(a, b):
    if is_number(a) and is_number(b):
        return a + b
    if is_number(a) and a == 0:
        return b
    if is_number(b) and b == 0:
        return a
    return make_sum(a, b)


def eval_diff(a, b):
    if is_number(a) and is_number(b):
        return a - b
    if is_number(a) and a == 0:
        return -b
    if is_number(b) and b == 0:
        return a
    return make_diff(a, b)


def eval_prod(a, b):
    if is_number(a) and is_number(b):
        return a * b
    if is_number(a) and a == 0 or is_number(b) and b == 0:
            return 0
    if is_number(a) and a == 1:
        return b
    if is_number(b) and b == 1:
        return a
    return make_prod(a, b)


def eval_div(a, b):
    if is_number(a) and is_number(b):
        return a / b
    if is_number(a) and a == 0:
        return 0
    if is_number(b) and b == 0:
        raise ZeroDivisionError
    if is_number(b) and b == 1:
        return a
    return make_div(a, b)
    
   
if __name__ == '__main__':
##    t1 = btree(2, btree(4, [], []), btree(8, [], []))
##    print(t1)
##    set_leftch(leftch(t1), btree(5, [], []))
##    print(t1)

    e1 = make_prod(make_sum(2, 3), make_diff(4, 5))
    e2 = make_prod(make_diff(make_prod(2, 'a'), 3), make_diff(4, 5))
    e3 = make_div(make_sum(make_prod(2, 7), make_div(0, 'b')), make_div('a', 1))

#    eval_exp(['$', 2, 3]) # This will cause an exception because $ is not a valid operator
