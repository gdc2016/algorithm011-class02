# 第二周学习总结

本周主要学习了哈希表、集合、树，堆以及图

### 哈希表和集合

哈希表，也是散列表，与数组通过索引不同，哈希表是通过键值key对元素进行直接访问。哈希函数的常见构造方式有：

1. 直接定制法
2. 数字分析法
3. 平方取中法
4. 折叠法
5. 除留余数法

集合（set）是一个元素不重合并且无序的数据结构，与哈希表不同，集合不存在键值key索引。

在python中，哈希表通过字典方式实现，哈希表和集合的定义方式分别如下：

```python
#定义一个有初始值的字典（哈希表）
dic = {'A':1,'B':2,'c':1}
#定义一个空字典
dic = {}
#定义集合
s = set([1,2,3])
s = set()
```

字典的常用操作如下：

- 查询： 根据key进行元素访问，时间复杂度为O(1)
- 插入：在不出现哈希冲突的情况下，时间复杂度为O(1)
- 删除：时间复杂度为O(1)
- 修改：时间复杂度为O(1)

### 树，二叉树，二叉搜索树

在python中树和二叉树的结点实现方式如下：

```python
#树结点
class TreeNode():
    def __init__(self,x):
        self.val = x
        #可以以列表形式存储多个子结点
        self.children = None
#二叉树结点
class BinaryTreeNode():
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
```

树与二叉树的区别是二叉树只有左子树与右子树，但是树可以有多个子树。

二叉树的遍历方式有四种：

1. 前序遍历：又称先序遍历，先访问根结点再访问左子树和右子树
2. 中序遍历：先访问左子树，再访问根节点最后再访问右子树
3. 后续遍历：先访问左子树，再访问右子树最后访问根
4. 层序遍历：依次访问每层的结点

无论是何种遍历方式，在遍历过程中每个元素都只访问一次，所以时间复杂度都为O(n)。具体实现方式如下：

```python
#前序遍历
def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)
#中序遍历
def inorder(root):
    if root:      
        inorder(root.left)
        print(root.val)
        inorder(root.right)
#后序遍历
def postorder(root):
    if root:      
        postorder(root.left)     
        postorder(root.right)
        print(root.val)
#层序遍历
def levelorder(root):
    queue = [root]
    if not root:
        return
    while queue:
        p = queue.pop(0)
        print(p.val)
        if p.left:
        	queue.append(p.left)
        if p.right:
        	queue.append(p.right)
```

二叉搜索树也称二叉有序树，它的主要特性是左子树中的结点小于根节点，右子树的值大于根节点，其中空树也是一个二叉搜索树。根据此特性，中序遍历二叉搜索树可以得到一个有序的序列。

### 堆

通过堆可以找到序列中的最大值（大根堆）或最小值（小根堆）的数据结构

对于大根堆，常用的操作有：

1. 找到当前最大值：直接获取首项元素，时间复杂度为O(1)
2. 删除元素：由于添加元素回导致元素的调整，时间复杂度为O(logn)
3. 添加元素：如当前位置就是该元素的最佳位置，时间复杂度为O(1)，不然会出现位置的调整，时间复杂度为O(logn)

二叉堆的主要性质如下：

1. 是一棵完全二叉树
2. 树中任意结点的值总是大于等于其子节点的值

二叉堆一般以数组的方式实现：

1. 索引为i的左孩子结点时2i+1
2. 索引为i的右孩子结点时2i+2
3. 索引为i的父节点的索引是(i-1)/2

二叉堆也是优先队列的常用实现方式。

### 图

图的组成部分：

- 点
  1. 度：可以与该点连通的边的个数，在有向图中分入度和出度
  2. 判断点与点之间是否连通
- 边
  1. 方向（分有向和无向）
  2. 权重

图的种类主要有：

1. 有向图

   有向无权图

   有向有权图

2. 无向图

   无向无权图

   无向有全图

图的算法主要有：

1. 广度优先搜索

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

   2. 深度优先搜索：

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

   3. 拓扑排序
   4. 最短路径算法