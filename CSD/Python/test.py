#create brute force solution
def create_brute_force_solution(n):
    head = Node(n[0])
    tail = head
    for i in range(1,len(n)):
        tail.next = Node(n[i])
        tail = tail.next
    return head
