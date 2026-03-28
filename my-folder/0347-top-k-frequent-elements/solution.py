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

    # the way this works is you get the frequency count and then because you want to find the top k, rather than iterating through a dictionary and sorting, make a list where the index is represented by the count which is bounded by the length of the list. then just run through the list backwards in index and collect all the things in the lists until k are reached.

    def topKFrequentHeap(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

    # note a heap is used to efficiently find the max and mins 

    def topKFrequent2ndAttempt(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = Counter(nums)
        res = []
        for key in count:
            heapq.heappush(heap, (-count[key], key))
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return(res)
    
    # this second attempt is good as you remebered to use a heap. note: its better than you just use a normal heap but you say once the length of the heap is longer than k then pop from the list after you add. this pop removes smallest element meaning youll only be left with the k biggest.
