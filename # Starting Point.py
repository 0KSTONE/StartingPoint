# Starting Point
import time

def Menu():
    while True:
        print("What're u here for?")
        print("1. Age")
        print("2. Siblings")
        print("3. Favourites")
        print("4. Quit")
        MenuSelection = input()
        
        if MenuSelection == "1":
                UserAge = AskAge()
        elif MenuSelection == "2":
            while True: 
                print(" 1. Sibling Entry")
                print(" 2. Sibling List")
                SibMenuSelection = input()
                
                if SibMenuSelection == "1":
                        UserSiblings, UserSiblingDetails = AskSiblings()
                elif SibMenuSelection == "2":
                    print("U have ", UserSiblings, " siblings.")
                    print("Their names are:")
                    for SibName in UserSiblingDetails:
                                print(SibName)

                else: print("Invalid Selection. Please try again.")

        elif MenuSelection == "3": 
                print("Favourites Not Implemented Yet")
        elif MenuSelection == "4":
                print("Goodbye.")
                break

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
        Counter = _ + 1
        print("Name ", str(Counter), "?")
        UserSiblingDetails.append(input())
    return UserSiblings, UserSiblingDetails, Counter

MyName, UserName = AskNames()
print("Yr name is ", len(UserName), " letters long.   Weird.")
print("Yr name plus mine is ", len(UserName) + len(MyName)," letters long.")

Menu()