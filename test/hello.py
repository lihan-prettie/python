def say_hello():
    return "Hello World!"


name = "peter"
age = 25
is_student = True
print("ur name is: ", name, ",and ur age is :", age)

speak = say_hello()
print(speak)

score = 80
print(f"你的成績是:{score}")
score += 5
print(f"調整後的成績:{score}")
