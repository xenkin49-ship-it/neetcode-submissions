class ListNode:
    def __init__(self,node):
        self.node=node
        self.next = None


class MyHashSet:

    def __init__(self):
        self.arr = [ListNode(0)for _ in range(10**4)]

    def add(self, key: int) -> None:
        index = key % len(self.arr)
        curr = self.arr[index]
        while curr.next:
            if curr.next.node == key:
                return 
            curr = curr.next
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = key%len(self.arr)
        curr = self.arr[index]
        while curr.next:
            if curr.next.node == key:
                curr.next.node = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        index = key % len(self.arr)
        curr = self.arr[index]
        while curr.next:
            if curr.next.node == key:
                return True
            curr = curr.next
        return False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)