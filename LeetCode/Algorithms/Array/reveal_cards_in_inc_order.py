import collections
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        ans = [0]*len(deck)
        deq = collections.deque([x for x in range(len(deck))])
        deck.sort()
        for i in range(len(deck)):
            top = deq.popleft()
            ans[top] = deck[i]
            if len(deq):
                below = deq.popleft()
                deq.append(below)
        return ans