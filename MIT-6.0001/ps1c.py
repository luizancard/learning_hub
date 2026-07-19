annual_salary = int(input("Enter the starting salary: "))
total_cost = 1000000
semi_anual_rase = 0.07
annual_return = 0.04
months = 36
down_payment = total_cost * 0.25
monthly_salary = annual_salary / 12
current_savings = 0
saving_rate = 1
bisection_search = 0
total_money = 0
month = 0

while month <= 36:
    month += 1
    if month % 6:
        annual_salary += semi_anual_rase * annual_salary
        monthly_salary = annual_salary / 12
    total_money += monthly_salary
    if month % 12:
        total_money = total_money * annual_return
    print(month)
    print(total_money)
"""
while not down_payment - 100 <= current_savings >= down_payment + 100:
    bisection_search += 1


print("Best savings rate: ", saving_rate)
print("Steps in bisection search: ", bisection_search)
"""
