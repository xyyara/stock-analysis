Question 1: Use yfinance to Extract Stock Data
Task: Reset the index, save, and display the first five rows of the tesla_data DataFrame using the head() function.

# Step 1: Import the necessary library
import yfinance as yf
# Step 2: Download Tesla stock data from Yahoo Finance
tesla_data = yf.download('TSLA', start='2020-01-01', end='2023-10-01')
# Step 3: Reset the index of the DataFrame
tesla_data.reset_index(inplace=True)
# Step 4: Display the first five rows of the DataFrame
print(tesla_data.head()) 

Question 2: Use Webscraping to Extract Tesla Revenue Data
Task: Display the last five rows of the tesla_revenue DataFrame using the tail() function.

import yfinance as yf
# Step 1: Download Tesla stock information
tesla = yf.Ticker("TSLA")
# Step 2: Get the financials (including revenue)
tesla_financials = tesla.financials
# Step 3: Extract the revenue row (Total Revenue)
tesla_revenue = tesla_financials.loc['Total Revenue']
# Step 4: Convert the Series to a DataFrame for better handling
tesla_revenue_df = tesla_revenue.reset_index()
# Step 5: Display the last five rows of the revenue data
print(tesla_revenue_df.tail())

Question 3: Use yfinance to Extract Stock Data
Task: Reset the index, save, and display the first five rows of the gme_data DataFrame using the head() function.

 # Step 1: Import the necessary library
import yfinance as yf
# Step 2: Download GameStop stock data from Yahoo Finance
gme_data = yf.download('GME', start='2020-01-01', end='2023-10-01')
# Step 3: Reset the index of the DataFrame
gme_data.reset_index(inplace=True)
# Step 4: Display the first five rows of the DataFrame
print(gme_data.head())

Question 4: Use Webscraping to Extract GameStop Revenue Data
Task: Display the last five rows of the gme_revenue DataFrame using the tail() function.

import pandas as pd
import requests
from io import StringIO
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
response = requests.get(url)
response.raise_for_status()
tables = pd.read_html(StringIO(response.text))
# Find the GameStop revenue table
gme_revenue = next(
    table for table in tables
    if any("GameStop Quarterly Revenue" in str(col)
           for col in table.columns)
)
# Standardize the column names
gme_revenue.columns = ["Date", "Revenue"]
# Display the last five rows
print(gme_revenue.tail(5))

Question 5: Plot Stock Graphs
Task: Use the make_graph() function to plot Tesla stock data and display the stock price over time.

import yfinance as yf
import matplotlib.pyplot as plt
# Question 1: Extract Tesla stock data
tesla_data = yf.download(
    "TSLA",
    period="5y",
    auto_adjust=False
)
# Reset the index
tesla_data = tesla_data.reset_index()
# Define the graph function
def make_graph(data):
    plt.figure(figsize=(12, 6))
    close_prices = data["Close"]
    if hasattr(close_prices, "ndim") and close_prices.ndim == 2:
        close_prices = close_prices.iloc[:, 0]
    plt.plot(
        data["Date"],
        close_prices,
        label="Tesla Stock Price",
        color="blue"
    )
    plt.title("Tesla Stock Price Over Time")
    plt.xlabel("Date")
    plt.ylabel("Closing Price (USD)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
# Display the graph
make_graph(tesla_data)

Question 6: Plot Stock Graphs
Task: Use the make_graph() function to plot GameStop stock data and display the stock price over time.

import yfinance as yf
import matplotlib.pyplot as plt
gme_data = yf.download("GME", period="5y", auto_adjust=False)
gme_data = gme_data.reset_index()
def make_graph(data, title):
    plt.figure(figsize=(12, 6))
    plt.plot(data["Date"], data["Close"], label="Stock Price", color="green")
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Closing Price (USD)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
make_graph(gme_data, "GameStop Stock Price Over Time")


