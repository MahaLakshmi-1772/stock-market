import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 1. Get user input
ticker = input("Enter stock ticker (e.g., AAPL): ")
start_date = input("Enter start date (YYYY-MM-DD): ")
end_date = input("Enter end date (YYYY-MM-DD): ")

# 2. Fetch data
data = yf.download(ticker, start=start_date, end=end_date)

# 3. Calculate moving averages
data['MA20'] = data['Close'].rolling(window=20).mean()
data['MA50'] = data['Close'].rolling(window=50).mean()

# 4. Plot data
plt.figure(figsize=(12, 6))
plt.plot(data['Close'], label='Close Price', color='blue')
plt.plot(data['MA20'], label='20-day MA', color='orange')
plt.plot(data['MA50'], label='50-day MA', color='green')
plt.title(f"{ticker.upper()} Price and Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
