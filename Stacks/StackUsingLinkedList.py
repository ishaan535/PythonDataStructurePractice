#Stacks are linear data-structures which can be implemented using either stacks or linked lists
#Insertion and deletion of elements in a stack take place from one end only.
#Stacks follow the LIFO rule - Last In First Out, where the last element that is inserted, is the first element that comes out.
#The main operations that can be performed on a stack , with their time complexities are as follows:
#Push (Insert) - O(1)
#Pop (Remove) - O(1)
#Peek (Retrieve the top element) - O(1)
import os


#Here we'll implement a stack using linked lists

#Linked Lists are made of nodes. So we create a node class.
#It will contain the data and the pointer to the next node.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Now we create the Stack class
#It will consist of a constructor having the top pointer, i.e., the pointer which points to the top element of the stack at any given time
#The length variable which keeps track of the length of the stack, and a bottom pointer which points to bottom most element of the stack
#After this will come the methods associated with a stack
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    # Next comes the push operation, where we insert an element at the top of the stack
    # Again this only requires access to the top pointer and involves no looping.
    # So time complexity is O(1)
    def push(self, data):
        self.size +=1
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Next comes the pop operation where we remove the top element from the stack
    # Its time complexity is O(1) as well
    def pop(self):
        if self.head is None:#If the stack is empty, we print an appropriate message
            print("Stack empty")
            return None
        else:#Else we make the top pointer point to the next of the top pointer and decrease the length by 1, effectively deleting the top element.
            popped = self.head.data
            self.head = self.head.next
            self.size -= 1
            return popped

    # The peek method will allow us to peek at the top element,i.e.,
    # It will return the element at the top of the stack without removing it from the stack.
    # Since for this we only need to see what the top pointer points at, the time complexity will be O(1)
    def peek(self):
        if self.head is None:
            return None
        return self.head.data

    def is_empty(self):
        return self.head is None

    def __len__(self):
        return self.size

    # Finally we'll implement a print method which prints the elements of the stack from top to bottom
    # This will be an O(n) operation as we'll obviously have to traverse the entire linked list to print all elelments
    def print_stack(self):
        if self.head is None:
            print("Stack empty")
        else:
            current_pointer = self.head
            while current_pointer is not None:
                print(current_pointer.data)
                current_pointer = current_pointer.next

def options():

    options_list = ['Push', 'Pop', 'Peek',
                    'Display Stack', 'Length', 'Exit']

    print("MENU")
    for i, option in enumerate(options_list):
        print(f'{i + 1}. {option}')

    ch = int(input("Enter choice: "))
    return ch


def switch_case(choice_val):

    os.system('cls')
    if choice_val == 1:
        elem = input("Enter Item: ")
        stack.push(int(elem))

    elif choice_val == 2:
        print('Popped item is: ', stack.pop())

    elif choice_val == 3:
        print("Item on peek is: ", stack.peek())

    elif choice_val == 4:
        print("Stack: ", end='')
        stack.print_stack()
        print("\n")

    elif choice_val == 5:
        print("Stack Length is: ", len(stack))

    elif choice_val == 6:
        import sys
        sys.exit()


if __name__ == '__main__':
    stack = Stack()
    while True:
        choice = options()
        switch_case(choice)
