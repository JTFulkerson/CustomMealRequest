import requests
import json
from bs4 import BeautifulSoup


def url_to_json(url: str, filename: str) -> None:
    # Send an HTTP request to the URL and get the response
    response = requests.get(url)

    # Get the content of the response as a string
    content = response.content.decode('utf-8')

    # Convert the string to a JSON object
    json_data = {'content': content}

    # Scrape the HTML content using BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')
    time_div = soup.find('div', {'class': 'location__details'})

    # Save the JSON object to a file
    with open(filename, 'w') as outfile:
        json.dump(response, outfile)


# def url_to_json(url: str, filename: str) -> None:
#     # Send an HTTP request to the URL and get the response
#     response = requests.get(url)

#     # Get the content of the response as a string
#     content = response.content.decode('utf-8')

#     # Scrape the HTML content using BeautifulSoup
#     soup = BeautifulSoup(content, 'html.parser')

#     # Find the div element that contains the breakfast hours
#     breakfast_div = soup.find('div', {'class': 'mealPeriod', 'data-id': '4'})

#     # Extract the breakfast hours and days from the div element
#     if breakfast_div is not None:
#         breakfast_hours = breakfast_div.find(
#             'div', {'class': 'location__times'}).text.strip()
#         breakfast_days = breakfast_div.find(
#             'div', {'class': 'location__hours'}).text.strip()
#     else:
#         breakfast_hours = ''
#         breakfast_days = ''

#     # Convert the extracted data to a dictionary
#     data = {'breakfast_hours': breakfast_hours,
#             'breakfast_days': breakfast_days}

#     # Save the dictionary to a JSON file
#     with open(filename, 'w') as outfile:
#         json.dump(data, outfile)


if __name__ == "__main__":
    url_to_json("https://udel.campusdish.com/en/LocationsAndMenus/CaesarRodneyFreshFoodCompany",
                "Ceasar_Rodney_Hours.json")
