class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_len = len(nums)
        dictionary_of_list_entries_iterated_on = {}  
        
        for i in range(0, num_len, 1):
            delta = target - nums[i]  
            if delta in dictionary_of_list_entries_iterated_on:
                dict_index = int(dictionary_of_list_entries_iterated_on[delta])
                if dict_index != i:
                    return [i, dict_index]
            dictionary_of_list_entries_iterated_on[nums[i]] = str(i)

                