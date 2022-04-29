from collections import defaultdict, Counter, deque
from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph, in_degree = defaultdict(list), Counter()
        for idx, u in enumerate(recipes):
            for v in ingredients[idx]:
                # 该原材料v 能制作出菜品u
                graph[v].append(u)
            in_degree[u] += len(ingredients[idx])
        # TODO: 这里的初始化队列，为什么不需要找入度为0的点呢？
        que, top_sort = deque(supplies), []
        while que:
            u = que.popleft()
            # 不属于图中的菜品/原材料
            if u not in graph: continue
            # 修改当前节点的出边
            for v in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    top_sort.append(v)
                    que.append(v)
        return top_sort
