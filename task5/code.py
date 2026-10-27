

# ATM Transaction Sequence Simulation

balance = float(input("Enter initial balance: ₹"))
n = int(input("Enter number of transactions: "))

total_deposits = 0
total_withdrawals = 0
successful = 0
rejected = 0

if balance < 0 or n < 0:
    print("Invalid initial balance or transaction count.")

else:
    for i in range(n):
        print("\nTransaction", i + 1)
        transaction_type = input(
            "Enter transaction type (deposit/withdraw): "
        ).lower()

        amount = float(input("Enter amount: ₹"))

        if amount <= 0:
            print("Rejected: Amount must be positive.")
            rejected += 1

        elif transaction_type == "deposit":
            balance += amount
            total_deposits += amount
            successful += 1
            print("Deposit successful.")

        elif transaction_type == "withdraw":
            if amount > 10000:
                print("Rejected: Exceeds withdrawal limit.")
                rejected += 1

            elif amount > balance:
                print("Rejected: Insufficient balance.")
                rejected += 1

            else:
                balance -= amount
                total_withdrawals += amount
                successful += 1
                print("Withdrawal successful.")

        else:
            print("Rejected: Invalid transaction type.")
            rejected += 1

        print("Current balance: ₹", round(balance, 2))

    print("\n----- ATM Transaction Summary -----")
    print("Total deposits: ₹", round(total_deposits, 2))
    print("Total withdrawals: ₹", round(total_withdrawals, 2))
    print("Successful transactions:", successful)
    print("Rejected transactions:", rejected)
    print("Final balance: ₹", round(balance, 2))
