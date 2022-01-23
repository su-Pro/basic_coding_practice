# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        for sub_path in path.split('/'):
            if sub_path == '..':
                if stk: stk.pop()
            elif sub_path == '' or sub_path == '.':
                continue
            else:
                stk.append(sub_path)
        return '/' + '/'.join(stk)


# leetcode submit region end(Prohibit modification and deletion)

Solution().simplifyPath('/../')
