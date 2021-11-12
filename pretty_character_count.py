# setdefault() method is a shortcut to ensure a key exists
# two arguments - first the key to check for, and second is the value to set at that key if key does not exist
# here we are counting how many times a character appears in the message

import pprint

# using pprint() to have a cleaner display of the dict's values.

message = 'It was a bright cold day in April, and the clocks were striking thirteen'

count = {}

for character in message:
    count.setdefault(character, 0) # set to zero so there is no error
    count[character] += 1

pprint.pprint(count)