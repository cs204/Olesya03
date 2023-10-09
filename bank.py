user_input = input("Приветствие: ").split(" ")
money = "$100"
if user_input[0] == "здравствуйте":
    money = "$0"
elif user_input[0].startswith("здрасте"):
    money = "$20"
print(f"{money}")