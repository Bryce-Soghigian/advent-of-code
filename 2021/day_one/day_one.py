import os
def load_array():
    """
    Loads example input
    """
    output = []
    
    with open(os.path.join(os.getcwd(), '2021/day_one.txt'), 'rt') as f:
        for num in f:
            num = int(num.strip().replace('\n', ''))
            output.append(num)

    return output

class Solution:


    def _part_one(self,nums):
        if len(nums) == 1:
            return 0
        output = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                output += 1
        return output


    def _part_two_optimized(self, nums,k=3):
        """
        
        We want to maintain a window of size k
        """
        increasing = []
        curr_window_sum = sum(nums[0:k])
        start = 0
        end = k

        while end <= len(nums)-1:
            increasing.append(curr_window_sum)
            curr_window_sum -= nums[start]
            curr_window_sum += nums[end]
            start += 1
            end += 1
        
        return self._part_one(increasing) + 1




    def _part_two(self, nums, k=3):
        """
        We want to check to see


        """

        increasing = []
        for i in range(len(nums)):
            increasing.append(sum(nums[i:i+k]))

        return self._part_one(increasing)


my_solution = Solution()
print(my_solution._part_one(load_array()))
print(my_solution._part_two(load_array()))
print(my_solution._part_two_optimized(load_array()))


