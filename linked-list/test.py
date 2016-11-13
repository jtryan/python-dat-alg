from node import *
from linkedlist import *

e1 = Element(2)
e2 = Element(3)
e3 = Element(5)
e4 = Element(6)


ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)


# print ll.head.next.value

# print ll.get_position(2).value

# ll.delete(5)
print ll.get_position(1).value
print ll.get_position(2).value
print ll.get_position(3).value
print "\n\n"

ll.insert(e4,2)

print ll.get_position(1).value
print ll.get_position(2).value
print ll.get_position(3).value
print ll.get_position(4).value
