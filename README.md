Hotel Prices Scraper
This Python script fetches hotel prices from Booking.com for different US states, calculates the average price for each state, and saves the results to a CSV file.

Requirements
Python 3.x
Requests
BeautifulSoup4
Pandas
Detailed Comments:
Import Statements:

Import necessary libraries for HTTP requests, HTML parsing, regular expressions, and data manipulation.
fetch_hotel_prices Function:

Constructs the URL for Booking.com based on the state and predefined check-in/check-out dates.
Sets up headers to mimic a browser.
Sends an HTTP GET request to the URL.
Checks if the request was successful (status code 200).
Parses the HTML response using BeautifulSoup.
Initializes an empty list for storing prices.
Uses a regular expression pattern to find prices in the format £xxxx.xx.
Extracts text from the HTML and finds all matches for the price pattern.
Processes the first 5 matches, converting them from strings to floats and appending them to the prices list.
Returns the list of prices.
List of US States:

A predefined list of states to be processed.
Main Data Processing Loop:

Initializes an empty list to store the collected data.
Loops through each state in the states list.
Calls fetch_hotel_prices for each state to get the list of prices.
If prices are retrieved, calculates the average price and appends a dictionary with the state and its average price to the data list.
Prints a completion message for each state.
DataFrame Creation and Sorting:

Creates a Pandas DataFrame from the data list.
Sorts the DataFrame by the 'Average Price' column in ascending order.
Prints the sorted DataFrame.
Save to CSV:

Saves the sorted DataFrame to a CSV file named hotel_prices_by_state.csv.
