class NonExistentNodeError(Exception):
    def __init__(self, message="Node does not exist"):
        self.message = message
        super().__init__(self.message)


class Node:
    def __init__(self, value=None) -> None:
        self.next = None
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.__current = self.head

    def __iter__(self):
        while self.__current:
            current = self.__current
            self.__current = self.__current.next
            yield current

        self.__current = self.head

    def __str__(self) -> str:
        pass

    def __len__(self) -> int:
        pass

    @property
    def values(self) -> list(object):
        pass

    def reverse(self) -> None:
        pass

    def print_list(self) -> None:
        pointer = self.head

        while pointer is not None:
            print(pointer.value)
            pointer = pointer.next

    def insert_head(self, head_value) -> None:
        new_node = Node(head_value)
        new_node.next = self.head
        self.head = new_node

    def insert_tail(self, tail_value) -> None:
        new_node = Node(tail_value)

        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next

            last.next = new_node

    def insert_after(self, target_node, after_value) -> None:
        if target_node is None:
            raise NonExistentNodeError

        new_node = Node(after_value)
        new_node.next = target_node.next
        target_node.next = new_node

    def insert_before(self, target_node, before_value) -> None:
        if target_node is None:
            raise NonExistentNodeError

        new_node = Node(before_value)
        new_node.next = target_node

        pointer = self.head

        while pointer.next is not target_node:
            pointer = pointer.next

        pointer.next = new_node

    def delete_node(self, target_value) -> None:
        pointer = self.head

        if pointer is not None:
            if pointer.value == target_value:
                self.head = pointer.next
                pointer = None
                return

        while pointer is not None:
            if pointer.value == target_value:
                break

            previous_node = pointer
            pointer = pointer.next

        if pointer == None:
            return

        previous_node.next = pointer.next
        pointer = None

    def pop_head(self) -> Node:
        pointer = self.head

        self.head = pointer.next
        return pointer

    def pop_tail(self) -> Node:
        pointer = self.head
        previous = None

        while pointer.next:
            previous = pointer
            pointer = pointer.next

        previous.next = None
        return pointer

    def get(self, index) -> object:
        pass


# class LinkedList:
#     def __init__(self, values=None):
#         self.head = None
#         self.tail = None
#         if values is not None:
#             self.add_multiple_nodes(values)
#     def __str__(self):
#         return ' -> '.join([str(node) for node in self])
#     def __len__(self):
#         count = 0
#         node = self.head
#         while node:
#             count += 1
#             node = node.next
#         return count
#     def __iter__(self):
#         current = self.head
#         while current:
#             yield current
#             current = current.next
#     @property
#     def values(self):
#         return [node.value for node in self]
#     def add_node(self, value):
#         if self.head is None:
#             self.tail = self.head = Node(value)
#         else:
#             self.tail.next = Node(value)
#             self.tail = self.tail.next
#         return self.tail
#     def add_multiple_nodes(self, values):
#         for value in values:
#             self.add_node(value)
#     def add_node_as_head(self, value):
#         if self.head is None:
#             self.tail = self.head = Node(value)
#         else:
#             self.head = Node(value, self.head)
#         return self.head

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_head(5)
    print(type(ll.head))
