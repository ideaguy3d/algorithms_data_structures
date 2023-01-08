import re

s1 = 'this is a simple sentance'
s2 = 'This, is a simple Sentance.'

a1 = [1, 2, 3, 4]
a2 = (3, 4, 5, 6)
a1, a2 = set(a1), set(a2)

print(re.findall('im', s1))

print(re.sub(r'[,.?]', '', s2))

b7 = 1

# end of file
