def printLinkedList(head):   
    if head:
        print(head.data)
        return(printLinkedList(head.next))
if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    printLinkedList(llist.head)
