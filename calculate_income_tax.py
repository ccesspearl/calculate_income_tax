# Exercise 12: Calculate income tax for the given income by adhering to the rules below
# Taxable Income	Rate (in %)
# First $10,000	    0
# Next $10,000	    10
# The remaining	    20

# Expected Output:
# For example, suppose the taxable income is 45000, and the income tax payable is
# 10000*0% + 10000*10%  + 25000*20% = $6000.


# Pseudocode 

# Create a variable that will let the user input their income 
income = int(input("Enter your income here: "))

# Create a variable for income tax payable and set it to 0 
income_tax_payable = 0 

# Create an if statement for first 10000 taxable income 
if income <= 10000:
    income_tax_payable = 0 

# Create an elif for second 10000 taxable income 
elif income <= 20000: 
    second_portion = income - 10000
    income_tax_payable = second_portion*0.10

# Create an else for remaining taxable income 
# Print the results
