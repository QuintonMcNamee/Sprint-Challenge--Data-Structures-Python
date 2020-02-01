from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.current == 0:
            if not self.storage.head:
                self.storage.add_to_tail(item)
            else:
                self.storage.head.value = item

        else:
            current = self.storage.head
            counter = 0
                
            while self.current > counter:
                if not current.next:
                    self.storage.add_to_tail(item)
                else:
                    current = current.next
                    counter += 1
            current.value = item
        self.current += 1

        if self.capacity <= self.current:
            self.current = 0

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        head = self.storage.head
        list_buffer_contents.append(head.value)

        while head.next != None:
            head = head.next
            list_buffer_contents.append(head.value)


        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
