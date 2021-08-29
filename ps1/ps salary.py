#ps1 (saving)
semi_annual_raise = .07
r = .04
down_payment = .25
cost = 1000000
epsilon = 100
money_needed = down_payment*cost
current_savings = 0
starting_salary = float(input("Starting salary? "))
monthly_salary = starting_salary/12


low = 0
high = 10000

guess = (high + low) / 2 

num_guesses = 0

while abs(current_savings - cost >= epsilon):
    for i in range (36):
        investment_flow =  current_savings*r/12
        current_savings += investment_flow + monthly_salary*(guess/10000)
    
        if i%6==0:
            monthly_salary = monthly_salary*(1+semi_annual_raise)
    
    if (current_savings > money_needed):
        high = guess
        guess = (high + low)/2
        
    elif (current_savings < money_needed):
        low = guess
        guess = (high + low)/2
        
    else:
        break
    
    num_guesses += 1



#ps1b (saving, with raise)
portion_down_payment = 0.25
current_savings = 0
r = 0.04
annual_salary = float(input("How much is your annual salary? "))
portion_saved = float(input("What percentage of your salary are you going to save each month? "))
total_cost = float(input("How much does your dream house cost? "))
semi_annual_raise = float(input("Raise, as a decimal? "))
monthly_salary = annual_salary/12
months_needed = 0
money_needed =  total_cost*portion_down_payment






while current_savings < money_needed:
    investment_flow =  current_savings*r/12
    current_savings += investment_flow + monthly_salary*portion_saved
    months_needed += 1
    if months_needed>0 and months_needed%6==0:
        monthly_salary = monthly_salary*(1+semi_annual_raise)

    

print("You will need", months_needed, "months to save up for your down payment")


#ps1c (finding right amount)
semi_annual_raise = .07
r = .04
down_payment = .25
cost = 1000000.0
epsilon = 100.0
money_needed = down_payment*cost
current_savings = 0.0
starting_salary = float(input("Starting salary? "))
monthly_salary = starting_salary/12


low = 0.0
high = 10000.0

guess = (high+low)/2

num_guesses = 0

while abs(current_savings - money_needed) >= epsilon:
    
    current_savings = 0.0
    monthly_salary = starting_salary/12
    
    for i in range (36):
        investment_flow =  current_savings*r/12
        current_savings += investment_flow + monthly_salary*(guess/10000)
    
        if i%6==0:
            monthly_salary = monthly_salary*(1+semi_annual_raise)
    
    if (current_savings > money_needed):
        high = guess
        guess = float((high + low)/2)
        
    elif (current_savings < money_needed):
        low = guess
        guess = float((high + low)/2)
        
    num_guesses += 1
    if num_guesses > 100:
        break

from decimal import Decimal
final = Decimal(guess/10000)

if num_guesses <= 100:
    print("Desired saving rate is", round(final,4))
    print("took me", num_guesses, "guesses")
else:
    print("ur pay too low")


