# 1. Create a tuple of your favorite foods and print the second food in the tuple.
food = ("Pizza","Biryani","Chicken Tikka","Pasta","paneer")
print(food[1])

# 2. Try to change the second food in the tuple and see what happens.
# food[1] = "Pulav"
# showing Error

# 3. Create a new tuple that contains only the first and last foods in the original tuple and print it.

newFood = (food[0],food[-1])
print(newFood)
# 4. Use the len() function to find the number of foods in the tuple and print it.

FoodLen = len(newFood)
print("Food Length is ", FoodLen)
# 5. Convert the tuple to a list and print the list.
Food_List = list(food)
print(Food_List)