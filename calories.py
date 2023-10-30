CALORIES_TABLE = {
    "Apple": 130,
    "Avocado": 50,
    "Lime": 20,
    "Orange": 80,
    "Kiwifruit": 90,
    "Pear": 100,
    "Lemon": 15,
    "Plums": 70,
    "Watermelon": 80,
    "Tangerine": 50,
}


user_input = input("Фрукт: ")
calories = CALORIES_TABLE.get(user_input, -1)
print(f"Калории: {calories}")