class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    # Convert a linked list to a number
    def linked_list_to_number(node: ListNode) -> int:
        num = 0
        while node:
            num = num * 10 + node.value
            node = node.next
        return num

    # Convert a number to a linked list
    def number_to_linked_list(num: int) -> ListNode:
        if num == 0:
            return ListNode(0)
        prev = None
        while num:
            current_digit = num % 10
            current_node = ListNode(current_digit)
            current_node.next = prev
            prev = current_node
            num //= 10
        return prev

    # Convert linked lists to numbers, add them and convert back to linked list
    num1 = linked_list_to_number(l1)
    num2 = linked_list_to_number(l2)
    total = num1 + num2
    return number_to_linked_list(total)


# Test cases
def test():
    # Helper function to convert list to ListNode
    def list_to_ListNode(nums):
        if not nums:
            return None
        return ListNode(nums[0], list_to_ListNode(nums[1:]))

    # Helper function to print ListNode
    def print_list(node):
        while node:
            print(node.value, end="->" if node.next else "\n")
            node = node.next

    l1 = list_to_ListNode([1, 2, 3])
    l2 = list_to_ListNode([4, 5, 6])
    print_list(addTwoNumbers(l1, l2))  # 5->7->9

    l1 = list_to_ListNode([1, 2, 3])
    l2 = list_to_ListNode([5, 6])
    print_list(addTwoNumbers(l1, l2))  # 1->7->9

    l1 = list_to_ListNode([1, 5])
    l2 = list_to_ListNode([1, 7, 7])
    print_list(addTwoNumbers(l1, l2))  # 1->9->2

    l1 = list_to_ListNode([9, 9, 9])
    l2 = list_to_ListNode([1])
    print_list(addTwoNumbers(l1, l2))  # 1->0->0->0


test()
