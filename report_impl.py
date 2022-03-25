import math
import mmh3
from bitarray import bitarray

class BloomFilter:
   def __init__(self, specify_item_count, param, fp_prob):
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
       # initialise all bits as 0
       self.bit_array.setall(0)

   def add(self, item):
       digests = []
       for i in range(self.hash_count):
           # Pass in a seed, i, to obtain a different digest with the mmh3
           # algorithm
           digest = mmh3.hash(item, i) % self.size
           digests.append(digest)

           # set the bit True in bit_array
           self.bit_array[digest] = True

   def check(self, item):
       for i in range(self.hash_count):
           digest = mmh3.hash(item, i) % self.size
           if self.bit_array[digest] == False:
               # if any of bit is False, its not present in filter
               # else there is a probability that it exists
               return False
       return True

   @classmethod
   def get_size(self, n, p):
       m = -(n * math.log(p)) / (math.log(2) ** 2)
       return int(m)
   @classmethod
   def get_item_count(self, m, p):
       n = -(m * math.log(2) ** 2) / (math.log(p))
       return int(n)
   @classmethod
   def get_hash_count(self, m, n):
       k = (m / n) * math.log(2)
       return int(k)