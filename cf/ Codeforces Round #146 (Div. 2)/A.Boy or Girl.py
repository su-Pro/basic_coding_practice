import collections

s = input()

if len(collections.Counter(s)) % 2 != 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")