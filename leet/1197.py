from collections import deque


class Solution2:
    offsets = [(1, -2), (1, 2), (-1, -2), (-1, 2),
               (2, 1), (2, -1), (-2, 1), (-2, -1)]


class Solution1:
    offsets = [(1, -2), (1, 2), (-1, -2), (-1, 2),
               (2, 1), (2, -1), (-2, 1), (-2, -1)]

    def minKnightMoves(self, _x: int, _y: int) -> int:
        visited = set()  # a
        queue = deque([(0, 0)])  # b
        steps = 0  # c

        while queue:
            cur_level_cnt = len(queue)  # 1: x
            for i in range(cur_level_cnt):
                cur_x, cur_y = queue.popleft()  # 2:
                if (cur_x, cur_y) == (_x, _y):
                    return steps

                for offset_x, offset_y in self.offsets:
                    offset_x, offset_y = cur_x + offset_x, cur_y + offset_y  # 3
                    if (offset_x, offset_y) not in visited:
                        visited.add((offset_x, offset_y))
                        queue.append((offset_x, offset_y))
            steps += 1

        return -1


class Solution:
    offsets = [(1, 2), (2, 1), (2, -1), (1, -2),
               (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

    def minKnightMoves(self, _x: int, _y: int) -> int:
        visited = set()
        que = deque([(0, 0)])
        steps = 0

        while que:
            cur_level_cnt = len(que)
            #print(cur_level_cnt)
            for i in range(cur_level_cnt):
                cur_x, cur_y = que.popleft()
                if (cur_x, cur_y) == (_x, _y):
                    return steps

                for offset_x, offset_y in self.offsets:
                    x, y = offset_x + cur_x, offset_y + cur_y
                    if (x, y) not in visited:
                        visited.add((x, y))
                        que.append((x, y))

            steps += 1


#


s = Solution()
print(s.minKnightMoves(2, 1))
print(s.minKnightMoves(5, 5))


# end of file
