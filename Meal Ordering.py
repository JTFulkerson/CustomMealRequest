# ----------------------------------------------------------------------------
# Created By: John Fulkerson
# With help from: Brennan Gallamoza
# Created Date: 9/23/2022
# ----------------------------------------------------------------------------

from datetime import date, datetime, timedelta
from dataclasses import dataclass
#from docx import Document
import os
import shutil
from xml.dom.minidom import Document

@dataclass
class Person:
    """
    Creates a person with name(string), phone(string), restriction(string)
    """
    name: str
    phone: str
    restriction: str

@dataclass
class Meal:
    """
    Creates a meal with fields, type(string), time(string), location(string), food(list)
    """
    type: str
    time: str
    location: str
    food: list

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
            return whatDiningHall(meal)

def takeOrder(b: bool, l: bool, d: bool) -> Request:
    """
    Takes order and writes into a Request type which is returned
    """
    order = Request(Meal("breakfast", "", "", ""), Meal("lunch", "", "", ""), Meal("dinner", "", "", ""))
    if b :
        order.breakfast.food = collectFood("breakfast")
        order.breakfast.time = input("What time would you like your breakfast ready? ")
        order.breakfast.location = whatDiningHall("breakfast")

    if l :
        order.lunch.food = collectFood("lunch")
        order.lunch.time = input("What time would you like your lunch ready? ")
        order.lunch.location = whatDiningHall("lunch")

    if d :
        order.dinner.food = collectFood("dinner")
        order.dinner.time = input("What time would you like your dinner ready? ")
        order.dinner.location = whatDiningHall("dinner")

    return order

def collectFood(mealType: str) -> list:
    lst = []
  
    # number of elements as input
    numFood = input("Enter the number of items you would like to order for " + mealType + "?: ")
    if numFood.isdigit():
        n = int(numFood)
    else:
        print("Please enter a whole number")
        return collectFood(mealType)
    # iterating till the range
    for i in range(0, n):
        ele = input("Type one item: ")
  
        lst.append(ele) # adding the element
      
    return lst

def recognize(doc: Document) -> Person:
    """
    Takes in a text document and if the person is the person in the doc it goes into ordering, if not it takes the new persons information and returns it
    """
    person = Person(personDoc.readline()[6:-1], personDoc.readline()[7:-1], personDoc.readline()[21:])
    temp = input("Are you " + person.name + "? ").lower()
    if temp == "no":
        person.name = input("What is your first and last name? ")
        person.phone = input("What is your phone number? ")
        person.restriction = input("What are your dietary restrictions? ")
        return person
    elif temp == "yes":
        return person
    else:
        print("Please only type yes or no ")
        recognize(person)

#Dates
theDate = datetime.today() + timedelta(1) #tomorrows date variable
mdy = theDate.strftime("%m/%d/%Y") #prints theDate in m/d/y
m_d_y = theDate.strftime("%m:%d:%Y") #prints theDate in m_d_y
d = theDate.strftime("%A") #prints theDate in word form

#Email
RODNEY_EMAIL = "rodneydiningffco@udel.edu"
PENCADER_EMAIL = "pencaderdininghall@udel.edu"
RUSSELL_EMAIL = "russelldininghall@udel.edu"

if __name__ == "__main__": 
    personDoc = open('person.txt','r')
    person = recognize(personDoc)
    absolutePath = os.path.dirname(__file__) #Gets path to active directory
    src = absolutePath + "/Custom Meal Request Form.docx" #Gets path to form template
    dest = absolutePath + "/previousMealRequests/" + " " + m_d_y+ " " + person.name + ".docx" #gets path to the previousMealRequests folder and names file
    if os.path.exists(dest):
        print("It appears you have already ordered for today!")
        exit()
    order = takeOrder(wantBreakfast(), wantLunch(), wantDinner())

    #file creation and editing
    newForm = shutil.copyfile(src,dest)

    #email
    subject = "CUSTOM MEAL REQUEST - " + person.name + " - " + mdy

    print("Form was saved at " + dest)
    print(person.name)
    print(person.phone)
    print(person.restriction)