class Solution:
    def survivedRobotsHealths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
        # O(N log N) - time, O(N) - space
        actual_healths = [x for x in healths]
        pos_pairs = sorted([(pos, i) for i, pos in enumerate(positions)])

        stack = []
        for _, i in pos_pairs:
            if directions[i] == 'R':
                stack.append(i)
            if directions[i] == 'L':
                while stack and actual_healths[i] > 0:
                    ci = stack[-1]
                    if actual_healths[ci] == actual_healths[i]:
                        actual_healths[i] = 0
                        actual_healths[ci] = 0
                        stack.pop()
                    elif actual_healths[ci] > actual_healths[i]:
                        actual_healths[i] = 0
                        actual_healths[ci] -= 1
                    else:
                        actual_healths[i] -= 1
                        actual_healths[ci] = 0
                        stack.pop()
        ans = [x for x in actual_healths if x > 0]
        return ans

