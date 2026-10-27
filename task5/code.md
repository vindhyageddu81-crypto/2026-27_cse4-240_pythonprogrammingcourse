# Case Study 13: ATM Transaction Sequence Simulation

## 1. Problem statement

Develop a Python program to simulate ATM transactions by processing deposits and withdrawals. The program should maintain the account balance, enforce withdrawal limits, reject invalid transactions, prevent withdrawals exceeding the available balance, and generate a summary of all successful and rejected transactions.

## 2. Sample ATM policy

These are illustrative rules for the project.

| Rule                               | Policy             |
| ---------------------------------- | ------------------ |
| Initial balance                    | ₹5,000             |
| Minimum deposit                    | Greater than ₹0    |
| Minimum withdrawal                 | Greater than ₹0    |
| Maximum withdrawal per transaction | ₹10,000            |
| Insufficient balance               | Reject withdrawal  |
| Invalid transaction type           | Reject transaction |

## 3. Algorithm

1. Start.
2. Input the initial account balance.
3. Input the number of transactions.
4. For each transaction, enter the transaction type and amount.
5. If the transaction is a deposit, validate the amount and add it to the balance.
6. If it is a withdrawal, validate the amount, withdrawal limit, and available balance.
7. Reject invalid transactions without changing the balance.
8. Record successful deposits, successful withdrawals, and rejected transactions.
9. Display the updated balance after each transaction.
10. Calculate the total deposited and withdrawn amounts.
11. Display the final balance and transaction summary.
12. Stop.

## 4. Flowchart
``` mermaid

flowchart TD
    A([Start]) --> B[/Input initial balance and transaction count/]
    B --> C[/Input transaction type and amount/]
    C --> D{Valid amount?}
    D -- No --> E[Reject transaction]
    D -- Yes --> F{Deposit or withdrawal?}
    F -- Deposit --> G[Add amount to balance]
    F -- Withdrawal --> H{Within withdrawal limit?}
    H -- No --> E
    H -- Yes --> I{Sufficient balance?}
    I -- No --> E
    I -- Yes --> J[Subtract amount from balance]
    G --> K[Update transaction summary]
    J --> K
    E --> L[Record rejected transaction]
    K --> M{More transactions?}
    L --> M
    M -- Yes --> C
    M -- No --> N[/Display final balance and summary/]
    N --> O([Stop])
```



## 6. Sample output

```
Enter initial balance: ₹5000
Enter number of transactions: 4

Transaction 1
Enter transaction type (deposit/withdraw): deposit
Enter amount: ₹2000
Deposit successful.
Current balance: ₹7000

Transaction 2
Enter transaction type (deposit/withdraw): withdraw
Enter amount: ₹1500
Withdrawal successful.
Current balance: ₹5500

Transaction 3
Enter transaction type (deposit/withdraw): withdraw
Enter amount: ₹12000
Rejected: Exceeds withdrawal limit.
Current balance: ₹5500

Transaction 4
Enter transaction type (deposit/withdraw): withdraw
Enter amount: ₹6000
Rejected: Insufficient balance.
Current balance: ₹5500

----- ATM Transaction Summary -----
Total deposits: ₹2000
Total withdrawals: ₹1500
Successful transactions: 2
Rejected transactions: 2
Final balance: ₹5500
```

## 7. Test cases

| Test | Transaction                           | Expected result                |
| ---- | ------------------------------------- | ------------------------------ |
| 1    | Deposit ₹2,000                        | Balance increases by ₹2,000    |
| 2    | Withdraw ₹1,000 with sufficient funds | Successful                     |
| 3    | Withdraw ₹12,000                      | Rejected: withdrawal limit     |
| 4    | Withdraw more than balance            | Rejected: insufficient balance |
| 5    | Deposit ₹0                            | Rejected: invalid amount       |
| 6    | Enter `transfer` as transaction type  | Rejected: invalid type         |

## 8. Conclusion

This project demonstrates the use of Python loops, conditional statements, arithmetic operations, and counters to simulate ATM transactions. It maintains an accurate running balance and generates a summary without allowing rejected transactions to affect the account.
