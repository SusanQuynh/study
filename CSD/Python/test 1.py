#create double linked list
def create_double_linked_list(n):
    head = Node(n[0])
    tail = head
    for i in range(1,len(n)):
        tail.next = Node(n[i])
        tail.next.prev = tail
        tail = tail.next
    return head
def update_double_linked_list(head,n):
    tail = head
    for i in range(len(n)):
        tail.data = n[i]
        tail = tail.next
    return head