#!/usr/bin/env python3

# reverse reading of the link

#convert to link
#rever output
class Link():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def output_reverse_array_with_link(self, input_array):

        # for i in range(0, len(input_array)):
        #   j = len(input_array) - 1 -i
        #       node = Link(v, None)

        if input_array is None:
            return

        head = Link(None)
        first = head
        for v in input_array:
            node = Link(v, None)
            head.next = node
            head = node

        def read_link(head):
            if head is None: return
            read_link(head.next)
            if head.val != None:
                print(head.val)


        read_link(first)


        # O(n)

Solution().output_reverse_array_with_link(None)