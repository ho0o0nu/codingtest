class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)


    def put(self, key: int, value: int) -> None:
        index = key % self.size
        
        # 인덱스에 노드가 존재하지 않는 경우 삽입 후 종료
        if not self.table[index].value:
            self.table[index] = ListNode(key, value)
            return
        
        # 인덱스에 노드가 존재하는 경우 연결 리스트 처리
        p = self.table[index]  # 인덱스의 첫 번째 값
        while p:
            if p.key == key:  # 이미 put과 get이 이루어져서 키가 존재?
                p.value = value
                return
            if not p.next:  # 다음 p가 존재하지 않는 경우
                break
            p = p.next
        p.next = ListNode(key, value) # 새 노드 연결         


    def get(self, key: int) -> int:
        index = key % self.size
        if not self.table[index].value:
            return -1
        
        # 노드가 존재하는 경우
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1


    def remove(self, key: int) -> None:
        index = key % self.size
        if not self.table[index].value:
            return
        
        # 인덱스의 첫 번째 노드인 경우
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if not p.next else p.next
            return

        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next
            

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)