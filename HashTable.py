class HashTable:
    def __init__(self):
        self.capacity = 10
        self.size = 0
        self.table = [None] * self.capacity

    def __len__(self):
        return self.size

    def __contains__(self, key):
        index = self._hash(key)
        return self.table[index] is not None

    def _hash(self, key):
        hash_value = hash(key) % self.capacity
        return hash_value

    def add(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for pair in self.table[index]:
                if pair[0] == key:
                    pair[1] = value
                    break
            else:
                self.table[index].append((key, value))
        self.size += 1


hash_table = HashTable()
hash_table.add("key1", "value1")
hash_table.add("key2", "value2")

print("Довжина таблиці:", len(hash_table))
print("Чи містить 'key1'?", "Так" if "key1" in hash_table else "Ні")
print("Чи містить 'key3'?", "Так" if "key3" in hash_table else "Ні")

