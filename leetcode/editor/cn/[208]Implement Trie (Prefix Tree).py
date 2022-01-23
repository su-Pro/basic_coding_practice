# leetcode submit region begin(Prohibit modification and deletion)
class Trie:

    def __init__(self):
        # 这里的N是一次性初始化的容量
        self.N = 100009
        self.son_set = [[0] * 26 for i in range(self.N)]
        self.cnt = [0] * self.N
        #标识当前已经有几个节点进入了Trie中
        self.idx = 0

    def insert(self, word: str) -> None:
        p_idx = 0
        for _, ch in enumerate(word):
            ch_u = ord(ch) - ord('a')
            if self.son_set[p_idx][ch_u] is 0:
                self.idx += 1
                self.son_set[p_idx][ch_u] = self.idx
            p_idx = self.son_set[p_idx][ch_u]
        self.cnt[p_idx] += 1

    def search(self, word: str) -> bool:
        p_idx = 0
        for _, ch in enumerate(word):
            ch_u = ord(ch) - ord('a')
            if self.son_set[p_idx][ch_u] is 0: return False
            p_idx = self.son_set[p_idx][ch_u]
        return self.cnt[p_idx] != 0

    def startsWith(self, prefix: str) -> bool:
        p_idx = 0
        for _,ch in enumerate(prefix):
            ch_u = ord(ch) - ord('a')
            if self.son_set[p_idx][ch_u] is 0: return False
            p_idx = self.son_set[p_idx][ch_u]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# leetcode submit region end(Prohibit modification and deletion)
