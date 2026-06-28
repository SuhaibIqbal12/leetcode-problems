from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 1

        # Handle number 1 separately
        if 1 in count:
            if count[1] % 2 == 0:
                ans = count[1] - 1
            else:
                ans = count[1]

        for x in count:
            if x == 1:
                continue

            length = 0
            curr = x

            while count[curr] >= 2:
                length += 2
                curr *= curr

            if count[curr] == 1:
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans