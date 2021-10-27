# The goal here is to create a function that accepts a list as a parameter
# and return the items as a string sentence. 
# e.g. random_things = ['apples', 'tofu', 'bananas', 'cats']
# the function should return "apples, tofu, bananas, and cats"


# This works but permanently removes an item off the end of the list...
def make_string(list):
    last_item = list.pop()
    for item in list:
        print(item, end=", ")
    print("and " + last_item, end=" ")

# This works according to what has been taught under Chapter 4 of Automate Boring Stuff with Python
def return_string(list):
    for index, item in enumerate(list):
        if index == 0:
            my_string = str(item) + ", " 
        elif index < len(list) - 1:
            my_string += str(item) + ", "
        else:
            my_string += "and " + str(item)
    return my_string
    
random_things = ['apples', 'tofu', 'bananas', 'cats']
print(return_string(random_things))


