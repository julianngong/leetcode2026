class Solution:
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        #[i for i in range(len(nums))] makes a list of indices from 0 to len(nums)-1
        #list(zip(list1,list2)) makes a list of tuples
        #sorted_list = sorted(tuple_list) will sort the tuple list based on the first element
        #sorted_list = sorted(tuple_list, key=lambda x: x[1]) sorts it by the second element
        numandindex = list(zip(nums, [i for i in range(len(nums))]))
        nums = sorted(numandindex)
        front = len(nums)-1
        back = 0
        found = False
        while found == False:
            added = nums[back][0]+nums[front][0]
            print("sum :",added)
            if added > target:
                front-=1
            elif added < target:
                back+=1
            else:
                found = True
        return([nums[back][1],nums[front][1]])
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i in range(len(nums)):
            table[nums[i]]=i
        print(table)
        for j in range(len(nums)):
            remainder = target - nums[j]
            if remainder in table.keys() and table[remainder] != j:
                return([j,table[remainder]])
            
