from impl import BloomFilter
import sys
import time

def load_usernames(filename, holder):
    f = open(filename, 'r')
    username = f.readline()
    while username:
        username = username.strip()
        holder.add(username)
        username = f.readline()
    return holder

def membership_test(holder):
    f = open(filename, 'r')
    list_ = [None for _ in range(160000)]
    i = 0
    username = f.readline()
    while username:
        username = username.strip()
        list_[i] = username
        username = f.readline()
        i+=1

    start = time.time()
    for username in list_:
        if isinstance(holder, BloomFilter): 
            if holder.check(username): pass
        if isinstance(holder, set): 
            if username in holder: pass
    end = time.time()
    avg_time_taken = 1000000000 * (end - start) / 160000
    return avg_time_taken 







if __name__ == '__main__':
    p = 1/1000
    bloomfilter = BloomFilter(specify_item_count = True, param = 160000, fp_prob = p)

    print(bloomfilter.hash_count)

    # A dataset of 160,000 Twitter usernames
    filename = 'input.txt'

    bloomfilter = load_usernames(filename, bloomfilter)
    set_ = load_usernames(filename, set())

    # Compare the sizes
    print(f'Size of Set: {sys.getsizeof(set_) / 1000000} bytes') # sys get size returns the number of bytes an object takes up, so we divide by 8
    print(f'Size of BloomFilter {bloomfilter.size / (8 * 1000000)} bytes') 
    print(f'The Set takes up {(sys.getsizeof(set_) * 8 / bloomfilter.size):.3f} times more space than the BloomFilter')

    time_bloom = membership_test(bloomfilter)
    time_set = membership_test(set_)
    print(f'Average time taken to test membership for BloomFilter: {time_bloom:.2f}ns')
    print(f'Average time taken to test membership for set: {time_set:.2f}ns')
    print(f'Testing membership in set is {(time_bloom / time_set):.3f} times faster than bloomfilter')

    