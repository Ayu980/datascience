indian_food = ["Samosa", "daal", "naan"]
chinese_food = ["Egg role", "pot sticker", "fried rice"]
italian_food = ["Pizza", "Pasta", "Risotto"]
dish = input("Enter a dish name: ")



if dish in indian_food:
    print("Indian_food")
elif dish in chinese_food:
    print("Chinese_food")
elif dish in italian_food:
    print("Italian_food")
else:
    print("Dish is not in the menue")


