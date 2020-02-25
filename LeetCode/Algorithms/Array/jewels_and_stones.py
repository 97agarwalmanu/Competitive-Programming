class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        num_jewels = 0
        jewel_list = list(J)
        for stone in S:
            if stone in jewel_list:
                num_jewels += 1
        return num_jewels