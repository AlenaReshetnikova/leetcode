# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two
# lists.
#
# Return the head of the merged linked list.
#
# Example 1:
#     Input: list1 = [1,2,4], list2 = [1,3,4]
#     Output: [1,1,2,3,4,4]
# Example 2:
#     Input: list1 = [], list2 = []
#     Output: []
# Example 3:
#     Input: list1 = [], list2 = [0]
#     Output: [0]
from random import randint


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def list_to_listnode(l: list):
    head = tail = None
    for i in l:
        if not head:
            head = ListNode(i)
            tail = head
        else:
            tail.next = ListNode(i)
            tail = tail.next
    return head


# def mergeTwoLists(list1, list2):
#     return sorted(list1 + list2)


# tests = [
#     [[1, 2, 4, 5], [1, 3, 4]],
#     [[randint(-100, 100) for _ in range(50)], [randint(-100, 100) for _ in range(50)]],
#     [[randint(-100, 100) for _ in range(50)], [randint(-100, 100) for _ in range(50)]],
#     [[], []],
#     [[], [0]]
# ]
# for test in tests:
#     print(mergeTwoLists(test[0], test[1]))


# while ListNode_1:
#     print(ListNode_1.val)
#     ListNode_1 = ListNode_1.next


def mergeTwoLists(list1, list2):
    def to_node(num):
        nonlocal head, tail
        if not head:
            head = ListNode(num)
            tail = head
        else:
            tail.next = ListNode(num)
            tail = tail.next

    head = tail = None
    while True:
        if list1 and list2:
            if list1.val > list2.val:
                to_node(list2.val)
                list2 = list2.next
            else:
                to_node(list1.val)
                list1 = list1.next
        if not list1 and list2:
            while list2:
                to_node(list2.val)
                list2 = list2.next
        if list1 and not list2:
            while list1:
                to_node(list1.val)
                list1 = list1.next
        if not list1 and not list2:
            return head


# def mergeTwoLists_2(list1, list2):
#     def add_node(value: int):
#         nonlocal head, tail
#         if not head:
#             head = ListNode(value)
#             tail = head
#         else:
#             tail.next = ListNode(value)
#             tail = tail.next
#
#     head = tail = None
#     while True:
#         if list1 and list2:
#             if list1.val > list2.val:
#                 add_node(list2.val)
#                 list2 = list2.next
#             else:
#                 add_node(list1.val)
#                 list1 = list1.next
#         if not list1 and list2:
#             while list2:
#                 add_node(list2.val)
#                 list2 = list2.next
#         if list1 and not list2:
#             while list1:
#                 add_node(list1.val)
#                 list1 = list1.next
#         if not list1 and not list2:
#             return head


tests = [
    [[1, 2, 4, 5], [1, 3, 4]],
    [sorted([randint(-100, 100) for _ in range(50)]), sorted([randint(-100, 100) for _ in range(50)])],
    [sorted([randint(-100, 100) for _ in range(50)]), sorted([randint(-100, 100) for _ in range(50)])],
    [[], []],
    [[], [0]]
]
for test in tests:
    ListNode_1 = list_to_listnode(test[0])
    ListNode_2 = list_to_listnode(test[1])
    print(test[0])
    print(test[1])
    print(mergeTwoLists(ListNode_1, ListNode_2))
    print()
