class Solution:
	def twoSum(self, nums, target):
		for i in range(len(nums)):
			for j in range(len(nums)):
				if ((nums[i] + nums[j]) == target) and (i != j):
					r = [j, i]
		return r
