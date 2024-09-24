class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map=Counter(nums)
        heap=[]

        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq,num))
            if len(heap)>k:
                heapq.heappop(heap)
        result=[]
        while heap:
            result.append(heapq.heappop(heap)[1])
        return result[::-1]