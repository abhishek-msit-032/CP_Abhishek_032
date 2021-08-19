"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        # Your code goes here
        new = self.head
        while new.next != None:
            new = new.next
        new.next = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # Your code goes here
        c = 1
        new = self.head
        if position < 1:
            return None

        while new and c <= position:
            if c == position:
                return new
            new = new.next
            c = c+1
        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # Your code goes here

        c = 1
        new = self.head
        if position > 1:
            while new and c < position:
                if c == position - 1:
                    new_element.next = new.next
                    new.next = new_element
                new = new.next
                c += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete(self, value):
        """Delete the first node with a given value."""
        # Your code goes here
        new = self.head
        previous = None
        while new.value != value and new.next:
            previous = new
            new = new.next
        if new.value == value:
            if previous:
                previous.next = new.next
            else:
                self.head = new.next
