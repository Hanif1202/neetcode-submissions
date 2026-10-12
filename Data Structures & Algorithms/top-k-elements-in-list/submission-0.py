class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums:
            if num not in hash_map:
                hash_map[num] = hash_map.get(num,1)
            else:   
                hash_map[num] = 1+ hash_map.get(num)
                
        hash_map = dict(sorted(hash_map.items(), key=lambda x: x[1], reverse=True))
        return list(hash_map)[:k]
                
        