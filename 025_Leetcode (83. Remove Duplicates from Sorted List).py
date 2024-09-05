class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        been=[]
        while head.next:
            if head.val not in been:
                been.append(head.val)
        print(been)
        return head
print(Solution().deleteDuplicates(head = [1,1,2]))


