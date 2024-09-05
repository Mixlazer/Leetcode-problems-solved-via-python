class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        number1=[]
        answer=''
        x=ListNode()
        while head:
            number1.append(str(head.val))
            head=head.next
        if len(number1)<n:
            return ListNode(answer)
        number1.pop((-n))
        answer=','.join(list(number1))
        return ListNode(answer)

