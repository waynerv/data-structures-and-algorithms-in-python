""" 栈的应用1：检查括号配对，后缀表达式求值器，
中缀表达式到后缀表达式的转换，
"""

from stack_list import *


class ESStack(SStack):
    def depth(self):
        return len(self._elems)


#############################################
######## Parentheses checker #################

def check_parens(text):
    parens = "()[]{}"
    open_parens = "([{"
    opposite = {')': '(', ']': '[', '}': '{'}

    def parentheses(text):
        i, text_len = 0, len(text)
        while True:
            while i < text_len and text[i] not in parens:
                i += 1
            if i >= text_len:
                return
            yield text[i], i
            i += 1
    
    st = SStack()
    for pr, i in parentheses(text):
        if pr in open_parens:  # push open pares into stack
            st.push(pr)
        elif st.pop() != opposite[pr]:
            print("Unmatching is found at", i, "for", pr)
            return False

    print("All parentheses are correctly matched.")
    return True


################################################
####### Suffix expression evaluator ############
def suffix_exp_evaluator(line):
    return suf_exp_evaluator(line.split())


def suf_exp_evaluator(exp):
    """exp is a list of items representing a suffix expression.
    This function evaluates it and return its value.
    """
    operators = "+-*/" 
    st = ESStack()

    for x in exp:
        if x not in operators:
            st.push(float(x))
            continue
        if st.depth() < 2: 
            raise SyntaxError("Short of operand(s).")
        a = st.pop()  # second argument
        b = st.pop()  # first argument
        if x == '+':
            c = b + a
        elif x == '-':
            c = b - a
        elif x == '*':
            c = b * a
        elif x == '/':  # may raise ZeroDivisionError
            c = b / a
        else:
            break
        # the else branch is not possible
        st.push(c)

    if st.depth() == 1:
        return st.pop()
    raise SyntaxError("Extra operand(s).")
# end suf_exp_evaluator


def suffix_exp_calculator():
    """Repeatly ask for expression input until an 'end'."""
    while True:
        try:
            line = input("Suffix Expression: ")
            if line == "end":
                return
            res = suffix_exp_evaluator(line)
            print(res)
        except Exception as ex:
            print("Error:", type(ex), ex.args)


def demo_suffix():
    print(suffix_exp_evaluator("1"))
    print(suffix_exp_evaluator("1 2 +"))
    print(suffix_exp_evaluator("1 3 + 2 *"))
    print(suffix_exp_evaluator("1 3 + 2 5 - *"))


#####################################################
##### Transform infix expression to suffix expression

priority = {'(': 1, '+': 3, '-': 3, '*': 5, '/': 5}
infix_operators = "+-*/()"


def tokens(line):
    """ 生成器函数，逐一生成 line 中的一个个单词。单词是一个浮点数或一个运算符。
    本函数只能处理二元运算符，不能处理一元运算符，也不能处理带符号的浮点数。 """
    i, llen = 0, len(line)
    while i < llen:
        while line[i].isspace():
            i += 1
        if i >= llen:
            break
        if line[i] in infix_operators:  # 运算符的情况
            yield line[i]
            i += 1
            continue

        j = i + 1  # 下面处理运算对象

        while (j < llen and not line[j].isspace() and
               line[j] not in infix_operators):
            if ((line[j] == 'e' or line[j] == 'E')  # 处理负指数
                  and j+1 < llen and line[j+1] == '-'):
                j += 1
            j += 1

        yield line[i:j]  # 生成运算对象子串
        i = j


def trans_infix_suffix(line):
    st = SStack()
    exp = []

    for x in tokens(line):  # tokens是一个待定义的生成器
        if x not in infix_operators:  # 运算对象直接送出
            exp.append(x)
        elif st.is_empty() or x == '(':  # 左括号进栈
            st.push(x)
        elif x == ')':  # 处理右括号的分支
            while not st.is_empty() and st.top() != '(':
                exp.append(st.pop())
            if st.is_empty():  # 没找到左括号，就是不配对
                raise SyntaxError("Missing '('.")
            st.pop()  # 弹出左括号，右括号也不进栈
        else:  # 处理算术运算符，运算符都看作是左结合
            while (not st.is_empty() and
                   priority[st.top()] >= priority[x]):
                exp.append(st.pop())
            st.push(x)  # 算术运算符进栈

    while not st.is_empty():  # 送出栈里剩下的运算符
        if st.top() == '(':   # 如果还有左括号，就是不配对
            raise SyntaxError("Extra '('.")
        exp.append(st.pop())

    return exp


# def trans_infix_suffix(line):
#     st = SStack()
#     exp = []
#     for x in tokens(line):
#         if x not in infix_operators:
#             exp.append(x)
#         elif st.is_empty() or x == '(':
#             st.push(x)
#         elif x == ')':
#             while not st.is_empty() and st.top() != '(':
#                 exp.append(st.pop())
#             if st.is_empty():
#                 raise SyntaxError("Missing '('.")
#             st.pop()  # discard left parenthesis
#         else:  # consider all ops left-associative
#             while (not st.is_empty() and
#                    priority[st.top()] >= priority[x]):
#                 exp.append(st.pop())
#             st.push(x)
#
#     while not st.is_empty():
#         if st.top() == '(':
#             raise SyntaxError("Extra '('.")
#         exp.append(st.pop())
#     return exp


def test_trans_infix_suffix(s):
    print(s)
    print(trans_infix_suffix(s))
    print("Value:", suf_exp_evaluator(trans_infix_suffix(s)))


def demo_trans():
    test_trans_infix_suffix("1.25")
    test_trans_infix_suffix("1 + 2")
    test_trans_infix_suffix("1 + 2 - 3")
    test_trans_infix_suffix("1 + 2 * 3")
    test_trans_infix_suffix("7. / 2 * 3")
    test_trans_infix_suffix("7.e-2/3*2")
    test_trans_infix_suffix("7.0e1/3*2e3")
    test_trans_infix_suffix("(1 + 2) * 3")
    test_trans_infix_suffix("1 + 2 * 3 - 5")
    test_trans_infix_suffix("13 + 2 * (3 - 5)")
    test_trans_infix_suffix("(1 + 2) * (3 - 5)")
    test_trans_infix_suffix("(1 + (2 * 3 - 5)) / 1.25")


if __name__ == "__main__":

    demo_trans()
    
##    check_parens("")
##    check_parens("()")
##    check_parens("([]{})")
##    check_parens("([]{}]")
##    check_parens("(abbvbb[hhh]jhg{lkii288}9000)000fhjsh")
##    check_parens("jkdsjckd(mfkk[fdjjfk],,,{kckjfc}jskdjkc]kkk")

##    suffix_exp_calculator()

    pass
