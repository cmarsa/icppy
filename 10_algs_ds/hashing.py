# hashing.py
'''
A hash function maps a large
space of inputs (e.g., all natural numbers) to a smaller space of outputs (e.g., the
natural numbers between 0 and 5000 ). Hash functions can be used to convert a
large space of keys to a smaller space of integer indices.
Since the space of possible outputs is smaller than the space of possible in-
puts, a hash function is a many-to-one mapping, i.e., multiple different inputs
may be mapped to the same output. When two inputs are mapped to the same
output, it is called a collision—a topic we will return to shortly. A good hash
function produces a uniform distribution; i.e., every output in the range is equal-
ly probable, which minimizes the probability of collisions.
'''

class intDict:
    '''A dictionary with integer keys'''
    def __init__(self, num_buckets):
        '''Create an empty dictionary'''
        self.buckets = []
        self.num_buckets = num_buckets
        for i in range(0, num_buckets):
            self.buckets.append([])
    
    def add_entry(self, key, dict_val):
        '''Assumes key an int. Adds an entry'''
        hash_bucket = self.buckets[key % self.num_buckets]
        # iterate over the hash_bucket to see the key-value pairs
        for i in range(0, len(hash_bucket)):
            # if the key coincides with a value replace and return
            if hash_bucket[i][0] == key:
                hash_bucket[i] = (key, dict_val)
                return
        # no value coincidence, so append
        hash_bucket.append((key, dict_val))
    
    def get_value(self, key):
        '''
        Assumes key an int.
        Returns value associated with key.
        '''
        # get the corresponding bucket for the key
        hash_bucket = self.buckets[key % self.num_buckets]
        # iterate over the bucket and ckeck if the key is present
        for e in hash_bucket:
            if e[0] == key:
                # key is present
                return e[1]
        # no key present in the bucket
        return None
    
    def __str__(self):
        result = '{'
        for b in self.buckets:
            for e in b:
                result = result + str(e[0]) + ':' + str(e[1]) + ','
        return result[:-1] + '}'


if __name__ == '__main__':
    import random
    d = intDict(20)
    for i in range(50):
        # choose a random int in the range
        key = random.choice(range(100))
        d.add_entry(key, i)
    print('d: ', d)
    print('\n', 'The buckets are: ')
    for hash_bucket in d.buckets:
        print('  ', hash_bucket)

'''
When we violate the abstraction barrier and peek at the representation of the
intDict , we see that some of the hash buckets are empty. Others contain one, two,
or three entries—depending upon the number of collisions that occurred.
What is the complexity of getValue ? If there were no collisions it would be
O(1), b ecause each hash bucket would be of length 0 or 1. But, of course, there
might be collisions. If everything hashed to the same bucket, it would be O(n)
where n is the number of entries in the dictionary, because the code would per-
form a linear search on that hash bucket. By making the hash table large enough,
we can reduce the number of collisions sufficiently to allow us to treat the com-
plexity as O(1) . That is, we can trade space for time.
'''