# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __lt__(self,other):
        return self.val<other.val

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq=[]
        for idx,list in enumerate(lists):
            if list is not None:
                heapq.heappush(pq, (list.val,idx,list))
        
        dummy=ListNode(-1)
        curr=dummy

        while pq:
            val,idx,min_node=heapq.heappop(pq)
            curr.next=min_node
            curr=curr.next
            if min_node.next is not None:
                heapq.heappush(pq,(min_node.next.val,idx,min_node.next))
        return dummy.next


        