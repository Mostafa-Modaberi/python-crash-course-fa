# ==========================================
# پاسخ تمرین 1
# ==========================================
print("\n=== 1 ===\n")
while True:
    number = int(input("Enter a number: "))

    if number <= 100:
        print(f"Accepted: {number}")
        break


# ==========================================
# پاسخ تمرین چالشی 1
# ==========================================
print("\n=== 2 ===\n")
total_score = 0
score_count = 0

while True:
    score = int(input("Enter score: "))

    if score == -1:
        break

    total_score += score
    score_count += 1

print(f"Total score: {total_score}")
print(f"Number of scores: {score_count}")


# ==========================================
# پاسخ تمرین چالشی 2
# ==========================================
print("\n=== 3 ===\n")
balance = 1000

while True:
    print()
    print("1. Show balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print(f"Balance: {balance}")

    elif choice == "2":
        amount = int(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Deposit successful")
        else:
            print("Invalid amount")

    elif choice == "3":
        amount = int(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount")

        elif amount > balance:
            print("Insufficient balance")

        else:
            balance -= amount
            print("Withdrawal successful")

    elif choice == "4":
        print("Goodbye")
        break

    else:
        print("Invalid option")
