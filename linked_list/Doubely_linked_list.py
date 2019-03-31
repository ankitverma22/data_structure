class Node:
    def __init__(self, data, prev =None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DoubelyLinkedLest:
    def __init__(self):
        self.head = None

    def add_at_beginnning(self,new_data):
        # self.head = Node(data, None, self.head)
        new_node = Node(data = new_data)
        new_node.next = self.head
        new_node.prev = None
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("the given previous node is not null")
            return

        new_node = Node(data = new_data,)
        # new_node.prev =prev_node
        new_node.next = prev_node.next
        prev_node.next= new_node
        new_node.prev = prev_node

        if new_node.next is not None:
            new_node.next.prev = new_node

    def add_at_last(self, new_data):
        new_node = Node(new_data)
        new_node.next = None
        temp = self.head
        while(temp):
            temp = self.head.next
            # self.head = self.head.next
        new_node.prev = temp
        temp.next = new_node

    def deleate(self,node):
        if self.head is None or node is None:
            return
        if self.head == node:
            self.head = self.head .next

    def insert_in_the_sorted_way(self, new_data):
        if self.head.data > new_data:
            self.add_at_beginnning(new_data)
            return

        temp = self.head.next
        while temp :
            if temp.data >new_data:
                self.insert_after(temp.prev, new_data)
                return
            temp = temp.next



    def PrintDLL(self):
        temp = self.head
        while (temp):
            print(temp.data,end =  ',')
            temp = temp.next


def main():
    Doubely_linked_list = DoubelyLinkedLest()
    Doubely_linked_list.add_at_beginnning((77))
    Doubely_linked_list.add_at_beginnning(44)

    Doubely_linked_list.add_at_beginnning(33)
    Doubely_linked_list.add_at_beginnning(31)
    # Doubely_linked_list.insert_after(,55)
    # Doubely_linked_list.insert_after(Doubely_linked_list.head.next,55)
    Doubely_linked_list.insert_in_the_sorted_way(34)
    Doubely_linked_list.PrintDLL()
    print("""aaaa""")
    Doubely_linked_list.deleate(Doubely_linked_list.head)
    # Doubely_linked_list.add_at_last(11)
    Doubely_linked_list.PrintDLL()
    # print(Doubely_linked_list.)

if __name__ == '__main__':
    main()