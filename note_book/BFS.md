# BFS
## 图遍历 & 拓扑序

### 遍历

树与图的广度优先遍历需要使用一个队列来实现。起初，队列中仅包含一个起点(例如1号节点)。在广度优先遍历的过程中，我们不断从队头取出一个节点x,对于x面对的多条分支，把沿着每条分支到达的下一个节点（如果尚未访问过）插入队尾，重复执行上述过程直到队列为空。

![[Pasted image 20220416142825.png]]

[AcWing 847. 图中点的层次](https://www.acwing.com/problem/content/849/)

```python3
import collections  
  
helper_ipt = lambda: map(int, input().split())  
  
N = int(1e5 + 10)  
n, m = helper_ipt()  
h, to_e, prev_ne, idx = [0] * N, [0] * N, [0] * N, 0  
  
  
def add(u, v):  
    global idx  
    idx += 1  
    to_e[idx] = v  # 1. 存出边  
    prev_ne[idx] = h[u]  # 2. 修改指针，准备加新边  
    h[u] = idx  # 3. 加新边  
  
  
for _ in range(m):  
    u, v = helper_ipt()  
    add(u, v)  
  
  
def bfs():  
    d, que = [-1] * N, collections.deque()  
    d[1] = 0  
    que.append(1)  
    while que:  
    u_idx = que.popleft()  
    u = h[u_idx]  
    while u:  
    v = to_e[u]  
    u = prev_ne[u]  
    # 加入待搜索的队列中  
    if d[v] == -1:  
    que.append(v)  
    # 更新d的距离  
    d[v] = d[u_idx] + 1  
    return d[n]  
  
minimum_step = bfs()  
  
print(  
    minimum_step  
)
```


### 拓扑序

 给定一张有向无环图，拓扑序A满足： 对于图中的每条边(Z,Y), X在A中都出现在y之前
 
 拓扑排序核心思想：重复选择入度为0的点x，将其连接的点入度-1
 1. 预计算所有点的入度deg[i]，构建入度为0的搜索队列que
 2. 从队列取出带搜索元素x，并将x插入到拓扑序尾部
 3. 从x出发的每条边(x,y),对y进行deg[y] - 1,如果减到0，则加入到搜索队列尾部。
 4. 重复2，3直到搜索队列为空
 5. 检查拓扑序和图顶点的数量关系，如果小于顶点数量，则说明有顶点未被遍历，进而证明存在环路。

[AcWing 848. 有向图的拓扑序列](https://www.acwing.com/problem/content/850/)

```python3
import collections  
  
N = int(1e5 + 10)  
h, e, ne, idx, in_deg = [0] * N, [0] * N, [0] * N, 0, [0] * N  
helper_ipt = lambda: map(int, input().split())  
  
  
def add(u, v):  
    global idx  
    idx += 1  
    e[idx] = v  
    ne[idx] = h[u]  
    h[u] = idx  
  
  
n, m = helper_ipt()  
for _ in range(m):  
    u, v = helper_ipt()  
    add(u, v)  
    in_deg[v] += 1  
  
  
def bfs():  
    que, top_sequence = collections.deque(), []  
    # 这里由于初始化in_deg长度是N，可以遍历所有图中的节点，来确保正确的初始化0入度点  
    for i in range(1, n + 1):  
    if in_deg[i] == 0: que.append(i)  
    while que:  
    u_idx = que.popleft()  
    u = h[u_idx]  
    top_sequence.append(u_idx)  
    while u:  
    v = e[u]  
    u = ne[u]  
    in_deg[v] -= 1  
    if in_deg[v] == 0: que.append(v)  
    return top_sequence  
  
  
A = bfs()  
  
if len(A) == n:  
    print(*A)  
else:  
    print(-1)
```

- [x] 有什么应用呢... 学了之后没啥感觉？

[[164. 可达性统计]] 

## 性质总结

### 层序
### 阶段性和单调性

## 经典模型

### 最短路

#### 1边权 & 单源

1. [[844. 走迷宫 | 裸最短路问题]]
2. [[1076. 迷宫问题 | 变形 -> 路径存储]]
3. [[188. 武士风度的牛 | 变形 -> 搜索方向]]
4. [[1100. 抓住那头牛 | 变形 -> 问题抽象建图]]


#### 1边权 & 多源
1. [[173. 矩阵距离]]

#### 01边权
1. [[175. 电路维修]]
2. [[E - Bishop 2]]

#### 不同边权

> 理解成图的最短路问题

### 最小步数

[[1107. 魔板]]
[[190. 字串变换]]
[[179. 八数码]]
[[172. 立体推箱子]]
[[174. 推箱子]]

## 优化
###  双向搜索
###  A*
