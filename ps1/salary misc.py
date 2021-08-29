semi_annual_raise = .07
r = .04
down_payment = .25
cost = 1000000.0
epsilon = 1000.0
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
