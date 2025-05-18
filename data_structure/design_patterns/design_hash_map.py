class HashMap:

    def __init__(self):
        self.size = 1000
        self.bucket = [[] for _ in range(self.size)]

    def hash(self, key):
        return key % self.size

    def put(self, key, value):
        index = hash(key)
        for pair in self.bucket[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.bucket[index].append([key, value])
    
    def get(self, key):
        index = hash(key)
        for pair in self.bucket[index]:
            if pair[0] == key:
                return pair[1]
        return -1
    
    def remove(self, key):
        index = hash(key)
        for i , pair in enumerate(self.bucket[index]):
            if pair == key:
                del self.bucket[index][i]
                return 
