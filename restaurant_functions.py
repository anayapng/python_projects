def print_restaurant_details(cust_pref, cuisine_type):
    """Print out the key value pairs in a dictionary"""
    print(f"\nThe halal-certified restaurants that serve {cust_pref.title()} food are:\n ") 
    for restaurant_name, information in cuisine_type.items():
        print(restaurant_name.title() + ":")
        print("Their signature dish and current Google rating are as follows:")
        for detail in information:
            print("\t- " + str(detail))
        print()

def merge_dictionaries(x, y, z, a):
	mergedDict = {**x, **y, **z, **a}
	return mergedDict

def add_restaurant(cuisine_type, restaurant_name, signature_dish, rating):
    """Allows users to input new restaurant details"""
    # cuisine_type = input("Which cuisine type would you like to contribute to?")
    cuisine_type[restaurant_name] = [signature_dish, rating]
    print(cuisine_type)
    print("\nIt has successfully been added! Thank you for your contribution!")

# COME BACK TO THIS ONE DAY!
# def restaurant_details():
#     """Prompts user to enter details of the restaurant they want to add."""
#     restaurant_name = input ("Name of halal restaurant: ")
#     signature_dish = input("Signature Dish: ")
#     rating = input("Rating: ")
#     return restaurant_name, signature_dish, rating