class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        number1=[]
        answer=''
        x=ListNode()
        while head:
            number1.append(head.val)
            head=head.next
        number1=sorted(list(set(number1)))
        strnumber1 = map(str, number1)
        print(number1)
        answer=','.join(strnumber1)
        return ListNode(answer)