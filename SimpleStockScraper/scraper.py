import requests
from bs4 import BeautifulSoup
import csv

url = "https://finance.yahoo.com/quote/AAPL"

response = requests.get(url)

if response.status_code == 200:
    print("Successfully retrieved the webpage!")

    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    
    price_tag = soup.find('fin-streamer', {'data-field': 'regularMarketPrice'})
    
    if price_tag:
        stock_price = price_tag.text
        print(f"The current stock price of Apple (AAPL) is: ${stock_price}")
        
        # Save the data into a CSV file
        with open('stock_prices.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Stock", "Price"])  
            writer.writerow(["AAPL", stock_price])  
    else:
        print("Stock price not found on the page.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
