
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def backtrack(index):
            if index == len(nums):
                result.append(path[:])
                return

            # Include current number
            path.append(nums[index])
            backtrack(index + 1)

            # Exclude current number
            path.pop()
            backtrack(index + 1)

        backtrack(0)
        return result
