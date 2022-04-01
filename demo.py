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
    bloomfilter = BloomFilter(specify_item_count=True, param=160000, fp_prob=1/100000)

    # A dataset of 160,000 Twitter usernames
    filename = 'input.txt'

    bloomfilter = load_usernames(filename, bloomfilter)
    holder = load_usernames(filename, set())

    print(f'Size of Set: {sys.getsizeof(holder) * 8} bits') # sys get size returns the number of bytes an object takes up, so we divide by 8
    print(f'Size of BloomFilter {bloomfilter.size} bits') 
    print(f'The Set takes up {(sys.getsizeof(holder) * 8 / bloomfilter.size):.3f} times more space than the BloomFilter')

    