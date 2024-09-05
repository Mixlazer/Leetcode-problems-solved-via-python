class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number1=[]
        number2=[]
        total=''
        str1=''
        str2=''
        x=ListNode()
        while l1:
            number1.append(str(l1.val))
            l1=l1.next
        while l2:
            number2.append(str(l2.val))
            l2=l2.next
        str1=''.join(list(reversed(number1)))
        str2=''.join(list(reversed(number2)))
        print(str1, str2)
        subtotal=str(int(str1)+int(str2))
        total=','.join(list(reversed(subtotal)))
        return ListNode(total)