# Starting Point
import time


print("My name?")
MyName = input()
print("hello world. I'm ", MyName)
print("What'syr name?")
UserName = input()
print("Yr name is ", UserName, "? Niceta meet u. ")

print("Yr name is ", len(UserName), " letters long.   Weird.")

print("Yr name plus mine is ", len(UserName) + len(MyName)," letters long.")

print("How oldr u?")
UserAge = input()
print("Yr age is ", UserAge, " years old.   Interesting.")
if int(UserAge) >= 18:
    print("U turned 18 ", int(UserAge) - 18, " years ago.   Wow.")
else: print("U will turn 18 in ", 18 - int(UserAge), " years.   Cool.")
