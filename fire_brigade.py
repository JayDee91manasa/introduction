smoke = input("Is there smoke? (yes/no): ").lower()
flames = input("Do you see flames? (yes/no): ").lower()

if smoke == "yes" or flames == "yes":
    print("Oh no!! its an emergency!!! Call the fire brigade immediately!")
else:
    print(" Situation seems safe. No need to call the fire brigade.")