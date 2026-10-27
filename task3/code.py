
# Campus Event Financial Planning

participants = int(input("Enter expected participants: "))

venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost: "))
transport = float(input("Enter transport cost: "))
certificates = float(input("Enter certificate cost: "))

sponsorship = float(input("Enter sponsorship amount: "))
fee = float(input("Enter registration fee per participant: "))

if (participants <= 0 or venue < 0 or equipment < 0
        or catering < 0 or transport < 0
        or certificates < 0 or sponsorship < 0 or fee <= 0):
    print("Invalid input.")
else:
    total_cost = venue + equipment + catering + transport + certificates

    remaining_cost = max(0, total_cost - sponsorship)

    # Minimum registrations needed after sponsorship
    break_even = int(remaining_cost / fee)

    if break_even * fee < remaining_cost:
        break_even += 1

    revenue = sponsorship + participants * fee
    balance = revenue - total_cost

    print("\n----- Event Financial Report -----")
    print("Total expenditure: ₹", total_cost)
    print("Sponsorship: ₹", sponsorship)
    print("Sponsorship shortfall: ₹", remaining_cost)
    print("Break-even registrations:", break_even)
    print("Expected registration revenue: ₹", participants * fee)
    print("Total expected revenue: ₹", revenue)

    if balance > 0:
        print("Expected surplus: ₹", balance)
    elif balance == 0:
        print("The event breaks even.")
    else:
        print("Expected deficit: ₹", abs(balance))

