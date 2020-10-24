#-*- coding:utf-8 -*-

import pprint


MESSAGE = "It was a bright cold day in April, and the clocks were striking thirteen"

count = {}

for character in MESSAGE:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
    print(character)

pprint.pprint(count)
pprint.pprint(count)
print(pprint.pformat(count))

