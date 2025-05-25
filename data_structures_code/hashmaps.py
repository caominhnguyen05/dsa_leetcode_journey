# Hashmap - Dictionaries
d = {'greg': 1, 'steve': 2, 'rob': 3}

print(d)

# Add key:val in dictionary: O(1)
d['arsh'] = 4

print(d)

# Check for presence of key in dictionary: O(1)
if 'greg' in d:
  print(True)

# Check the value corresponding to a key in the dictionary: O(1)
print(d['greg'])

# Loop over the key:val pairs of the dictionary: O(n)
for key, val in d.items():
  print(f'key {key}: val {val}')

# Defaultdict
from collections import defaultdict
default = defaultdict(list)

print(default[2])
print(default)

# Counter
from collections import Counter
string = 'aaaaaaaaaaaabbbbbbbbbbbccccccceeeeeeee'

counter = Counter(string)
print(counter)