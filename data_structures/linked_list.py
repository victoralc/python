class Node:

    """
    An object for storing a single node of a linked list.
    Models two attributes - date and the link to the next node in the list
    """

    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return "<Node date: %s>" % self.data


class LinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, data):
        """
        Adds a new node containing date at the head of the list
        Constant Time O(1)
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def size(self):
        """
        Returns the number of the nodes in the list takes O(n) time
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count

    def insert(self, data, index):
        """
        Insert O(1)
        Find a node O(n)
        Takes overall time O(n)
        """
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)
        position = index
        current = self.head

        while position > 1:
            current = node.next_node
            position -= 1

        prev_node = current
        next_node = current.next_node

        prev_node.next_node = new
        new.next_node = next_node

    def search(self, key):
        """
        Search for the first node containing date that matches the key
        Returns the node or None if not found
        Complexity Time: Linear Time O(n)

        """
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def remove(self, key):

        """
        Return Node containing data that matches the key
        Returns the node or None if key doesn't exist
        Takes O(n) time
        """

        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                previous.next_code = current.next_node
            else:
                previous = current
                current = current.next_node

        return current

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return '-> '.join(nodes)