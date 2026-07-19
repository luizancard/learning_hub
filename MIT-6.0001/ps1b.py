annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_anual_rase = float(input("Enter the semi­annual raise, as a decimal:"))
portion_down_payment = total_cost * 0.25
monthly_salary = annual_salary / 12
current_savings = 0
months = 0

while portion_down_payment > current_savings:
    if months != 0 and months % 6 == 0:
        annual_salary += annual_salary * semi_anual_rase
        monthly_salary = annual_salary / 12
    months += 1
    current_savings += (portion_saved * monthly_salary) + (current_savings * 0.04) / 12

print("Number of months: ", months)
