# ==========================================
# پاسخ تمرین 1
# ==========================================
print("\n=== 1 ===\n")

age = int(input("Age: "))

if age >= 18:
    print("Adult")
else:
    print("Child")


# ==========================================
# پاسخ تمرین 2
# ==========================================
print("\n=== 2 ===\n")

temperature = int(input("Temperature: "))

if temperature > 30:
    print("Hot")
elif temperature >= 20:
    print("Good")
else:
    print("Cold")


# ==========================================
# پاسخ تمرین 3
# ==========================================
print("\n=== 3 ===\n")

username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("Login successful")
elif username != "admin" and password == "1234":
    print("Wrong username")
elif username == "admin" and password != "1234":
    print("Wrong password")
else:
    print("Wrong username and password")


# ==========================================
# پاسخ تمرین 4
# ==========================================
print("\n=== 4 ===\n")

age = int(input("Age: "))
is_student = input("Student (True/False): ") == "True"

if 18 <= age <= 60 or is_student:
    print("Registration accepted")
else:
    print("Registration rejected")
