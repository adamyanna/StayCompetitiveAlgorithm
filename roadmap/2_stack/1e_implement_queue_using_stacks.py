#!/usr/bin/env python3

"""
implement-queue-using-stacks
"""


class Solution(object):
    # simulate_stack_with_two_queues
    # use python list to simulate queue
    # use list len to simulate return of queue size
    # pop[0] remove element from queue head
    # append add element from queue tail
    # stack push 1,2,3
    # queue a [1, 2, 3]
    # queue b []
    # pop -> first element = 3
    # queue a pop 1, 2 into queue b
    # queue b last element is stack pop element
    def __init__(self):
        self.sim_queue_a = []
        self.sim_queue_b = []

    # if needed
    # implement a size variable to access queue size (list length)
    # def get_queue_a_size()

    # push、top、pop 和 empty

    def push(self, new_element):
        if len(self.sim_queue_a) == 0 and len(self.sim_queue_b) == 0:
            self.sim_queue_a.append(new_element)
        else:
            # push to stack
            if len(self.sim_queue_a) > 0:
                self.sim_queue_a.append(new_element)
            else:
                self.sim_queue_b.append(new_element)

    def top(self):
        # return top element of stack
        # use list len to simulate return of queue size
        result = None
        if len(self.sim_queue_a) > 0:
            while len(self.sim_queue_a) > 0:
                temp = self.sim_queue_a.pop(0)
                self.sim_queue_b.append(temp)
                if len(self.sim_queue_a) == 0:
                    result = temp
        else:
            while len(self.sim_queue_b) > 0:
                temp = self.sim_queue_b.pop(0)
                self.sim_queue_a.append(temp)
                if len(self.sim_queue_b) == 0:
                    result = temp

        return result

    def pop(self):
        # return top element of stack
        # use list len to simulate return of queue size
        if len(self.sim_queue_a) > 0:
            while len(self.sim_queue_a) > 0:
                temp = self.sim_queue_a.pop(0)
                if len(self.sim_queue_a) == 0:
                    return temp
                self.sim_queue_b.append(temp)
        else:
            while len(self.sim_queue_b) > 0:
                temp = self.sim_queue_b.pop(0)
                if len(self.sim_queue_b) == 0:
                    return temp
                self.sim_queue_a.append(temp)

    def empty(self):
        if len(self.sim_queue_a) == 0 and len(self.sim_queue_b) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    # 例如输入数组1、2、4、7、11、15和数字15。由于4+11=15，因此输出4和11。
    # print(Solution().get_sum_of_number([1, 2, 4, 7, 11, 15], 15))

    # 输入：
    # ["MyStack", "push", "push", "top", "pop", "empty"]
    # [[], [1], [2], [], [], []]
    # 输出：
    # [null, null, null, 2, 2, false]

    stack = Solution()
    print(stack.push(1))
    print(stack.push(2))
    print(stack.top())
    print(stack.top())
    print(stack.empty())