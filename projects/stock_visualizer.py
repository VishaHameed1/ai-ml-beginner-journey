import yfinance as yf
import matplotlib.pyplot as plt

def get_stock_data(ticker):
    print(f"Fetching data for {ticker}...")
    # Get 1 month of historical data
    stock = yf.Ticker(ticker)
    df = stock.history(period="1mo")

    if not df.empty:
        # Plotting the closing price
        plt.figure(figsize=(10, 5))
        df['Close'].plot(color='green', linewidth=2)
        plt.title(f"{ticker} Stock Price - Last 30 Days")
        plt.xlabel("Date")
        plt.ylabel("Price (USD)")
        plt.grid(True)
        plt.show()
    else:
        print("❌ Error: Ticker symbol not found. Use symbols like TSLA, AAPL, or MSFT.")

if __name__ == "__main__":
    symbol = input("Enter Stock Ticker (e.g., TSLA, AAPL): ").upper()
    get_stock_data(symbol)