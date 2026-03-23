class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        res = []
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        
        for num, cnt in seen.items():
            freq[cnt].append(num)
        
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

# before you try to use a sorted list really justify in your head if you need to sort. just becuase they want a specific nlogn solution doesnt mean it involves sorting. All solutions involve a frequency map first. For top frequent elements think about making these frequency maps first.
