# 实现一个 flatten 函数，把嵌套的列表扁平化，你需要用递归函数来实现。
# 比如 [[1,2], [1,2,3] -> [1,2,1,2,3]

def flatten(mylist):
    result = []
    def nested(mylist):
        for item in mylist:
            if isinstance(item, list):
                nested(item)
            else:
                result.append(item)
    nested(mylist)
    return result

def test_flatten():
    list01 = [1, 2, 3, 4]
    assert flatten(list01) == [1, 2, 3, 4]
    list02 = [1, [2, 3], 4]
    assert flatten(list02) == [1, 2, 3, 4]
    list03 = [1, [2, [3, 4]]]
    assert flatten(list03) == [1, 2, 3, 4]
    list04 = [1, [2, [3, [4]]]]
    assert flatten(list04) == [1, 2, 3, 4]
