#Queues are another form of linear data structure very similar to stacks.
#The difference is queues follow the FIFO rule - First In First Out, much like real life queues,
#Where the person gets in first, gets to leave first.
#Quesues can be implemented with both arrays and linked lists but the array implementation is not eficient
#Because for removing an element from the queues, which happens from the front of the array(queue),
#the indices of the array have to be updated every time, essentially making it an O(n) operation,
#Whereas the same operation can be done in O(1) time with linked lists.
#Queues have enqueue and dequeue operations which correspond to the push and pop operations of stacks , only difference being dequeue removes element from the front
#Time complexities are as follows:
#Peek - O(1)
#Enqueue - O(1)
#Dequeue - o(1)

import os

#Like for stacks, we need a node class which will contain the data and a pointer to the next node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


#Next we need the Queue class itself which will contain a constructor initialising the queue and then the methods we require
class Queue:

#The 'first' pointer will always point to the front of the queue, the element which is to be removed next that is
#The 'last' pointer will always point to the end of the queue, i.e., the element which has last been entered
    def __init__(self):
        self.first = None
        self.rear = None
        self.length = 0

#Now comes the peek method which will return the element at the front of the queue
    def peek(self):
        if self.is_empty():
            return None
        return self.first.data

    def is_empty(self):
        return self.length == 0

    def __len__(self):
        return self.length

#The enqueue operation will add an element at the end of the queue
#If the queue is empty, it will make both the first and last pointer point to the new node
#Else, if you will first make the next of the new node to point to the present last node and then it will update the last node to point to the new node
#Time complexity will be O(1)
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.rear = new_node
            self.first = self.rear
            self.length += 1
            return
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.length += 1
            return


#Next comes the dequeue operation which removes the front element of the queue
#If the queue is empty, it will print an appropriate message
#Else, it will simply make the first pointer point to the next element of the first pointer.
    def dequeue(self):
        if self.is_empty():
            print("Queue Empty")
            return None  # Return None explicitly to handle empty queue safely

        dequeued_value = self.first.data  # Store data before removal

        if self.rear == self.first:  # If only one element is present
            self.rear = None
            self.first = None
        else:
            self.first = self.first.next  # Move front pointer

        self.length -= 1
        return dequeued_value  # Return the dequeued value

#Finally we'll create the print method which prints the elements of the queue in, well, a queue like format
    def print_queue(self):
        if self.length == 0:
            print("Queue Empty")
            return
        else:
            current_pointer = self.first
            while current_pointer is not None:
                if current_pointer.next is None:
                    print(current_pointer.data)
                else:
                    print(f'{current_pointer.data}  <<--  ', end='')
                current_pointer = current_pointer.next
            return


    def __repr__(self):
        if self.is_empty():
            return "Queue is empty"
        elements = []
        current = self.first
        while current:
            elements.append(str(current.data))
            current = current.next
        return " <- ".join(elements)

def options():

    options_list = ['Enqueue', 'Dequeue', 'Peek',
                    'Display Queue', 'Exit']

    print("MENU")
    for i, option in enumerate(options_list):
        print(f'{i + 1}. {option}')

    choice_val = int(input("Enter choice: "))
    return choice_val


def switch_case(choice):

    os.system('cls')
    if choice == 1:
        elem = int(input("Enter item to Enqueue: "))
        Q.enqueue(elem)

    elif choice == 2:
        print('Dequeued item is: ', Q.dequeue())

    elif choice == 3:
        print("First item is: ", Q.peek())

    elif choice == 4:
        print("Queue: ")
        Q.print_queue()
        print("\n")

    elif choice == 5:
        import sys
        sys.exit()

###############################################################################


if __name__ == '__main__':
    Q = Queue()
    while True:
        choice = options()
        switch_case(choice)

