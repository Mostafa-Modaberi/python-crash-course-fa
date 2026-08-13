# ==========================================
# پاسخ تمرین 1
# ==========================================
print("\n=== 1 ===\n")


def calculate_area(length, width):
    return length * width


length = int(input("Length: "))
width = int(input("Width: "))

area = calculate_area(length, width)

print(f"Area: {area}")


# ==========================================
# پاسخ تمرین چالشی 1
# ==========================================
print("\n=== 2 ===\n")


def find_maximum(*numbers):
    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    return maximum


result = find_maximum(12, 45, 7, 31, 20)

print(f"Maximum: {result}")


# ==========================================
# پاسخ تمرین چالشی 2
# ==========================================
print("\n=== 3 ===\n")


def calculate_discount(price, discount=0):
    final_price = price - (price * discount / 100)
    return final_price


price = float(input("Price: "))

discount = float(input("Discount: "))

final_price = calculate_discount(price, discount)

print(f"Final price: {final_price}")
