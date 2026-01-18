# Agentic Stock Workflow

An **automated stock data workflow** that downloads historical stock prices, generates statistical summaries, visualizes trends, and produces a Markdown report with AI-style analysis.  

This project demonstrates a **small, agentic workflow**—a step toward building more complex AI orchestration pipelines.  

---

## Features

- Downloads historical stock prices for multiple symbols (e.g., NVDA, TSLA, META) using `yfinance`.
- Generates summary statistics (`mean`, `std`, `min`, `max`) for each stock.
- Detects trends and volatility and produces **AI-style textual analysis**.
- Plots stock closing prices and saves charts as PNG files.
- Compiles everything into a **Markdown report** for easy sharing.
- Modular and extensible for future enhancements.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/basic-agentic-stock-workflow.git
cd agent-stock-prices
```


2. Create and activate a virtual environment (Mac/Linux):

```bash
python3.14 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install --upgrade pip
pip install pandas matplotlib yfinance tabulate
```

4. Run the workflow:

```bash
python main.py
```

5. Output files are saved in data/:

*_prices.csv → Raw stock data

*_summary.csv / *_summary.md → Statistics

*_chart.png → Stock charts

agentic_stock_report.md → Complete report

6. Add more stocks by updating the stock_symbols list in main.py.

7. Enhance trends or AI-style summaries by editing analyze_stock(df).

8. Keep your virtual environment and caches out of Git by using .gitignore.

9. Commit changes and push to GitHub to track improvements.

10. Experiment freely — the workflow is modular and ready for extension into more complex AI orchestrators.