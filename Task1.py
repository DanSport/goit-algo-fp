class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse_list(self):
        prev = None
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev

    def sorted_insert(self, new_node: Node):
        if self.head is None or self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
            return
        cur = self.head
        while cur.next and cur.next.data < new_node.data:
            cur = cur.next
        new_node.next = cur.next
        cur.next = new_node


    def sort_list(self):
        sorted_list = LinkedList()
        cur = self.head
        while cur:
            next_node = cur.next
            sorted_list.sorted_insert(cur)
            cur = next_node
        self.head = sorted_list.head



    def merge_sorted_lists(self, list2: 'LinkedList') -> 'LinkedList':
        merged_list = LinkedList()
        cur1 = self.head
        cur2 = list2.head

        while cur1 and cur2:
            if cur1.data < cur2.data:
                merged_list.sorted_insert(Node(cur1.data))
                cur1 = cur1.next
            else:
                merged_list.sorted_insert(Node(cur2.data))
                cur2 = cur2.next

        while cur1:
            merged_list.sorted_insert(Node(cur1.data))
            cur1 = cur1.next
        while cur2:
            merged_list.sorted_insert(Node(cur2.data))
            cur2 = cur2.next

        return merged_list




llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

# Реверсування списку
print("\nРеверсований зв'язний список:")
llist.reverse_list()
llist.print_list()

# Сортування списку
print("\nВідсортований зв'язний список:")
llist.sort_list()
llist.print_list()

# Об'єднання двох відсортованих списків
llist2 = LinkedList()
llist2.insert_at_beginning(3)
llist2.insert_at_beginning(8)
llist2.insert_at_end(18)
llist2.insert_at_end(21)
print("\nПерший відсортований список:")
llist.print_list()
print("Другий відсортований список:")
llist2.sort_list()
llist2.print_list()
print("\nОб'єднаний відсортований список:")
merged = llist.merge_sorted_lists(llist2)
merged.print_list()



