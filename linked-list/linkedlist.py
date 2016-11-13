
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        current = self.head
        found = False
        counter = 1
        if position < 1:
            return None
        while current and found is False:
            if counter == position:
                found = True
            else:
                current = current.next
                counter += 1
        if current is None:
            return None

        return current

    def insert_at(self, new_element, position):
        counter = 1
        current = self.head
        if position < 2:
            return None
        while current and counter < position:
            if counter == position - 1:
                new_element.next = current.next
                current.next = new_element
                current = current.next
                counter += 1
            elif position == 1:
                new_element.next = self.head
                self.head = new_element

    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next
