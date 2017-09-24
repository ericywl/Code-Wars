class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

def push(head, data):
	n = Node(data)
	if not head:
		return n
	n.next = head
	return n

def build_one_two_three():
	head = None
	for i in xrange(3, 0, -1):
		head = push(head, i)
	return head


print push(None, 1).data
print push(Node(1), 2).data
print push(Node(1), 2).next.data

print build_one_two_three().data
print build_one_two_three().next.data
print build_one_two_three().next.next.data
print build_one_two_three().next.next.next