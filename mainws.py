import requests
from bs4 import BeautifulSoup

def get_hotel_data(location, budget):
    # URL
    url = f"https://www.booking.com/searchresults.en-gb.html?label=hotels-english-en-row-BqpuUwk1WtAXtPTMt4anngS228854886432%3Apl%3Ata%3Ap1%3Ap22%2C563%2C000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-118598409%3Alp1009919%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YcsZ-Id2vkzIfTmYhvC5HOg&gclid=CjwKCAjw5v2wBhBrEiwAXDDoJfSAuW1_2wrMBBjLxFwjHgUqm3aY7-ChzxsyEbLRd_Sr1JL91voTyRoCi6gQAvD_BwE&aid=309654&dest_id=-2231099&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0"

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        hotels = soup.find_all('div', class_='bodycontraint--full-width   ')

        for hotel in hotels[:]:  
            name = hotel.find('div', class_='f6431b446c a15b38c233').text.strip()
            price = hotel.find('span', class_='e4adce92df').text.strip()
            rating = hotel.find('div', class_='a3b8729ab1 d86cee9b25').text.strip()
            address = hotel.find('span', class_='aee5343fdb def9bc142a').text.strip()

            print(f"Name: {name}")
            print(f"Price: {price}")
            print(f"Rating: {rating}")
            print(f"Address: {address}")
            print("------------------------")
    else:
        print("Failed to fetch data. Please try again later.")

def main():
    location = input("Enter the location you want to visit: ")
    budget = input("Enter your budget per night: ")

    get_hotel_data(location, budget)

if __name__ == "__main__":
    main()