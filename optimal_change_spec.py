from optimal_change import optimal_change

print(optimal_change(1000, 1173.26) == 'The optimal change for an item that costs $1000 with an amount paid of $1173.26 is 1 $100 bill, 1 $50 bill, 1 $20 bill, 3 $1 bills, 1 quarter, and 1 penny.')

print(optimal_change(20,20) == 'No change is due.')

print(optimal_change(1000000,1) == 'Not enough money to purchase.')

print(optimal_change(5,11.33) == 'The optimal change for an item that costs $5 with an amount paid of $11.33 is 1 $5 bill, 1 $1 bill, 1 quarter, 1 nickel and 3 pennies.')

