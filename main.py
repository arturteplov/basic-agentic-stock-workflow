import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from tabulate import tabulate
import os


# List of stocks to analyze
stock_symbols = ["NVDA", "TSLA", "META"]

# Date range
start_date = "2012-01-01"
end_date = "2026-01-01"


# Create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Dictionary to hold dataframes
stocks_data = {}

# Download each stock
for symbol in stock_symbols:
    print(f"Downloading {symbol} data...")
    df = yf.download(symbol, start=start_date, end=end_date)
    df.to_csv(f"data/{symbol}_prices.csv")
    stocks_data[symbol] = df
print("All data downloaded!")


#Summarize each stock

# Dictionary to hold summaries
stocks_summary = {}

for symbol, df in stocks_data.items():
    summary = df.describe()
    stocks_summary[symbol] = summary
    # Save summary
    summary.to_csv(f"data/{symbol}_summary.csv")
    summary_md = summary.to_markdown()
    with open(f"data/{symbol}_summary.md", "w") as f:
        f.write(summary_md)
print("All summaries saved!")

#step 5

 


def analyze_stock(df):
    info = ""
    
    # FIX: Ensure we are dealing with a Series, not a DataFrame
    # This 'squeezes' the Close column into a 1D format
    close_prices = df['Close'].squeeze()
    
    # Max daily percentage change
    pct_change = close_prices.pct_change()
    max_change = pct_change.max()
    min_change = pct_change.min()
    
    # Trend calculation using the squeezed series
    overall_change = (close_prices.iloc[-1] - close_prices.iloc[0]) / close_prices.iloc[0]
    
    # Now this 'if' will work because overall_change is a single number (scalar)
    if overall_change > 0.05:
        info += f"Stock increased by {overall_change:.2%} over the year. "
    elif overall_change < -0.05:
        info += f"Stock decreased by {overall_change:.2%} over the year. "
    else:
        info += f"Stock remained roughly stable ({overall_change:.2%}). "
    
    # Max/Min change are also now single numbers
    if max_change > 0.05 or min_change < -0.05:
        info += "High volatility detected during the year."
    else:
        info += "Volatility was moderate."
    
    return info




# Test for one stock
analyze_stock(stocks_data["NVDA"])

#Plot each stock

for symbol, df in stocks_data.items():
    plt.figure(figsize=(10,5))
    plt.plot(df['Close'], label="Close Price")
    plt.title(f"{symbol} Stock Close Price")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"data/{symbol}_chart.png")
    plt.show()


#Generate markdown report for all stocks

report_path = "data/agentic_stock_report.md"

with open(report_path, "w") as f:
    f.write("# Agentic Stock Report\n\n")
    for symbol, df in stocks_data.items():
        f.write(f"## {symbol}\n\n")
        f.write("### Summary Statistics\n\n")
        summary_md = stocks_summary[symbol].to_markdown()
        f.write(summary_md + "\n\n")
        f.write("### AI-style Analysis\n\n")
        f.write(analyze_stock(df) + "\n\n")
        f.write(f"### Price Chart\n\n![Chart]({symbol}_chart.png)\n\n")
print(f"Report created: {report_path}")