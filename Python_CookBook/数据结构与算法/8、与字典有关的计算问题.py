"""
对字典进行各种计算
"""
price = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
min_price = min(zip(price.values(), price.keys()))
print(min_price)
max_price = max(zip(price.values(), price.keys()))
print(max_price)
