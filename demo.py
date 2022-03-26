from impl import BloomFilter
import sys

def load_usernames(filename, holder):
    f = open(filename, 'r')
    line = f.readline()
    while line:
        line = line.strip()
        holder.add(line)
        line = f.readline()
    return holder


if __name__ == '__main__':
    bloomfilter = BloomFilter(specify_item_count=True, param=160000, fp_prob=0.05)

    # A dataset of 160,000 Twitter usernames
    filename = 'input.txt'

    bloomfilter = load_usernames(filename, bloomfilter)
    holder = load_usernames(filename, set())

    print(f'Size of set {sys.getsizeof(holder) * 8}') # sys get size returns the number of bytes an object takes up, so we divide by 8
    print(f'Size of bloomfilter {bloomfilter.size}') 
    print(f'ratio of bloomfilter vs set 1 : {sys.getsizeof(holder) * 8 / bloomfilter.size}')

    