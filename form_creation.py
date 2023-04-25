from dataclasses import dataclass
import os
import shutil
from stat import S_IRUSR, S_IWUSR, S_IRGRP, S_IROTH
from reportlab.pdfgen import canvas
from dotenv import load_dotenv
from datetime import datetime


@dataclass
class Person:
    name: str
    phone: str
    email: str
    restriction: str
    personal_email: str
    personal_email_password: str
    server_name: str
    server_port: str


@dataclass
class Meal:
    type: str
    time: str
    location: str
    food: list


@dataclass
class Request:
    breakfast: Meal
    lunch: Meal
    dinner: Meal
    recipients: list[str]


def duplicate_form(date_obj, user: Person, template_location: str, pdf_destination_folder: str) -> str:
    destination = pdf_destination_folder + \
        date_obj.strftime("%m-%d-%Y") + " " + user.name + ".pdf"
    shutil.copyfile(template_location, destination)
    return destination


def fill_out_pdf(date_obj, user: Person, pdf_location: str):
    """Fills out current pdf from the already copied template. 

    Args:
        date_obj (_type_): _description_
        user (Person): _description_
        pdf_location (str): _description_
    """



def load_person(path: str) -> Person:
    """_summary_

    Args:
        path (str): _description_

    Returns:
        Person: _description_
    """
    env_path = os.path.join('.', path)
    load_dotenv(env_path)
    return Person(os.getenv("NAME"), os.getenv("PHONE_NUMBER"), os.getenv("SCHOOL_EMAIL"), os.getenv("DIETARY_RESTRICTIONS"),
                  os.getenv("PERSONAL_EMAIL"), os.getenv("PERSONAL_EMAIL_PASSWORD"), os.getenv("SERVER_NAME"), os.getenv("SERVER_PORT"))


if __name__ == "__main__":
    date_str = datetime.now()
    user = load_person('.env')
    fill_out_pdf(date_str, user, duplicate_form(date_str, user, "./Custom Meal Request Form.pdf",
                                                "./previous_meal_requests/"))
