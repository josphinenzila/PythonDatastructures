""" Creating a calculator to calculate the total cost of a meal in dollars. """

import sys

if __name__ == "__main__":
    meal_cost = float(input("Input the meal cost: ").strip())
    tip_percent = int(input("Input the tip percent: ").strip())
    tax_percent = int(input("Input the tax percent: ").strip())

    tip_amount = meal_cost * tip_percent / 100
    tax_amount = meal_cost * tax_percent / 100
    total_cost = str(meal_cost + tip_amount + tax_amount)

    print("The total meal cost is " + total_cost)
