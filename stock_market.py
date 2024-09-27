import yfinance as yf
import mplfinance as mpf

# Download stock data
stock_data = yf.download('AAPL', start='2023-01-01', end='2023-09-01')

# Plot stock data
mpf.plot(stock_data, type='candle', style='charles', volume=True, title='AAPL Stock Price', ylabel='Price')
