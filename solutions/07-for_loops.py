# ==========================================
# پاسخ تمرین 1
# ==========================================
print("\n=== 1 ===\n")
for number in range(1, 11):
    print(number)


# ==========================================
# پاسخ تمرین چالشی 1
# ==========================================
print("\n=== 2 ===\n")

number = int(input("Number: "))

for multiplier in range(1, 11):
    result = number * multiplier
    print(f"{number} x {multiplier} = {result}")


# ==========================================
# پاسخ تمرین چالشی 2
# ==========================================
print("\n=== 3 ===\n")

password = "1234"

for attempt in range(3):
    user_password = input("Enter password: ")

    if user_password == password:
        print("Successful")
        break

    remaining_attempts = 2 - attempt

    if remaining_attempts > 0:
        print(f"Wrong password. {remaining_attempts} attempts left.")

else:
    print("Account locked")
