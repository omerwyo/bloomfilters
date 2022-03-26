from bloomfilter import BloomFilter
from random import shuffle

# Initialise a Bloom Filter, specifying that we will be passing in 
# the number of items we'd like it to account for (13 words)
# We also pass in a false probability of 0.05
n = 13
p = 0.05

bloomfilter = BloomFilter(specify_item_count = True, param = n, fp_prob = p)

print(f"Size of resultant bit array:{bloomfilter.size}")
print(f"False positive Probability:{bloomfilter.fp_prob}")
print(f"Number of hash functions:{bloomfilter.hash_count}\n")

# 13 words to add into the bloomfilter
words_present = ['bonus', 'bonuses', 'coherent', 'cohesive', 'colorful', 'collaborative',
                 'comely', 'comfort','gems', 'generosity', 'generous', 'genius', 'singapore']

# 7 words to test against
words_absent = ['bluff', 'war', 'humanity',
                'hurt', 'nuke', 'gloomy', 'blooming' ]

shuffle(words_present)
shuffle(words_absent)

for word in words_present:
    bloomfilter.add(word)

test_set = words_present + words_absent

shuffle(test_set)

fp_count, present_count, absent_count = 0, 0, 0

for word in test_set:
    if bloomfilter.check(word):
        if word in words_absent:
            print(f"'{word}' is a false positive", end = '\n\n')
            fp_count+=1
        else:
            print(f"'{word}' is probably present", end = '\n\n')
            present_count+=1
    else:
        print(f"'{word}' is definitely not present", end = '\n\n')
        absent_count+=1
        
print(f'Number of words probably present: {present_count}')
print(f'Number of words definitely absent: {absent_count}')
print(f'Number of false positives: {fp_count}')
