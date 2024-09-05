class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, firstlist: list, secondlist: list) -> list:
        list1 = []
        list2 = []
        while firstlist:
            list1.append(firstlist.val)
            firstlist = firstlist.next
        while secondlist:
            list2.append(secondlist.val)
            secondlist = secondlist.next
        subanswer = sorted(list1 + list2)
        subanswer = map(str, subanswer)
        answer = ListNode(','.join(subanswer))
        return answer

print(Solution().mergeTwoLists([],[]))