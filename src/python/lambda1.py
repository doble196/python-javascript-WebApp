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

# Sort by closing price
data.sort(key=lambda item: item["close"])
for item in data:
    print("{symbol} closed at {close} on {date}".format(**item))

# Sort by volume
data.sort(key=lambda item: item["volume"])
for item in data:
    print("{symbol} had a volume of {volume} on {date}".format(**item))
