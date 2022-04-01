import math
import mmh3
from bitarray import bitarray

class BloomFilter:
    """
    Class for Bloom filter, using murmur3 hash function
    Our implementation of a Bloom Filter can be initialised by providing num_items (n) and p or bitarray_size (m) and p
    p is the false probability
    """
    def __init__(self, specify_item_count: bool, param: int, fp_prob: float):
        """
        specify_item_count : bool
            A boolean to denote if the param that we pass in is n or m
            True denotes n
            False denotes m
        param : int
            Either n or m depending on if specify_item_count is True or False respectively
        fp_prob : float
            False Positive probability in decimal
        """
        self.fp_prob = fp_prob

        if specify_item_count:
            self.num_items = param
            self.size = self.get_size(self.num_items, fp_prob)
        else:
            self.size = param
            self.num_items = self.get_item_count(self.size, fp_prob)

        # number of hash functions to use
        self.hash_count = self.get_hash_count(self.size, self.num_items)

        # Bit array of given size
        self.bit_array = bitarray(self.size)

        # initialize all bits as 0
        self.bit_array.setall(0)

    def add(self, item):
        """
        Add an item in the filter
        """
        digests = []
        for i in range(self.hash_count):
            # create digest for given item.
            # i work as seed to mmh3.hash() function
            # With different seed, digest created is different
            digest = mmh3.hash(item, i) % self.size
            digests.append(digest)

            # set the bit True in bit_array
            self.bit_array[digest] = True

    def check(self, item):
        """
        Check for existence of an item in filter
        """
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            if self.bit_array[digest] == False:
                # if any of bit is False, its not present
                # in filter
                # else there is probability that it exist
                return False
        return True

    @classmethod
    def get_size(self, n, p):
        """
        Return the size of bit array(m) to used using
        following formula
        m = -(n * lg(p)) / (lg(2)^2)
        n : int
            number of items expected to be stored in filter
        p : float
            False Positive probability in decimal
        """
        m = -(n * math.log(p)) / (math.log(2) ** 2)
        return int(m)

    @classmethod
    def get_item_count(self, m, p):
        """
        Return the suggested item count using
        following formula
        n = -(m * lg(2)^2) / lg(p)
        n : int
            number of items expected to be stored in filter
        p : float
            False Positive probability in decimal
        """
        n = -(m * math.log(2) ** 2) / (math.log(p))
        return int(n)

    @classmethod
    def get_hash_count(self, m, n):
        """
        Return the hash function(k) to be used using
        following formula
        k = (m/n) * lg(2)
        m : int
            size of bit array
        n : int
            number of items expected to be stored in filter
        """
        k = (m / n) * math.log(2)
        return int(k)
