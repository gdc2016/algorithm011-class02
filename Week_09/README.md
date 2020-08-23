# 第九周学习总结

本周主要是进一步学习了动态规划和字符串

### 高级动态规划

1. 分治+最优子结构
2. 顺推形式：动态递推

相关练习：

1. 爬楼梯
2. 不同路径
3. 股票系列题目
4. 打家劫舍系列题目

不同路径的状态转移方程：

dp[i][j] = dp[i+1][j] + dp[i][j+1]

dp[0][0]最终会保存共有几条不同路径

### 字符串

python中字符串是不可变的

Atoi模板

```python
# Python
class Solution(object):
    def myAtoi(self, s):
        if len(s) == 0 : return 0
        ls = list(s.strip())
        
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-','+'] : del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit() :
            ret = ret*10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign * ret,2**31-1))
```

字符串暴力匹配模板

```python
# Python
def forceSearch(txt, pat):
  n, m = len(txt), len(pat)
  for i in range(n-m+1):
    for j in range(m):
      if txt[i+j] != pat[j]:
        break
    if j == m:
      return i
  return -1 
```

Rabin-Karp代码实现

```python
#Python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        d = 256
        q = 9997
        n = len(haystack)
        m = len(needle)
        h = pow(d,m-1)%q
        p = 0
        t = 0
        if m > n:
            return -1
        for i in range(m): # preprocessing
            p = (d*p+ord(needle[i]))%q
            t = (d*t+ord(haystack[i]))%q
        for s in range(n-m+1): # note the +1
            if p == t: # check character by character
                match = True
                for i in range(m):
                    if needle[i] != haystack[s+i]:
                        match = False
                        break
                if match:
                    return s
            if s < n-m:
                t = (t-h*ord(haystack[s]))%q
                t = (t*d+ord(haystack[s+m]))%q
                t = (t+q)%q
        return -1
```

KMP算法

KMP算法（Knuth-Morris-Pratt）的思想就是，当子串与目标字符串不匹配时，其实你已经知道了前面已经匹配成功那 一部分的字符（包括子串与目标字符
串）。KMP 算法的想法是，设法利用这个已知信息，不要把“搜索位置” 移回已经比较过的位置，继续把它向后移，这样就提高了效率。