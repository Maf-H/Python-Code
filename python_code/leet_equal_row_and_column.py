from pprint import pprint
class Solution:
    def equal_pairs(self, grid: list[list[int]]) -> int:
        columns = [[r[i] for r in grid] for i in range(len(grid))]
        count_r = 0

        # grid_dict = {}
        # for row in grid:
        #     print(row)
        # print()
        # for col in columns:
        #     print(col)

        for row in grid:
            for col in columns:
                if row == col:
                    count_r += 1
                    # d[tuple(g)] = 1
        # else:
        #     d[tuple(g)] += 1

        # for row in grid:
        #     if row in columns:
        #         count_r += 1
        # for col in columns:
        #     if col in grid:
        #         count_c += 1
        return count_r
grids = [[[13,13],[13,13]],[[3,2,1],[1,7,6],[2,7,7]], [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]]
# for grid in grids[0]:
#     print(grid)
# for grid in grids[1]:
#     print(grid)

s = Solution()
for grid in grids:
    print(s.equal_pairs(grid))