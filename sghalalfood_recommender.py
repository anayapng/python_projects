"""
For self practice on loops, lists, dictionaries and functions. 
This is a simple recommendation system for halal food in Singapore.
Based on user's preference for cuisine type, or users can opt for random recommendation.
Users may also contribute to the restaurant list if they wish to.
I intend to slowly grow this recommender into one that can scrape information online, once I gain more knowledge on Python.
"""

from restaurant_functions import print_restaurant_details, add_restaurant, merge_dictionaries
import random

chinese = {
	'nuodle': ['beef noodles', 4.1],
	'tang tea house': ['dim sum', 4.2],
	'home of seafood': ['seafood in a bag', 3.4],
	'maks place': ['butter sotong', 4.2],
	'le fuse': ['mala xiang guo', 4.6],
	'the dim sum place': ['classic dim sum', 4.4],
	'buey tahan see-food': ['chilli crab', 4.0],
	'wok hey': ['egg fried rice', 3.1],
	}

japanese = {
	'daya izakaya': ['izakaya', 4.2],
	'hei sushi': ['spicy salmon sushi', 3.8],
	'gyunion': ['beef bowl', 4.5],
	'tokyo shokudo': ['signature tendon', 3.7],
	'monster planet': ['chicken katsu curry', 4.4],
	'sora boru': ['curry boru', 3.7],
	'ichikokudo hokkaido ramen': ['gifts from the sea bowl', 4],
	'wakuwaku yakiniku': ['jo-karubi (boneless short rib)', 4.7],
	}

korean = {
	'omoomo': ['spicy chicken don', 3.7 ],
	'jw korean food story': ['army stew', 4.6],
	'hanok by massizim': ['beef rib stew', 3.5],
	'captain kim korean bbw and hotpot': ['bbq!', 4.1],
	'jinjja chicken': ['korean friend chicken', 4.5],
	'egg stop': ['beef teriyaki toast', 3.4],
	'dosirak': ['beef bulgogi bowl', 4.0],
	'4fingers crispy chicken': ['signature mix', 4.4],
	}

asian_fusion = {
	'qiji': ['nasi lemak', 4.7],
	'puncak beset noodles': ['sambal fish', 4.4],
	'straits kitchen': ['buffet', 4.3],
	'kedai kopi': ['local favourites', 4.3],
	'the halia': ['slow cooked white phyrenees lamb shank', 4.2],
	'21 on rajah': ['nasi goreng istimewa', 4.2],
	'spize': ['satay gado gado', 4],
	}


while True: 
	prompt = "What type of cuisine would you like to eat? "
	prompt += "(Chinese, Japanese, Korean, Asian Fusion)\n"
	prompt += "You may indicate 'random' if you would like a random recommendation.\n"
	prompt += "(Enter 'q' if you would like to exit) "
	cuisine_preference = input(prompt)
	if cuisine_preference.lower() == 'chinese':
		print_restaurant_details(cuisine_preference, chinese)
	elif cuisine_preference.lower() == 'japanese':
		print_restaurant_details(cuisine_preference, japanese)
	elif cuisine_preference.lower() == 'korean':
		print_restaurant_details(cuisine_preference, korean)
	elif cuisine_preference.lower() == 'asian fusion':
		print_restaurant_details(cuisine_preference, asian_fusion)
	elif cuisine_preference.lower() == 'random':
		combined = merge_dictionaries(chinese, japanese, korean, asian_fusion)
		print("\nHere is a random recommendation for you to try out!\n\t")
		full_list = list(combined.items())
		random_reco = random.choice(full_list)
		print(str(random_reco) + "\n")
	elif cuisine_preference == 'q':
		break

# Provide users with opportunity to add new restaurants that are not on the list.

prompt = "\nBefore you go, would you like to add on a new halal restaurant into the list? (y/n) "
prompt += "\n(Indicating 'n' will allow you to exit the program) "

while True:
	answer = input(prompt)
	if answer.lower() == 'y':
		second_prompt = "Which cuisine type would you like to contribute to? "
		second_prompt += "(Chinese / Japanese / Korean / Asian Fusion) "
		user_choice = input(second_prompt)
		"""
		I should be able to use a function to replace this.
		I will come back to it once I learn how to use a function's output
		as an input for another function.
		"""
		if user_choice.lower() == 'chinese':
			restaurant_name = input ("Name of Halal restaurant: ")
			signature_dish = input("Signature Dish: ")
			rating = input("Rating: ")
			add_restaurant(chinese, restaurant_name, signature_dish, rating)
		elif user_choice.lower() == 'japanese':
			restaurant_name = input ("Name of Halal restaurant: ")
			signature_dish = input("Signature Dish: ")
			rating = input("Rating: ")
			add_restaurant(japanese, restaurant_name, signature_dish, rating)
		elif user_choice.lower() == 'korean':
			irestaurant_name = input ("Name of Halal restaurant: ")
			signature_dish = input("Signature Dish: ")
			rating = input("Rating: ")
			add_restaurant(korean, restaurant_name, signature_dish, rating)
		elif user_choice.lower() == 'asian fusion':
			restaurant_name = input ("Name of Halal restaurant: ")
			signature_dish = input("Signature Dish: ")
			rating = input("Rating: ")
			add_restaurant(asian_fusion, restaurant_name, signature_dish, rating)
	elif answer.lower() == 'n':
		break
