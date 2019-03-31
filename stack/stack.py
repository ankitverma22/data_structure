class StackNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

# add a element in the stack
class Stack:
    def __init__(self):
        self.root = None

    def isempty(self):
        return True if self.root is None else False

#deleate an elemant on stack
    def push(self, data):
        self.root = StackNode(data, self.root)
        print("%d pushed to stack"%(data))

    def pop(self):
        if self.root is None:
            return float("-inf")
        temp = self.root
        self.root = self.root.next
        popped  = temp.data
        return popped

    def peek(self):
        if self.root is None:
            return float("")
        return self.root.data

def main():
    stack = Stack()
    stack.push(20)
    stack.push(30)
    print(stack.pop())
    print(stack.isempty())
    print(stack.peek())

if __name__ == '__main__':
    main()