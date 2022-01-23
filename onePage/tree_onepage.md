# tree_onepage

## 基本概念

### 现实世界

#### 1. 案例

#### ⭐️ 2. 属性

### 计算机世界

#### 1. 术语

#### ⭐️ 2. 定义与ADT

#### ⭐️ 3. 实现

***递归列表***

***基础指针***

## 应用 & 基本操作

### ⭐️ 1. 表达式解析

### 2. 遍历

## 变种

### complete tree

[[[958]Check Completeness of a Binary Tree]]

### 快搜（BST & AVL）

### ⭐️ Trie

[wiki](https://en.wikipedia.org/wiki/Trie#Dictionary_representation)

- [prefix树](https://en.wikipedia.org/wiki/File:Trie_example.svg)
- 快速读写字符串集合？

#### 1. 应用

> 目前只是站在解决算法题的角度，未从工业应用角度考虑问题

1. 判断存在性
2. 计算出现次数

#### 2. 基本思想

#### 3. 模板代码

[835. Trie字符串统计](https://www.acwing.com/problem/content/submission/code_detail/10044010/) 

```python
N = 100010
cnt = [0] * N
son_set = [[0] * 26 for i in range(N)]
# 标识当前一共存了多少个节点到trie中
idx = 0


def insert(str):
    global idx, cnt, son_set
    p_idx = 0

    for _, ch in enumerate(str):
        ch_u = ord(ch) - ord('a')
        if son_set[p_idx][ch_u] is 0:
            idx += 1
            son_set[p_idx][ch_u] = idx
        p_idx = son_set[p_idx][ch_u]
    cnt[p_idx] += 1


def query(str):
    global idx, cnt, son_set
    p_idx = 0

    for _, ch in enumerate(str):
        ch_u = ord(ch) - ord('a')
        if son_set[p_idx][ch_u] is 0: return 0
        p_idx = son_set[p_idx][ch_u]

    return cnt[p_idx]


def main():
    n = int(input())
    while (n):
        n -= 1
        opt, s = list(input().split(" "));
        str = list(s)

        if (opt == "I"):
            insert(str)
        else:
            print(query(str))


main()
```

#### 4. 典型例题
[[[208]Implement Trie (Prefix Tree)]]

#### 5. 变种问题

推荐阅读：
[【宫水三叶】一题双解 :「二维数组」&「TrieNode」](https://leetcode-cn.com/problems/implement-trie-prefix-tree/solution/gong-shui-san-xie-yi-ti-shuang-jie-er-we-esm9/)

### ⭐️ 并查集

