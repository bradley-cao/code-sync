class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = dict()
        for i in range(len(nums)):
            if nums[i] not in freqs:
                freqs[nums[i]] = 0
            freqs[nums[i]] += 1

        return sorted(freqs, key=freqs.get, reverse=True)[:k]