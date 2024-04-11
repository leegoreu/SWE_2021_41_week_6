from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    number_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in number_index:
            return [number_index[complement], i]
        number_index[num] = i 
