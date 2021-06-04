
def optimal_change(item_cost, amount_paid):
    change_var = round(amount_paid - item_cost,3)
    change_quantity = []
    comma = ','

    # While somewhat similar to Roman Numerals, I found this to be altogether much more challenging. Below is a key to USD currency denominations.

    denomination_map = {
        '$100':100,
        '$50':50,
        '$20':20,
        '$10':10,
        '$5':5,
        '$1':1,
        'quarter':.25,
         'dime':.1,
         'nickel':.05,
         'penny':.01
         }

    # Loops through denomination_map to append the values >= to our current change total. Similar to working with roman numerals, we subtract the denomination's value from the remaining change total. Rounding to avoid errors in calculation and infinite float values.

    for index, value in enumerate(denomination_map):
        while change_var >= denomination_map[value]:
                change_quantity.append(denomination_map[value])
                change_var = round(change_var-denomination_map[value],3)
    
    # A horrible violation of DRY in its entirety. My apologies, could not find a better solution in time! Could definitely use a ton of refactoring... I look forward to reviewing this.

    hundred = ''
    fifty = ''
    twenty = ''
    ten = ''
    five = ''
    one = ''
    quarter = ''
    dime = ''
    nickel = ''
    penny = ''

    if change_quantity.count(100) == 1:
        hundred += ' 1 $100 bill'
    
    elif change_quantity.count(100) >= 1:
        hundred += f' {change_quantity.count(100)} $100 bills'

    if change_quantity.count(50) == 1:
        fifty += ' 1 $50 bill'
    
    elif change_quantity.count(50) >= 1:
        fifty += f' {change_quantity.count(50)} $50 bills'

    if change_quantity.count(20) == 1:
        twenty += ' 1 $20 bill'
    
    elif change_quantity.count(20) >= 1:
        twenty += f' {change_quantity.count(20)} $20 bills'

    if change_quantity.count(10) == 1:
        ten += ' 1 $10 bill'
    
    elif change_quantity.count(10) >= 1:
        ten += f' {change_quantity.count(10)} $10 bills'

    if change_quantity.count(5) == 1:
        five += ' 1 $5 bill'
    
    elif change_quantity.count(5) >= 1:
        five += f' {change_quantity.count(5)} $5 bills'

    if change_quantity.count(1) == 1:
        one += ' 1 $1 bill'
    
    elif change_quantity.count(1) >= 1:
        one += f' {change_quantity.count(1)} $1 bills'

    if change_quantity.count(.25) == 1:
        quarter += ' 1 quarter'
    
    elif change_quantity.count(.25) >= 1:
        quarter += f' {change_quantity.count(.25)} quarters'

    if change_quantity.count(.10) == 1:
        dime += ' 1 quarter'
    
    elif change_quantity.count(.10) >= 1:
        dime += f' {change_quantity.count(.1)} dimes'

    if change_quantity.count(.05) == 1:
        nickel += ' 1 nickel'
    
    elif change_quantity.count(.05) >= 1:
        nickel += f' {change_quantity.count(.05)} nickels'

    if change_quantity.count(.01) == 1:
        penny += ' and 1 penny'
    
    elif change_quantity.count(.01) >= 1:
        penny += f' and {change_quantity.count(.01)} pennies'
    
    # Edge cases

    if amount_paid < item_cost:
        return('Not enough money to purchase.')

    if len(change_quantity) == 0:
       return('No change is due.')

   
    # Again, my apologies for this absolute mess. I am definitely in need of cleaner methods of string interpolation and formatting. 

    return(
        f'The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is' 
        + f'{hundred}''{}'.format(comma if len(hundred)>0 else '') 
        + f'{fifty}''{}'.format(comma if len(fifty)>0 else '') 
        + f'{twenty}''{}'.format(comma if len(twenty)>0 else '') 
        + f'{ten}''{}'.format(comma if len(ten)>0 else '') 
        + f'{five}''{}'.format(comma if len(five)>0 else '') 
        + f'{one}''{}'.format(comma if len(one)>0 else '') 
        + f'{quarter}''{}'.format(comma if len(quarter)>0 else '') 
        + f'{dime}''{}'.format(comma if len(dime)>0 else '') 
        + f'{nickel}' 
        + f'{penny}.'
        )


