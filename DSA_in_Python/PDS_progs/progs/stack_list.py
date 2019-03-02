""" 基于 Python list 实现的栈类 
"""


class StackUnderflow(ValueError):
    pass


class SStack(): 
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return not self._elems

    def top(self):
        if not self._elems:
            raise StackUnderflow
        return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if not self._elems:
            raise StackUnderflow
        return self._elems.pop()

    
if __name__ == '__main__':
    st = SStack()
    st.push(1)
    st.push(5)
    print(st.pop())
    print(st.top())
    print(st.pop())
    print(st.is_empty())
    st.top()
