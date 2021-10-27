import sys

# Eventually, the function will cause the final answer to return to 1. 

def collatz(number):
    """
    Returns values based on whether number is odd or even
    """
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

print("Please input an integer: ")
while True:
    try:
        number = input()
        number = int(number)
    except ValueError:
        print("You need to enter an integer!!")
    else:
        answer = collatz(number)
        print(answer)
        if answer == 1:
            sys.exit()
  
