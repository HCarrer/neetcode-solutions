class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		count = {}
		for num in nums:
			if num in count:
				count[num] += 1
			else:
				count[num] = 1
		
		freq = [[] for i in range(len(nums) + 1)]
		for index, count in count.items():
			freq[count].append(index)
   
		res = []
		for i in range(len(freq) - 1, 0, -1):
			for n in freq[i]:
				res.append(n)
				if len(res) == k:
					return res