"""
آموزش پایتون - رشته‌ها (Strings)

رشته (String) یعنی مجموعه‌ای از حروف، اعداد یا نمادها
که همیشه داخل "" یا '' نوشته می‌شود.
"""

# ==========================================
# ساخت رشته
# ==========================================

course_name = "Python Programming"
favorite_food = "Pizza 🍕"
student_name = "Sara"

print(course_name)
print(favorite_food)
print(student_name)


# ==========================================
# رشته چندخطی
# ==========================================

story = """
It's not about winning; it's about fun!
SpongeBob
"""

print(story)


# ==========================================
# تابع len()
# ==========================================
# تعداد کاراکترهای یک رشته را برمی‌گرداند.

print(len(course_name))
print(len(student_name))
print(len("🐍 Python"))


# ==========================================
# Indexing (دسترسی به یک کاراکتر)
# ==========================================
# شماره‌گذاری از صفر شروع می‌شود.

game = "Minecraft"

print(game[0])      # M
print(game[1])      # i
print(game[-1])     # t (آخرین حرف)
print(game[-2])     # f


# ==========================================
# Slicing (بریدن رشته)
# ==========================================

print(game[0:5])    # Minec
print(game[5:])     # raft
print(game[:5])     # Minec
print(game[:])      # کل رشته


# ==========================================
# Escape Sequences
# ==========================================

print("Python \"Programming\"")
print('It\'s my favorite language.')
print("C:\\Users\\Mostafa")
print("Hello\nWorld")


# ==========================================
# اتصال رشته‌ها
# ==========================================

first_name = "SpongeBob"
last_name = "SquarePants"

full_name = first_name + " " + last_name
print(full_name)


# ==========================================
# f-Strings
# ==========================================
# بهترین روش برای ساخت متن

age = 15
score = 98

print(f"My name is {first_name}.")
print(f"I am {age} years old.")
print(f"My score is {score}.")
print(f"{first_name} has {len(first_name)} letters.")
print(f"5 × 4 = {5 * 4}")


# ==========================================
# متدهای رشته
# ==========================================

movie = "spider man"

print(movie.upper())      # SPIDER MAN
print(movie.lower())      # spider man
print(movie.title())      # Spider Man


# ==========================================
# حذف فاصله‌های اضافی
# ==========================================

name = "   Mostafa   "

print(name.strip())
print(name.lstrip())
print(name.rstrip())


# ==========================================
# پیدا کردن متن
# ==========================================

text = "Python Programming"

print(text.find("Program"))
print(text.find("Java"))      # پیدا نشد → -1


# ==========================================
# جایگزینی متن
# ==========================================

print(text.replace("Python", "Java"))
print(text.replace("Programming", "Course"))


# ==========================================
# بررسی وجود یک متن
# ==========================================

print("Python" in text)
print("Java" in text)

print("Java" not in text)
print("Python" not in text)


# ==========================================
# تمرین 2
# ==========================================
#
# سه متغیر زیر را بساز:
#
# favorite_game
# favorite_movie
# favorite_animal
#
# سپس:
# 1- هر سه را چاپ کن.
# 2- طول favorite_game را با len() چاپ کن.
# 3- اولین حرف favorite_movie را چاپ کن.
# 4- بررسی کن آیا "Cat" داخل favorite_animal وجود دارد یا نه.
#
#
# پاسخ نمونه
#
# favorite_game = "Minecraft"
# favorite_movie = "Frozen"
# favorite_animal = "Cat"
#
# print(favorite_game)
# print(favorite_movie)
# print(favorite_animal)
#
# print(len(favorite_game))
# print(favorite_movie[0])
# print("Cat" in favorite_animal)
