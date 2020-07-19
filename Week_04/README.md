# 第四周学习总结

本周主要进一步学习了广度优先搜索和深度优先搜索以及学习了两个算法，贪心算法和二分查找

## 广度优先搜索和深度优先搜索

广度优先搜索

基本思想是：首先访问起始顶点v，然后由v出发，依次访问v的各个未被访问过的邻接顶点，然后再依次访问这些顶点的所有未被访问过的邻接顶点，再从这些访问过的顶点出发，再访问它们所有未被访问过的邻接顶点….以此类推，直到途中所有的顶点都被访问过为止。类似于二叉树的层序遍历

bfs的代码实现模板如下：

```python
def bfs(graph,start,end):
    queue = []
    queue.append([start])
    #由于图存在环，故需记录访问过的顶点
    visited = set()
    while queue:
        node = queue.pop()
        visited.add(node)
        process(node)
        nodes = generated_related_nodes(node)
        queue.push(nodes)
```

深度优先搜索：

采用回溯的思想，从图的起始顶点出发，向前搜索，以达到目标。但当探索到某一步时，发现原先选择并不优或达不到目标，就退回一步重新选择，直到最终遍历完整个图。

dfs的代码实现模板如下：

```python
visited = set()
def dfs(node,visited):
    #终止条件，判断该点是否已经访问过
    if node in visited:
        return
    visited.add(node)
    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node,visited)
```

## 贪心算法

贪心算法的基本思想是从局部分析问题，每次找到一个局部中的最优情况，不断叠加，从而找到整个问题的最优解。

与动态规划不同，贪心算法对每个子问题的解决方法都做出选择，不能回退。动态规划会保存之前子问题的解，并根据以前的结果对当前进行选择，可以回退。

贪心算法存在一定的局限性，因为并不是每个局部都找最优解叠加就一定是整个问题的最优解，故只有在一些特定场景下可以采用贪心算法。

如最优化问题，图中的最小生成树和哈夫曼编码。

一旦一个问题可以通过贪心算法来解决，那贪心算法一定是该问题的最优解。

由于贪心法的高效性以及其所求得的答案比较接近最优结果，故在现实场景中贪心法也可以用作辅助算法或者直接解决一些要求结果不特别精确的问题。

## 二分查找

对一个数组的查找方式可以通过从头或从尾遍历每个元素，从而找到符合条件的元素，这样的话每个元素都需访问一次，时间复杂度为O(n)，对于很长的数组，这样的查询方式效率就显得偏低了。针对有序数组，可以采用二分查找的方式提升查找效率，由于每次的对半查找，故时间复杂度为O(logn)，相比遍历查找大幅提升了。

二分查找的代码模板如下：

```python
left, right = 0, len(array) - 1
while left <= right:
    mid = (left + right) / 2
    if array[mid] == target:
    	# find the target!!
        break or return result
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

