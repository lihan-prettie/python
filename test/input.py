# name = input("please enter ur name:")
# height = int(input("please enter ur height(cm):"))
# weight = int(input("please enter ur weight(kg):"))
# bmi = weight/(height/100)**2
# print(f"dear {name}, ur bmi is {bmi:.2f}")

age = int(input("please enter ur age:"))
if age > 150 or age < 0:
    print("please enter a correct age")
elif age > 17:
    print("adult")
elif age < 15:
    print("kid")
else:
    print("teen")
