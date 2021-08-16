"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter Sales Value: $"))
small_bonus = 0.1
large_bonus = 0.15

if sales < 1000:
    final_bonus=small_bonus * sales
    print(final_bonus)
elif sales >= 1000:
    final_bonus = sales * large_bonus
    print (final_bonus)
