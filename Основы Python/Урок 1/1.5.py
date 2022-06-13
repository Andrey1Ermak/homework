revenue = int(input("Enter revenues of your company: "))
expenditure = int(input("Enter expenditures of your company: "))

if revenue > expenditure:
    print(f"Your financial result is profit. "
          f"Profitability of your business is {(revenue - expenditure)/revenue:.2f}")
    number = int(input("How many staff members in your company? "))
    print(f'Profit per staff member is {(revenue - expenditure)/number:.2f}')
elif revenue == expenditure:
    print("Your financial result is 0.")
else:
    print("Your financial result is loss")