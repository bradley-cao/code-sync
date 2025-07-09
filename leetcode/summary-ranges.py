class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []

        if len(nums) == 0: return []

        left = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] - nums[i - 1] == 1:
                i += 1
            else:
                right = nums[i-1]
                if left == right:
                    ranges.append(str(right))
                else:
                    ranges.append(f"{left}->{right}")
                left = nums[i]
                i += 1
        
        right = nums[len(nums) - 1]
        if left == right:
            ranges.append(str(right))
        else:
            ranges.append(f"{left}->{right}")
        return ranges