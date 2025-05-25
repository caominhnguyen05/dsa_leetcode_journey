# Hashsets

s = set()
print(s)

# Add item into Set - O(1)
s.add(1)
s.add(2)
s.add(3)

print(s)

# Lookup if item in set - O(1)
if 1 in s:
    print(True)

# Remove item from set - O(1)
s.remove(3)

print(s)

string = 'aaaaaaaaaaaabbbbbbbbbbbccccccceeeeeeee'
sett = set(string) # Set construction - O(S) - S is the length of the string

print(sett)

# Loop over items in set - O(n)
for x in s:
    print(x)