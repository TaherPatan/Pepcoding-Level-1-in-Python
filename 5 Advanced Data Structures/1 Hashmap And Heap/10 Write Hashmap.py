class ListNode:
    def __init__(self, key, val):
        self.key, self.value = key, val
        self.next = None


class MyHashMap:
    def __init__(self):
        self.max_size = 4
        self.hashtable = [None] * self.max_size
        self.size = 0

    def __setitem__(self, key, value):
        print(self.max_size)
        index = hash(key) % 4
        if not self.hashtable[index]:
            self.hashtable[index] = ListNode(key, value)
            self.size += 1
        else:
            cur = self.hashtable[index]
            while True:
                if cur.key == key:
                    cur.value = value
                    return
                if not cur.next:
                    break
                cur = cur.next
            cur.next = ListNode(key, value)
        loading_factor = self.size // self.max_size
        if 2 <= loading_factor:
            new_hashtable = self.hashtable
            self.hashtable = [None] * (self.max_size * 2)
            for bucket in new_hashtable:
                while bucket:
                    self[bucket.key] = bucket.value
                    bucket = bucket.next
            del new_hashtable

    def __getitem__(self, key):
        index = hash(key) % self.max_size
        cur = self.hashtable[index]
        while cur:
            if cur.key == key:
                return cur.value
            else:
                cur = cur.next
        return 'null'

    def remove(self, key):
        index = hash(key) % self.max_size
        cur = prev = self.hashtable[index]
        if not cur:
            return 'null'
        if cur.key == key:
            return_val = cur.value
            self.hashtable[index] = cur.next
            self.size -= 1
            return return_val
        else:
            cur = cur.next
            while cur:
                if cur.key == key:
                    return_val = cur.value
                    prev.next = cur.next
                    self.size -= 1
                    return return_val
                else:
                    cur, prev = cur.next, prev.next


if __name__ == '__main__':
    hash_map = MyHashMap()
    while (command := input()) != 'quit':
        words = command.split()
        if 'put' in command:
            hash_map[words[1]] = words[2]
        elif 'get' in command:
            print(hash_map[words[1]])
        elif 'remove' in command:
            print(hash_map.remove(words[1]))
        elif 'containsKey' in command:
            print('true' if hash_map[words[1]] != 'null' else 'false')
        elif 'display' in command:
            print('Display Begins')
            for idx, element in enumerate(hash_map.hashtable):
                curr = element
                print(f'Bucket{idx}', end=' ')
                while curr:
                    print(f'{curr.key}@{curr.value}', end=' ')
                    curr = curr.next
                print('.')
