# Starting Point
import time

def AskNames():
    print("My name?")
    MyName = input()
    print("hello world. I'm ", MyName)
    print("What'syr name?")
    UserName = input()
    print("Yr name is ", UserName, "? Niceta meet u. ")
    return MyName, UserName

def AskAge():
    print("How oldr u?")
    UserAge = input()
    try: 
        print("Yr age is ", UserAge, " years old.   Interesting.")
        if int(UserAge) >= 18:
            print("U turned 18 ", int(UserAge) - 18, " years ago.   Wow.")

        elif int(UserAge) == 18: print("U turned 18 this year.   Cool.")

        elif int(UserAge) < 18: print("U will turn 18 in ", 18 - int(UserAge), " years.   Awesome.")

        elif int(UserAge) <= 0: print("U haven't been born yet.   Amazing.")
    except ValueError: print("That wasn'ta real number.  -_-")
    return UserAge

def AskSiblings(): 
    while True:
        print("How many siblings do u have?")
        UserSiblings = input()
        
        try: 
            UserSiblings = int(UserSiblings)
            print("U have ", UserSiblings, " siblings.   Interesting.") 
            break  # Exit the loop if a valid number is entered
        except ValueError: 
            print("That wasn't a real number. Please enter a valid number.  -_-")

    UserSiblingDetails = []
    for _ in range(UserSiblings):
        print("What's One?")#add sequential order   "name?")
        UserSiblingDetails.append(input())
    return UserSiblingDetails


MyName, UserName = AskNames()
print("Yr name is ", len(UserName), " letters long.   Weird.")
print("Yr name plus mine is ", len(UserName) + len(MyName)," letters long.")


UserAge = AskAge()

UserSiblingDetails = AskSiblings()