from datetime import date, datetime, timedelta
from dataclasses import dataclass
import os
import shutil

@dataclass
class Meal:
    """
    Creates a meal with fields, type(string), time(string), location(string)
    """
    type: str
    time: str
    location: str
    food: str

@dataclass
class Request:
    """
    Contains all 3 meals, Breakfast, Lunch, and Dinner
    """
    breakfast: Meal
    lunch: Meal
    dinner: Meal

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
            return "pencader"
            break
        else :
            print("Please enter either A, B, or C")
            whatDiningHall(meal)

def takeOrder(b: bool, l: bool, d: bool) -> Request:
    """
    Takes order and writes into request form
    """
    order = Request(Meal("breakfast", "", "", ""), Meal("lunch", "", "", ""), Meal("dinner", "", "", ""))
    if b :
        order.breakfast.food = input("What would you like to order for breakfast? ")
        order.breakfast.time = input("What time would you like your breakfast ready? ")
        order.breakfast.location = whatDiningHall("breakfast")

    if l :
        order.lunch.food = input("What would you like to order for lunch? ")
        order.lunch.time = input("What time would you like your dinner ready? ")
        order.lunch.location = whatDiningHall("lunch")

    if d :
        order.dinner.food = input("What would you like to order for dinner? ")
        order.dinner.time = input("What time would you like your dinner ready? ")
        order.dinner.location = whatDiningHall("dinner")

    return order
    
#Emails
rodneyEmail = "rodneydiningffco@udel.edu"
pencaderEmail = "pencaderdininghall@udel.edu"
russellEmail = "russelldininghall@udel.edu"

#Dates
theDate = datetime.today() + timedelta(1) #tomorrows date variable
mdy = theDate.strftime("%m/%d/%Y") #prints theDate in m/d/y
m_d_y = theDate.strftime("%m_%d_%Y") #prints theDate in m/d/y
d = theDate.strftime("%A") #prints theDate in word form

#File Locations
src = r"/Users/johnfulkerson/src/CustomMealRequest/Custom Meal Request Form.docx"
dest = r"/Users/johnfulkerson/src/CustomMealRequest/Previous Meal Requests/" + m_d_y + ".docx"

#Main
order = takeOrder(wantBreakfast(), wantLunch(), wantDinner())
path = shutil.copyfile(src,dest)

