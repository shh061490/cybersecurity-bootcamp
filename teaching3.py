# Write a program in python that splits the bill evenly between group.
# Ask how much they want to tip and how many people
#Example
#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6

#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.:muscle:
#Write your code below this line
def split_bill(): # this is where you define the function
    
    bill = float(input("Enter the total bill amount ($): "))
    tip_percentage = float(input("Enter the tip percentage (15 for 15% tip etc.):"))
    payees = int(input("Enter the number of payees:"))

    total_amount = bill * (1 + tip_percentage / 100)
    amount_per_payee = total_amount / payees
    amount_per_payee = round(amount_per_payee, 2)
    total_bill = total_amount + tip_percentage # could be written total_bill =round(total_amount, 2)
    print(f"Each person should pay: ${amount_per_payee:.2f}")
    print(f"Total amount of bill after gratuity: ${total_bill:.2f}")

split_bill() # Here is where you call up the func or the script won't know what its doing or won't work
