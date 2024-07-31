import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

# Define a function to fetch hotel prices from Booking.com
def fetch_hotel_prices(state):
    # Construct the URL for Booking.com search results (modify query as needed)
    url = f'https://www.booking.com/searchresults.html?ss={state}&checkin_month=12&checkin_monthday=1&checkout_month=12&checkout_monthday=31&checkin_year=2024&checkout_year=2024'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    
    # Check if request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve data for {state}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract hotel prices (modify the selectors based on the actual HTML structure)
    prices = []
    
    # Define the regular expression pattern for prices
    pattern = r'£(\d+(?:,\d{3})*(?:\.\d{1,2})?)'
    
    # Extract all text from the HTML and find prices using regex
    text = soup.get_text()
    matches = re.findall(pattern, text)
    # Process matches to convert them into float values
    for match in matches[:5]:
        # Add the currency symbol back and convert to float
        price_str = f'£{match}'
        try:
            # Remove the currency symbol and convert to float
            price = float(match.replace(',', ''))
            prices.append(price)
        except ValueError:
            continue
    
    return prices

# List of US states (you may need to adjust or use more specific locations)
states = [
    'California', 'Texas', 'New York', 'Florida', 'Georgia', 'Illinois', 
    'Pennsylvania', 'Ohio', 'Michigan', 'North Carolina', 'New Jersey', 
    'Virginia', 'Washington', 'Arizona', 'Massachusetts', 'Tennessee', 
    'Indiana', 'Missouri', 'Maryland', 'Wisconsin', 'Colorado', 'Minnesota', 
    'South Carolina', 'Alabama', 'Oklahoma', 'Kentucky', 'Louisiana', 
    'Connecticut', 'Iowa', 'Arkansas', 'Mississippi', 'Kansas', 'Nebraska', 
    'West Virginia', 'New Mexico', 'Maine', 'New Hampshire', 'Montana', 
    'Wyoming', 'South Dakota', 'North Dakota', 'Vermont', 'Delaware', 
    'Rhode Island', 'Hawaii', 'Idaho', 'Alaska'
]

# Fetch and process data
data = []
for state in states:
    prices = fetch_hotel_prices(state)
    if prices:
        average_price = sum(prices) / len(prices) if prices else None
        data.append({'State': state, 'Average Price': average_price})
        print("Completed - " + state)

# Create a DataFrame
df = pd.DataFrame(data)

# Sort DataFrame by average price
df_sorted = df.sort_values(by='Average Price')

# Display the results
print(df_sorted)

# Save to CSV if needed
df_sorted.to_csv('hotel_prices_by_state.csv', index=False)
