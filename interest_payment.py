def main():
    print("This is a monthly payment loan calculator")
    print("")

    principal = float(input("Input the loan amount:"))
    apr = float(input("Input the annual interest rate:"))
    years = int(input("Input amount of Year:"))

    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1-(1+monthly_interest_rate)**(-amount_of_months))

    print("The Monthly payment for this loan:"+ str(monthly_payment))
main()