# ==========================================
# پاسخ تمرین 1
# ==========================================

name = input("Name: ")
age = int(input("Age: "))
height = float(input("Height (cm): "))

print(f"Hello {name}!")
print(age + 1)
print(height / 100)


# ==========================================
# پاسخ تمرین 2
# ==========================================

book1 = float(input("Book 1 price: "))
book2 = float(input("Book 2 price: "))
book3 = float(input("Book 3 price: "))

total = book1 + book2 + book3
average = total / 3

print(round(total, 2))
print(round(average, 2))
print(average > 20)
print(f"Average price: {round(average, 2)}")
