# coding: utf-8
import csv
from pathlib import Path

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""

loan_costs = [500, 600, 200, 1000, 450]


""" Calculates the total number and amount of loans in the list_costs
    and based on that the average loan amount"""

number_of_loans=len(loan_costs)
total_loans=sum(loan_costs)
average_loan_amount = round(total_loans/number_of_loans,2)

"""Prints the total number and amount of loans and the average loan amount"""

print(f"The total value of the loans is ${total_loans}")
print(f"The loan portfolio consists of {number_of_loans} loans")
print(f"The average loan amount is ${average_loan_amount}")

"""Part 2: Analyze Loan Data.

    Analyze the loan to determine the investment evaluation.

    Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

    1. Use get() on the dictionary of additional information to extract the 
        **Future Value** and **Remaining Months** on the loan.
        a. Save these values as variables called `future_value` and `remaining_months`.
        b. Print each variable.

        @NOTE:
        **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
        **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

    2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
    3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}


"""Extracts the Future Value and Remaining Value of the loan from dictionary
    and assigns it to the variables"""
    
future_value=loan.get("future_value")
remaining_months=loan.get("remaining_months")
annual_discount_rate=0.2

"""Prints the Future Value and the amount of months remaining for the loan repayment"""
print("The future value of the loan is $", future_value)
print(f"It remains {remaining_months} months for the loan")


"""Calculates the Present Value of the Loan and prints it"""

present_value=round(future_value/(1+annual_discount_rate/12)**remaining_months,2)
print("The Present Value of this loan is $", present_value)

"""Compairs the Present Value of the Loan to its price to decide whether to buy it or not"""

if present_value >loan.get("loan_price"):
    print("The cost of the loan is worth buying!")
elif present_value == loan.get("loan_price"):
    print("The cost of the loan is worth at least considering!")
else:
    print("The loan is too expensive and not worth the price!")    

"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

""" This function calculates the Present Value 
    requiered parameters are
    1. future_value
    2. anual_discount_rate
    3. remaining_months
and returns present_value  
"""

def pres_value(future_value,annual_discount_rate,remaining_months):
    present_value =future_value/(1+annual_discount_rate/12)**remaining_months
    return present_value


"""Assigns the values from the new_loan dictionary to the variables"""

future_value=new_loan.get("future_value")
remaining_months=new_loan.get("remaining_months")
annual_discount_rate=0.2

"""Calls the function pres_value to calculate the Present Value of the new loan"""

present_value=round(pres_value(future_value,annual_discount_rate,remaining_months), 2)
print(f"The present value of the new loan is $ {present_value}")


"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than 500
    b. If the loan_price is less than 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

inexpensive_loans=[]

"""Finds the loans that cost less or equal than $ 500 in the list of dictionaries
    and creates new list of dictionaries called 'inexpensive_loans' 
    then prints it"""

for each_loan in loans:
    price_of_loan=each_loan.get("loan_price")
    if price_of_loan<=500:
        inexpensive_loans.append(each_loan)

print(inexpensive_loans)

"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
        d. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

"""


"""Sets the csv output path to record the data
    and defines the header in the file"""

csvpath=Path("inexpensive_loans.csv")
header=(inexpensive_loans[1].keys())

"""
Writes in the 'inexpensive_loans.csv' all inexpencive loans 
"""

with open(csvpath,'w',) as csvfile:
    csvwriter=csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(header)
    for each_loan in inexpensive_loans:
        csvwriter.writerow(each_loan.values())
