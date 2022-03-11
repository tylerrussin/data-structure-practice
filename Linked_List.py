# Linked list from scratch
from cgi import test


class Node():

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList():

    def __init__(self):
        self.head = Node()
        self.tail = self.head
    
    def add_node(self, val=0):
        self.tail.next = Node(val)  # Initiate new node
        self.tail = self.tail.next  # Add node to end of list

    def remove_node(self):
        current_node = self.head    # Start at head

        # Iterate till at tail node O(n) time-complexity
        while current_node.next != None:
            prev_node = current_node
            current_node = current_node.next

        prev_node.next = None   # Remove tail node

    def __str__(self):
        current_node = self.head    # Start at head
        running = True
        output_str = ''

        # Iterate through whole list
        while running:
            output_str += '{} -> '.format(current_node.val)     # Creating output str

            # Checking if tail has been hit
            if current_node.next == None:
                running = False
            else:
                current_node = current_node.next

        print(output_str)


    def find_value(self, val):
        current_node = self.head    # Start at head

        # Iterate till node with value is found
        while current_node.next != None:

            # Checking for current val
            if current_node.val == val:
                return current_node
            else:
                current_node = current_node.next

        # If value does not exist
        return None

    def length(self, node):
        count = 1
        while node.next != None:
            count += 1
            node = node.next

    def sort_list(self):

        def merge_sort(self, current_node):
            pass


        merge_sort(self.head)
        


if __name__ == '__main__':

    # Input Data
    data = [3,4,2,7,1,9,4]

    test_list = LinkedList()

    test_list.__str__()

    for val in data:
        test_list.add_node(val)

    test_list.__str__()

    test_list.remove_node()

    test_list.__str__()





        


    
        

