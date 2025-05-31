class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []

        # 힙에 음수로 삽입(최대값을 뽑기 위해)
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))
        
        topk = list()
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])
        
        return topk