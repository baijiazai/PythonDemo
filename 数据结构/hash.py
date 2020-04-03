class IntDict:
    def __init__(self, num_buckets):
        """ num_buckets 为需要创建的空间数 """
        self.buckets = []
        self.num_buckets = num_buckets
        for _ in range(num_buckets):
            self.buckets.append([])
    
    def add_entry(self, key, dict_val):
        """ key 为散列表的键，dict_val 为需要插进散列表的值 """
        hash_bucket = self.buckets[key % self.num_buckets]
        for i in range(len(hash_bucket)):
            if hash_bucket[i][0] == key:
                hash_bucket[i] = (key, dict_val)
                return
        hash_bucket.append((key, dict_val))

    def get_value(self, key):
        """ key 为散列表的键 """
        hash_bucket = self.buckets[key % self.num_buckets]
        for e in hash_bucket:
            if e[0] == key:
                return e[1]
        return None
    
    def __str__(self):
        res = '{'
        for b in self.buckets:
            for e in b:
                res += str(e[0]) + ':' + str(e[1]) + ','
        return res[:-1] + '}'


if __name__ == "__main__":
    import random
    D = IntDict(17)
    for i in range(20):
        key = random.choice(range(10 ** 5))
        D.add_entry(key, i)
    print('The value of the IntDict is:')
    print(D)
    print('\n', 'The buckets are:')
    for hash_bucket in D.buckets:
        print('', hash_bucket)
    
