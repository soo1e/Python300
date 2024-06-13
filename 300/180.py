low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []

for i in [0,1,2,3,4]:
    print(abs(low_prices[i] - high_prices[i]))
    volatility.append(high_prices[i]-low_prices[i])