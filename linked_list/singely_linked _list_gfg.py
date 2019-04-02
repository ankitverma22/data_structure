class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class SingeyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def add_at_beginning(self, data):
        self.head = Node(data, self.head)
        self.length += 1

    # def deleate(self,key):
    #     self.length -=1
    #     if  not self.head:
    #         return
    #     temp = self.head
    #     # deleating first node
    #     if  self.head is key:
    #         self.head =self.head.next
    #         temp.next = None
    #         temp= None
    #         return
    #     # deleate at intermeidate node
    #     while temp:
    #         if temp.data is key:
    #             prev.next = temp.next
    #             temp.next = None
    #             temp = None
    #
    #     temp= temp.next
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
    def reversed(self):
        temp = self.head
        reversed_SLL = SingeyLinkedList()
        while temp:
            reversed_SLL.add_at_beginning(temp.data)
            temp= temp.next
        return reversed_SLL.print_list()


    def get_Nth_node(self, n):
        count = 0
        temp= self.head
        while temp:
            if(count== n):
                return temp.data
            count += 1
            temp = temp.next




    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end= ',')
            temp = temp.next

def main():
    Singely_linked_list = SingeyLinkedList()
    # for i in range(12):
    Singely_linked_list.add_at_beginning(30)
    Singely_linked_list.add_at_beginning(31)
    Singely_linked_list.add_at_beginning(32)
    Singely_linked_list.add_at_beginning(33)
    Singely_linked_list.add_at_beginning(34)
    Singely_linked_list.add_at_beginning(36)
    print(Singely_linked_list.get_Nth_node(3))
    Singely_linked_list.reversed()
    b=4
    # print(Singely_linked_list.get_Nth_node(b))
    # Singely_linked_list.delete(31)
    print("\n")
    Singely_linked_list.print_list()


if __name__ == '__main__':
    main()