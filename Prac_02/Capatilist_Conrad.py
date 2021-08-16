"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random
OUTPUT_FILE = 0
MAX_INCREASE = 0.175  # 10%
MAX_DECREASE = 0.175  # 5%
MIN_PRICE = 1
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
day_count = 0
day = 0
out_file = open(OUTPUT_FILE, 'w')
price = INITIAL_PRICE
print("${:,.2f}".format(price))
while MIN_PRICE <= price <= MAX_PRICE:
    day_count = day_count + 1
    day = day + 1
    price_change = 0
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print("${:,.2f}".format(price,file=out_file))
    print(f"on day {day} the price was ${price:,.2f}",file=out_file)
    out_file.close()