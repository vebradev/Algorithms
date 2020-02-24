#!/usr/bin/python

def recipe_batches(recipe, ingredients):
    # set empty list to hold batches
    batches = []
    for ingredient in recipe:
        # set key variables for the calculation: required & available
        # grab the required amount from the recipe
        required_amount = recipe[ingredient]
        # and available amount from ingredients dict using the get method
        # which allows to insert default value if suck key is not found
        available_amount = ingredients.get(ingredient, 0)
        # divide available by required and cast value to int in order to find
        # the rounded number of batches
        batches.append(int(available_amount/required_amount))
        # print(f"Required: {required_amount} of {ingredient}, available: {available_amount}")
    return min(batches)

# print(recipe_batches(
#     {'milk': 100, 'butter': 50, 'flour': 5},
#     {'milk': 138, 'butter': 48, 'flour': 51}
# ))

# print(recipe_batches(
#     { 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, 
#     { 'milk': 1288, 'flour': 9, 'sugar': 95 }
# ))

# recipe_batches({ 'milk': 2 }, { 'milk': 200})

if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
