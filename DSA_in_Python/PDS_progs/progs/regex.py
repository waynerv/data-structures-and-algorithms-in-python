""" 简单正则表达式的匹配 """

__author__ = 'Qiu Zongyan'
#### 简化正则表达式匹配函数
## 模式语言：
## 字符 c 与其自身匹配
## ^ 与字符串开头匹配（匹配前缀）
## $ 与字符串结束匹配（匹配后缀）
## . 与任何字符匹配
## * 和其前一字符一起，与该字符的0次或任意次出现匹配

## 限制：字符串中不能出现上述元字符（不支持换意序列）


def match(re, text):
    rlen, tlen = len(re), len(text)

    def match_here(re, i, text, j):
        """检查从text[j]开始的正文是否与re[i]开始的模式匹配"""
        while True:
            if i == rlen:
                return True
            if re[i] == '$':
                return i+1 == rlen and j == tlen
            if i+1 < rlen and re[i+1] == '*':
                return match_star(re[i], re, i+2, text, j)
            if j == tlen or (re[i] != '.' and re[i] != text[j]):
                return False
            i, j = i+1, j+1

    def match_star(c, re, i, text, j):
        """在text里跳过0个或多个c后检查匹配"""
        for n in range(j, tlen):
            # print(c, n, i, j)
            if match_here(re, i, text, n):
                return True
            if text[n] != c and c != '.':
                break
        return False

    if re[0] == '^':
        if match_here(re, 1, text, 0): # 只匹配前缀
            return 0
        return -1                      # 匹配前缀不成功
    for n in range(tlen):              # 检查各个位置的匹配
        if match_here(re, 0, text, n):
            return n
    return -1

p1 = "a*b.*"
p2 = "^ab*c.$"
p3 = "a*bc.*bc"
p4 = "aab*c$"

print(match(p1, "bccdabaaabcbbabcccbc")) # 0
print(match(p1, "cccdabaaabcbbabcccbc")) # 4
print(match(p1, "cccdadcccbcbaabcccbc")) # 9
print(match(p2, "abbbbbca"))             # 0
print(match(p2, "^^^^abbcd"))            # -1
print(match(p2, "abbbbbcda"))            # -1
print(match(p3, "bccdabaaabcbbabcccbc")) # 0
print(match(p3, "dccdabaaabcbbabcccbc")) # 6
print(match(p4, "hfahfjkhhaabbc"))       # 9
print(match(p4, "hfahfjkhhaabbcd"))      # -1


