# Payroll.py

# input statements
salary = float(input("Enter the employee's salary: "))
numDependents = float(input("Enter the number of dependents: "))

# calculate taxes here
stateTax = salary * 0.065
federalTax = salary * 0.28
dependentDeduction = salary * 0.025 * numDependents
totalWithholding = stateTax + federalTax - dependentDeduction
takeHomePay = salary -totalWithholding

# output statements
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" + str(federalTax))
print("Dependent Deduction: $" + str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
