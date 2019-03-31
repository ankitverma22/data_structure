
'''
node(data,next node)
singlylinked list(add at start,end ,print)

'''

class Node:
    def __init__(self, data,next):
        self.data = data
        self.next = next


class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def add_at_beginning(self, data):
        self.head = Node(data, self.head)
        self.length += 1

    def add_at_end(self, data):
        if self.head ==None:
            self.head = Node(data, self.head)
            self.length +=1
            return

        temp = self.head


        while temp.next:
            temp = temp.next

        temp.next = Node(data, None)
        self.length += 1

    def delete(self, value):
        if not self.head:
            return

        temp = self.head
        # deleting head node
        if self.head.data is value:
            self.head = self.head.next
            temp.next = None
            temp = None
            return

        # deleting intermediate node
        prev = None
        while temp:
            if temp.data is value:
                prev.next = temp.next
                temp.next = None
                temp = None
                break

            prev = temp
            temp = temp.next


    def print_list(self):
        temp = self.head
        # for i in range(self.length ):
        #     print(temp.data, end=',')
        #     temp = temp.next
        while temp:
            print(temp.data, end=',')
            temp = temp.next



def main():
    singly_linked_list = SinglyLinkedList()
    for i in range(12):
        singly_linked_list.add_at_beginning(i)
        # singly_linked_list.print_list()
        # print("  ",singly_linked_list.length)

        # singly_linked_list.delete(4)
        # singly_linked_list.print_list()
        # singly_linked_list.delete(13)
        # singly_linked_list.print_list()
        # singly_linked_list.delete(5)
        # singly_linked_list.print_list()



    singly_linked_list.print_list()

if __name__ == '__main__':
    main()