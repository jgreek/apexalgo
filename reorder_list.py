class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def findMiddle(head):
    """Find the middle of the linked list using Floyd's algorithm."""
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def reverseList(head):
    """Reverse a linked list."""
    prev = None
    while head:
        next_temp = head.next
        head.next = prev
        prev = head
        head = next_temp
    return prev


def mergeLists(l1, l2):
    """Merge two lists in the desired order."""
    while l1 and l2:
        l1_next = l1.next
        l2_next = l2.next

        l1.next = l2
        if l1_next:
            l2.next = l1_next

        l1 = l1_next
        l2 = l2_next


def reorderList(head):
    """Reorder the linked list as per the problem statement."""
    # Base condition to check if head is None or has only one node
    if not head or not head.next:
        return

    # Find the middle and split the linked list into two halves
    middle = findMiddle(head)
    first_half = head
    second_half = middle.next
    middle.next = None

    # Reverse the second half
    second_half = reverseList(second_half)

    # Merge the two halves
    mergeLists(first_half, second_half)


def display(head):
    """Utility function to display the linked list."""
    elements = []
    while head:
        elements.append(str(head.val))
        head = head.next
    print(" -> ".join(elements))


# Test cases
# Creating linked list from list [1,2,3,4]
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4

print("Original List:")
display(node1)

reorderList(node1)
print("Reordered List:")
display(node1)

# Creating linked list from list [1,2,3,4,5]
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("\nOriginal List:")
display(node1)

reorderList(node1)
print("Reordered List:")
display(node1)
