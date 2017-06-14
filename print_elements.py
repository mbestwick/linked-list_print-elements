"""
Input Format
The void Print(Node* head) method takes the head node of a linked list as a
parameter. Each struct Node has a data field (which stores integer data) and a
next field (which points to the next element in the list).

Note: Do not read any input from stdin/console. Each test case calls the Print
method individually and passes it the head of a list.

Output Format
Print the integer data for each element of the linked list to stdout/console
(e.g.: using printf, cout, etc.). There should be one element per line.

"""


class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def print_list(head):
    curr = head

    while curr:
        print curr.data
        curr = curr.next
