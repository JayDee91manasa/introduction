def display_birthdays(birthday):
    for name, birthday in birthday.items():
        print(f"{name}'s birthday is on {birthday}")

birthdays = {}
for i in range(5):
    name = input(f"Enter the name of friend {i+1}: ")
    birthday = input(f"Enter {name}'s birthday (dd/mm/yyyy): ")
    birthdays[name] = birthday

print("\nStored Birthdays:")
display_birthdays(birthdays)