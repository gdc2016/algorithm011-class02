# 第三周学习总结

本周主要学习了泛型递归和分治回溯的算法。

### 泛型递归

递归是通过函数体来进行循环，在汇编语言中并没有所谓的循环，而是通过返回之前的代码或函数体达到循环的效果，也就是递归。

递归的代码实现模板如下：

```python
def recursion(level, param1, param2, ...): 
    # recursion terminator (终止条件)
    if level > MAX_LEVEL: 
	   process_result 
	   return 
    # process logic in current level （当前层处理逻辑）
    process(level, data...) 
    # drill down （进入下一层）
    self.recursion(level + 1, p1, ...) 
    # reverse the current level status if needed （若需要，返回当前层后清除当前层的操作）
```

递归学习要点：

1. 初学时可以通过画树形图理解递归思想
2. 熟练后要抛弃人肉递归
3. 分析问题时尝试将其拆解成可重复解决的问题
4. 利用数学归纳法的思维

### 分治和回溯

分治（Divide & Conquer) 的基本思想是将一个大问题分解为若干个规模较小的子问题，这些子问题相互独立且与原问题性质相同，分别求出这些子问题的解后，再通过合适的方法将他们合并成整个问题的解。分治和递归的区别在于递归未必存在将子问题合并求解的过程，可能递归完后就直接求解。

分治法的代码实现模板如下：

```python
def divide_conquer(problem, param1, param2, ...): 
  # recursion terminator (递归终止条件)
  if problem is None: 
	print_result 
	return 
  # prepare data （数据准备）
  data = prepare_data(problem) 
  subproblems = split_problem(problem, data) 
  # conquer subproblems （问题分解）
  subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
  subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
  subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
  …
  # process and generate the final result （处理并产生问题的解）
  result = process_result(subresult1, subresult2, subresult3, …)
	
  # revert the current level states （清除当前层的状态）
```

回溯：采用试错的思想，它尝试分步的去解决一个问题，首先尝试从一个方向来解答问题，当发现该方向无法得到正确的结果时，便进行回退，从其它的方向来寻求解答，深度优先搜索采用的便是回溯的思想。

