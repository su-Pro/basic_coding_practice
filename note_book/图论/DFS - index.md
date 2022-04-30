# DFS

## 关键问题
### 递归栈
### 区别于BFS

***优点***
- 代码短，易实现

### 内部搜索 & 外部搜索

> 判别依据：是以整个棋牌状态为准还是以棋牌内部的格子为准?「不严谨」更容易接受的是：在决策树中，不同路径是否需要维护严格的“独立状态”

- 考虑到是否需要手动回溯关键状态（例如vt数组）

[AcWing 1112. 迷宫](https://www.acwing.com/activity/content/problem/content/1480/) vs [AcWing 1113. 红与黑](https://www.acwing.com/activity/content/problem/content/1481/) 


## Flood-fill 联通性

> 局限性：无法求**轻松**求得最短路程
- [ ] 迁移该部分，到图论 - Flood-fill
	- [ ]  BFS
	- [ ]  DFS
	- [ ]  代码


- [x] AcWing 1097. 池塘计数 TODO: BFS flood-fill 补充
- [x] AcWing 1098. 城堡问题
- [x] AcWing 1106. 山峰和山谷
- [x] AcWing 1112. 迷宫
- [x] AcWing 1113. 红与黑

## *状态搜索
- [ ] 和二进制枚举的关系？

- [x] AcWing 1116. 马走日
- [x] AcWing 1117. 单词接龙
- [ ] AcWing 1118. 分成互质组

## *记忆化

- [ ] 和DP问题之间的转化？

## *剪枝策略

## 迭代加深

## 双向DFS

## IDA*

## 图 - 遍历