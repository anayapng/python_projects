# Calculating the percentage of having a streak of 6 Heads or 6 Tails in a row, in a 100 times flip.
# Experiment is done 10,000 times. 

import random

number_of_streaks = 0 # records the number of times 'H' or 'T' appears 6 times in a row
streak_value = 0 # records the number of times the letter behind is the same as the next one

for experiment_number in range(10000):
    # Creates a list of 100 'heads' or 'tails' value
    coin_list = []
    for flips in range(100):
        if random.randint(0, 1) == 0:
            coin_list.append('H')
        elif random.randint(0,1) == 1:
            coin_list.append('T')

    # Checks if there is a streak of 6 heads or tails in a row.
    for i in range(len(coin_list)):
        if coin_list[i] == coin_list[i-1]: 
            streak_value += 1
        else:
            streak_value = 0 # resets the streak value
    
    if streak_value == 6:
        number_of_streaks += 1 # only increases when we have 6 Hs or 6 Ts in a row.
        
print("Chance of streak: %s%%" % (number_of_streaks/100))