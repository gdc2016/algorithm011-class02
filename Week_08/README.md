# 第8周学习总结

本周主要学习了位运算，布隆过滤器，LRU缓存和排序算法

### 位运算

十进制转换为二进制的方法：

将十进制数不断除以2并从末尾往前填写每次除下来的余数，等到整个除完后就能得到二进制数

常用的位运算符如下：

按位或：|

按位与：&

按位取反：~

按位异或：^

常用的位运算：

1. 将 x 最右边的 n 位清零： x& (~0 << n)
2. 获取 x 的第 n 位值（ 0 或者 1）： (x >> n) & 1
3. 获取 x 的第 n 位的幂值： x& (1 << n)
4. 仅将第 n 位置为 1：x | (1 << n)
5. 仅将第 n 位置为 0：x & (~ (1 << n))
6. 将 x 最高位至第 n 位（含）清零： x& ((1 << n) -1）
7. 将第 n 位至第 0 位（含）清零： x& (~ ((1 << (n + 1))-1))

实战运算要点（常用的一些操作转换为位运算）

- 判断奇偶：
- 判断偶数：
- x%2==0 --> x&1 == 0
- 判断奇数：
- x%2==1 --> x&1 == 1
- 将变量除以2：
- x/2 --> x>>1
- 清零最低位的 1:
- X = X&(X-1)
- 得到最低位的 1:
- X&-X
- X&~X => 0

### 布隆过滤器：

布隆过滤器可以用于检索一个元素是否在一个集合中。

优点是空间效率和查询时间都远远超过一般的算法。

缺点是有一定的误识别率和删除困难。
应用场景：

1. 比特币网络
2. 分布式系统（Map-Reduce） — Hadoop、search engine
3. Redis 缓存
4. 垃圾邮件、评论等的过滤

### LRU缓存

两个要素： 大小 、替换策略
Hash Table + Double LinkedList

操作时间复杂度：

- O(1) 查询
- O(1) 修改、更新

代码实现：

```python
class LRUCache(object): 

	def __init__(self, capacity): 
		self.dic = collections.OrderedDict() 
		self.remain = capacity

	def get(self, key): 
		if key not in self.dic: 
			return -1 
		v = self.dic.pop(key) 
		self.dic[key] = v   # key as the newest one 
		return v 

	def put(self, key, value): 
		if key in self.dic: 
			self.dic.pop(key) 
		else: 
			if self.remain > 0: 
				self.remain -= 1 
			else:   # self.dic is full
				self.dic.popitem(last=False) 
		self.dic[key] = value
```

### 排序算法

常见排序算法示例：

冒泡排序：

```python
def Bubble_sort(s):
    for i in range(len(s)):
        #执行每一趟排序,len(s)-i到len(s)-1为已经排好序的区域，无需再进行比较
        for j in range(len(s)-i-1):
        #比较前后相邻的两个数
            if s[j] > s[j+1]:
                s[j],s[j+1] = s[j+1],s[j]
```

选择排序：

```python
def selection_sort(s):
    N = len(s)
    for i in range(N):
        #假设首项为最小值
        min = i
        #遍历未排序区域
        for j in range(i+1,N):
        #将未排序区域的每个值与当前的最小值进行比较，找到真正的最小值
            if s[j] < s[min]:
                min = j
        s[i],s[min] = s[min],s[i]
```

插入排序：

```python
def Insertion_sort(s):
    N = len(s)
    for i in range(1,N):
        j = i
        #将当前值与前面的每一项进行比较
        while j > 0 and s[j] < s[j-1]:
            s[j],s[j-1] = s[j-1],s[j]
        #每次交换后要更新j的值，确保永远指向当前进行插入排序的值
            j -= 1
```

归并排序：

```python
def mergesort(nums, left, right):
    if right <= left:
        return
    mid = (left+right) >> 1
    mergesort(nums, left, mid)
    mergesort(nums, mid+1, right)
    merge(nums, left, mid, right)

def merge(nums, left, mid, right):
    temp = []
    i = left
    j = mid+1
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            temp.append(nums[i])
            i +=1
        else:
            temp.append(nums[j])
            j +=1
    while i<=mid:
        temp.append(nums[i])
        i +=1
    while j<=right:
        temp.append(nums[j])
        j +=1
    nums[left:right+1] = temp
```

快速排序：

```python
def quick_sort(begin, end, nums):
    if begin >= end:
        return
    pivot_index = partition(begin, end, nums)
    quick_sort(begin, pivot_index-1, nums)
    quick_sort(pivot_index+1, end, nums)
    
def partition(begin, end, nums):
    pivot = nums[begin]
    mark = begin
    for i in range(begin+1, end+1):
        if nums[i] < pivot:
            mark +=1
            nums[mark], nums[i] = nums[i], nums[mark]
    nums[begin], nums[mark] = nums[mark], nums[begin]
    return mark
```

堆排序：

```python
def heapify(parent_index, length, nums):
    temp = nums[parent_index]
    child_index = 2*parent_index+1
    while child_index < length:
        if child_index+1 < length and nums[child_index+1] > nums[child_index]:
            child_index = child_index+1
        if temp > nums[child_index]:
            break
        nums[parent_index] = nums[child_index]
        parent_index = child_index
        child_index = 2*parent_index + 1
    nums[parent_index] = temp


def heapsort(nums):
    for i in range((len(nums)-2)//2, -1, -1):
        heapify(i, len(nums), nums)
    for j in range(len(nums)-1, 0, -1):
        nums[j], nums[0] = nums[0], nums[j]
        heapify(0, j, nums)
```

