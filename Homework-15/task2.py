foods = ("Apple", "Banana", "Orange", "Mango", "Strawberry", "Grape", "Mandarin", "Strawberry")
calories=(52, 96, 62, 605, 33, 68, 50, 33)

print(f"5th food: {foods[4]} - {calories[4]} kcal")
print(F"last food: {foods[-2]} - {calories[-2]} kcal")

unique_foods = list(set(foods))
print("Unique foods:", unique_foods)


food_dict = {}

for food, cal in zip(foods, calories):
    food_dict[food] = cal

print("Unique Food-Calorie Dictionary:")
for food, cal in food_dict.items():
    print(f"{food}: {cal} kcal")
    
