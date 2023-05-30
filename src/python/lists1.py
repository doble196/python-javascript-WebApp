# OHLCV data
data = [
    {
        "symbol": "AAPL",
        "date": "2023-01-01",
        "open": 150.5,
        "high": 152.4,
        "low": 148.5,
        "close": 152.3,
        "volume": 10000000,
    },
    {
        "symbol": "BTC",
        "date": "2023-01-01",
        "open": 45000,
        "high": 46000,
        "low": 44000,
        "close": 45500,
        "volume": 5000,
    },
    # Add more data here
]

# Print first stock/crypto data
print(data[0])

# Add new stock/crypto data
data.append(
    {
        "symbol": "ETH",
        "date": "2023-01-01",
        "open": 3000,
        "high": 3100,
        "low": 2900,
        "close": 3050,
        "volume": 7000,
    }
)

# Sort data by closing price
data.sort(key=lambda item: item["close"])

# Print list of stock/crypto data
for item in data:
    print(f"Symbol: {item['symbol']}, Close: {item['close']}")
