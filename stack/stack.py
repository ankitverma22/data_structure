class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        self.top = Node(data, self.top)

    def pop(self):
        if self.top:
            poped_node = self.top.data
            self.top = self.top.next
            return poped_node
        else:
            return -1


def main():
    stack = Stack()
    for i in range(10):
        stack.push(i)

    for i in range(12):
        print(stack.pop())


if __name__ == "__main__":
    main()




