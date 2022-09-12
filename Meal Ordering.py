from datetime import date, datetime, timedelta

def wantBreakfast() -> bool :
    """
    Intended to return True or False wether the user wants breakfast or not. 
    """
    user = input("Do you want to special order breakfast? \n").lower()
    if  user == "yes" :
        return True
    elif user == "no" :
        return False
    else:
        print("Please only type yes or no")
        return wantBreakfast()

def wantLunch() -> bool :
    """
    Intended to return True or False wether the user wants lunch or not. 
    """
    user = input("Do you want to special order lunch? \n").lower()
    if  user == "yes" :
        return True
    elif user == "no" :
        return False
    else:
        print("Please only type yes or no")
        return wantLunch()

def wantDinner() -> bool :
    """
    Intended to return True or False wether the user wants dinner or not. 
    """
    user = input("Do you want to special order dinner? \n").lower()
    if  user == "yes" :
        return True
    elif user == "no" :
        return False
    else:
        print("Please only type yes or no")
        return wantDinner()

def whatDiningHall(meal: str) -> str :
    """
    Intended to enter meal and then user is prompted what dining hall they would like that meal in. The dining hall they choose is then returned. 
    """
    while True:
        d1a = input("Which dining hall would you like " + meal + " in: \n A) Russell B) Cesear Rodney C) Pencader \n").lower()
        if d1a == "a" :
            return "russell"
            break
        elif d1a == "b" :
            return "rodney"
            break
        elif d1a == "c" :
            print("pencader")
            break
        else :
            print("Please enter either A, B, or C")
            whatDiningHall(meal)

def order(b: bool, l: bool, d: bool) :
    """
    Takes order and writes into request form
    """
    if b :
        input("What would you like to order for breakfast? ")
        input("What time would you like your breakfast ready? ")
        whatDiningHall("breakfast")

    if l :
        input("What would you like to order for lunch? ")
        input("What time would you like your dinner ready? ")
        whatDiningHall("lunch")

    if d :
        input("What would you like to order for dinner? ")
        input("What time would you like your dinner ready? ")
        whatDiningHall("dinner")
    
#Emails
rodneyEmail = "rodneydiningffco@udel.edu"
pencaderEmail = "pencaderdininghall@udel.edu"
russellEmail = "russelldininghall@udel.edu"

#Dates
theDate = datetime.today() + timedelta(1) #tomorrows date variable
mdy = theDate.strftime("%m/%d/%Y") #prints theDate in m/d/y
d = theDate.strftime("%A") #prints theDate in word form

#Main
order(wantBreakfast(), wantLunch(), wantDinner())

