from collections import defaultdict
import heapq

class Solution:
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        total = []
        output = []
        if len(nums) == 1:
            return([nums[0]])
        else:
            nums = sorted(nums)
            count = defaultdict(int)
            initial = nums[0]
            count[initial] += 1
            for i in range(1,len(nums)):
                if nums[i] != nums[i-1]:
                    total.append((nums[i-1],count[nums[i-1]]))
                    initial = nums[i]
                count[initial]+=1
            total.append((nums[i],count[nums[i]]))
            total = sorted(total, key=lambda x: x[1],reverse = True)
            for i in range(k):
                output.append(total[i][0])
            return(output)
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num]+=1
        max_heap = []  # Create a max heap

        for num, freq in count.items():
            # Push (negative frequency, number) into the max heap
            heapq.heappush(max_heap, (freq, num))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        result = [num for _, num in max_heap]
        return(result)


        
