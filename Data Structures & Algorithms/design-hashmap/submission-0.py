class ListNode:
    def __init__(self,key=-1,val=-1):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.arr = [ListNode() for _ in range(10**4)]
    
    def hash(self, key):
        index = key % len(self.arr)
        return index

    def put(self, key: int, value: int) -> None:
        curr = self.arr[self.hash(key)]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = ListNode(key,value)

    def get(self, key: int) -> int:
        curr = self.arr[self.hash(key)]
        while curr.next:
            if curr.next.key == key:
                return curr.next.val 
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        curr = self.arr[self.hash(key)]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)