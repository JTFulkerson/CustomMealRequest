# ----------------------------------------------------------------------------
# Created By: John Fulkerson
# With help from: Brennan Gallamoza
# Created Date: 10/4/2022
# ----------------------------------------------------------------------------

from dataclasses import dataclass
from lib2to3.pgen2.token import NAME
import os
from stat import S_IWUSR, S_IRUSR, S_IRGRP, S_IROTH
import shutil
from time import time
#from urllib import request
from xml.dom.minidom import Document

from docx2pdf import convert

#importing enviornment variables
from dotenv import load_dotenv


"""
Need to install:
pip install python-docx
pip install docx2pdf
pip install python-dotenv
"""

@dataclass
class Person:
    """Creates a person with name(string), phone(string), restriction(string)
    """
    name: str
    phone: str
    restriction: str

@dataclass
class Meal:
    """Creates a meal with fields, type(string), time(string), location(string), food(list)
    """
    type: str
    time: str
    location: str
    food: list

@dataclass
class Request:
    """Contains all 3 meals, Breakfast, Lunch, and Dinner
    """
    breakfast: Meal
    lunch: Meal
    dinner: Meal
    recipients: list[str]

def want_meal(meal: str) -> bool:
    """Intended to return True or False wether the user wants certain meal or not. 

    Returns:
        bool: _description_
    """
    user = input("Do you want to special order " + meal + "? \n").lower()
    if  user == "yes":
        return True
    elif user == "no":
        return False
    else:
        print("Please only type yes or no")
        return want_meal(meal)

def whatDiningHall(meal: str) -> str:
    """Intended to enter meal and then user is prompted what dining hall they would like that meal in. The dining hall they choose is then returned. 

    Args:
        meal (str): _description_

    Returns:
        str: _description_
    """
    while True:
        d1a = input("Which dining hall would you like " + meal + " in: \n A) Russell B) Cesear Rodney C) Pencader \n").lower()
        if d1a == "a" :
            return "Russell"
        elif d1a == "b" :
            return "Cesear Rodney"
        elif d1a == "c" :
            return "Pencader"
        else :
            print("Please enter either A, B, or C")
            return whatDiningHall(meal)

def collect_order(b: bool, l: bool, d: bool) -> Request:
    """Takes order, time, location and writes into a Request type which is returned.

    Args:
        b (bool): _description_
        l (bool): _description_
        d (bool): _description_

    Returns:
        Request: _description_
    """
    order = Request(Meal("breakfast", "", "", ""), Meal("lunch", "", "", ""), Meal("dinner", "", "", ""), [])
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

def collectFood(mealType: str) -> list[str]:
    """Prompts user with how many items they would like to order then turn all of the items into a list.

    Args:
        mealType (str): _description_

    Returns:
        list[str]: _description_
    """
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
    """Takes in a text document and if the person is the person in the doc it goes into ordering, if not it takes the new persons information and returns it.

    Args:
        doc (Document): _description_

    Returns:
        Person: _description_
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

def layout_order(meal: Meal) -> str:
    """Takes a meal and outputs the food items in the string with line breaks between items.

    Args:
        meal (Meal): _description_

    Returns:
        str: _description_
    """
    order_string = ""
    for item in meal.food:
        order_string += item + "\n"
    return order_string

def convert_pdf(path: str):
    """Tells user to convert file to pdf and waits for it to happen.

    Args:
        path (str): Path to docx that needs to be converted
    """
    convert(path)
    os.remove(path)

def convert_location_to_email(loc: str) -> str:
    if(loc == "Russell"):
        return"russelldininghall@udel.edu"
    elif(loc == "Cesear Rodney"):
        return "rodneydiningffco@udel.edu"
    elif(loc == "Pencader"):
        return "pencaderdininghall@udel.edu"
    else:
        return ""

def create_recipient_list(order: Request) -> list[str]:
    recipientList = [SCHOOL_EMAIL]
    if convert_location_to_email(order.breakfast.location) != "":
        recipientList.append(convert_location_to_email(order.breakfast.location))
    if convert_location_to_email(order.lunch.location) != "":
        recipientList.append(convert_location_to_email(order.lunch.location))
    if convert_location_to_email(order.dinner.location) != "":
        recipientList.append(convert_location_to_email(order.dinner.location))
    if not recipientList:
        print("No meals were ordered")
        exit()
    return list(set(recipientList))

def make_new_form(person: Person, order: Request):
    formTemplate = "./Custom Meal Request Form.docx" #Gets path to form template
    newForm = shutil.copyfile(formTemplate,word_docx_destination)
    os.chmod(word_docx_destination, S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH)
    document = Document(word_docx_destination)
    styles = document.styles
    table = document.tables[0]
    table.cell(0, 0).text = "Name: " + person.name
    table.cell(1, 0).text = "Day of Week: " + d
    table.cell(1, 3).text = "Date: " + mdy
    table.cell(2, 0).text = "Diet Restriction: " + person.restriction
    table.cell(0, 3).text = "Phone: " + person.phone

    table.cell(3, 1).text = "Time: " + order.breakfast.time
    table.cell(3, 2).text = "Location: " + order.breakfast.location
    table.cell(4, 0).text = layout_order(order.breakfast)

    table.cell(5, 1).text = "Time: " + order.lunch.time
    table.cell(5, 2).text = "Location: " + order.lunch.location
    table.cell(6, 0).text = layout_order(order.lunch)

    table.cell(7, 1).text = "Time: " + order.dinner.time
    table.cell(7, 2).text = "Location: " + order.dinner.location
    table.cell(8, 0).text = layout_order(order.dinner)

    for row in table.rows:
     for cell in row.cells:
         paragraphs = cell.paragraphs
         for paragraph in paragraphs:
             for run in paragraph.runs:
                 font = run.font
                 font.size= Pt(16)

    document.save(word_docx_destination)

import smtplib
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
def send_email(send_from, name, send_to, subject, message, files=[],
              server="localhost", port=587, username='', password='',
              use_tls=True):
    """Compose and send email with provided info and attachments.

    Args:
        send_from (str): from name
        send_to (list[str]): to name(s)
        subject (str): message title
        message (str): message body
        files (list[str]): list of file paths to be attached to email
        server (str): mail server host name
        port (int): port number
        username (str): server auth username
        password (str): server auth password
        use_tls (bool): use TLS mode
    """
    msg = MIMEMultipart()
    msg['From'] = name + " <" + send_from + ">"
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(message))

    for path in files:
        part = MIMEBase('application', "octet-stream")
        with open(path, 'rb') as file:
            part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        'attachment; filename={}'.format(Path(path).name))
        msg.attach(part)

    smtp = smtplib.SMTP(server, port)
    if use_tls:
        smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()

#Dates
from datetime import date, datetime, timedelta
theDate = datetime.today() #+ timedelta(1) #tomorrows date variable
mdy = theDate.strftime("%m/%d/%Y") #prints theDate in m/d/y
m_d_y = theDate.strftime("%m-%d-%Y") #prints theDate in m_d_y
d = theDate.strftime("%A") #prints theDate in word form

if __name__ == "__main__":
    env_path = os.path.join('.', '.env')
    load_dotenv(env_path)

    #Personal Info
    NAME = os.getenv("NAME")
    PHONE_NUMBER = os.getenv("PHONE_NUMBER")
    DIETARY_RESTRICTIONS = os.getenv("DIETARY_RESTRICTIONS")
    SCHOOL_EMAIL = os.getenv("SCHOOL_EMAIL")
    PERSONAL_EMAIL = os.getenv("PERSONAL_EMAIL")
    PERSONAL_EMAIL_PASSWORD = os.getenv("PERSONAL_EMAIL_PASSWORD")
    SERVER_NAME = os.getenv("SERVER_NAME")
    SERVER_PORT = os.getenv("SERVER_PORT")
    
    print("Taking order for " + d)
    personDoc = open('person.txt','r')
    person = recognize(personDoc)
    word_docx_destination = "./previousMealRequests/" + m_d_y+ " " + person.name + ".docx" #gets path to the previousMealRequests folder and names file
    pdf_destination = "./previousMealRequests/" + m_d_y+ " " + person.name + ".pdf" #gets path to the previousMealRequests folder and names file
    if os.path.exists(pdf_destination):
        print("It appears you have already ordered for today!")
        exit()
    order = collect_order(want_meal('breakfast'), want_meal('lunch'), want_meal('dinner'))

    #file creation and editing
    from docx import Document
    from docx.shared import Pt
    make_new_form(person, order)

    recipients = create_recipient_list(order)
    convert_pdf(word_docx_destination)
    
    #Sending Email
    subject = "CUSTOM MEAL REQUEST - " + person.name + " - " + mdy
    body = input("Type the email body: ")
    send_email(PERSONAL_EMAIL, NAME, recipients, subject, body, [pdf_destination], SERVER_NAME, SERVER_PORT, PERSONAL_EMAIL, PERSONAL_EMAIL_PASSWORD)

    print("Form was saved at " + pdf_destination)