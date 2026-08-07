# ==========================================
# تمرین 1
# ==========================================
print("=== 1 ===\n")

# دریافت اطلاعات دانش‌آموز اول
first_student_name = input("First student name: ")
first_student_age = int(input("First student age: "))

# دریافت اطلاعات دانش‌آموز دوم
second_student_name = input("Second student name: ")
second_student_age = int(input("Second student age: "))

# مقایسه سن‌ها
age_comparison = first_student_age > second_student_age

# نمایش نتایج
print(first_student_name)
print(second_student_name)
print(age_comparison)


# ==========================================
# تمرین 2 (چالشی)
# ==========================================

print("=== 2 ===\n")

# دریافت اطلاعات محصول اول
first_product = input("First product: ")
first_price = int(input("First price: "))

# دریافت اطلاعات محصول دوم
second_product = input("Second product: ")
second_price = int(input("Second price: "))

# مقایسه‌های مختلف
equal_prices = first_price == second_price
first_more_expensive = first_price > second_price
second_cheaper_or_equal = second_price <= first_price
same_name = first_product == second_product

# محاسبه قیمت کل
total_price = first_price + second_price

# نمایش نتایج
print(f"\nEqual prices: {equal_prices}")
print(f"First product is more expensive: {first_more_expensive}")
print(f"Second product is cheaper or equal: {second_cheaper_or_equal}")
print(f"Same name: {same_name}")
print(f"{first_product} costs more than {second_product}: {first_more_expensive}")

# نمایش فاکتور
print(f"\n{first_product} : {first_price}")
print(f"{second_product} : {second_price}")
print("-" * 20)
print(f"full price : {total_price}")
