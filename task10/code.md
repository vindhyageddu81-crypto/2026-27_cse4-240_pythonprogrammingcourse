# Case Study 9: Integrated E-Commerce Order Processing and Reconciliation

## 1. Problem statement

Develop a Python program to manage e-commerce orders by processing product purchases, applying discounts, recording dispatches and returns, and updating inventory. The program should calculate net revenue, identify discrepancies between ordered and dispatched quantities, and generate a final inventory summary.

## 2. Sample business rules

These are illustrative rules for the project.

| Rule           | Policy                                                     |
| -------------- | ---------------------------------------------------------- |
| Discount       | 10% when order value is ₹5,000 or more                     |
| Dispatch       | Stock decreases by the dispatched quantity                 |
| Return         | Returned stock is added back to inventory after inspection |
| Invalid order  | Reject quantities greater than available stock             |
| Reconciliation | Flag differences between ordered and dispatched quantities |
| Net revenue    | Sales after discounts minus refunds for returned items     |

## 3. Algorithm

1. Start.
2. Store product names, prices, and initial stock quantities.
3. Input order details, including ordered, dispatched, and returned quantities.
4. Validate quantities against available stock and ensure returns do not exceed dispatched quantities.
5. Calculate the order value and apply eligible discounts.
6. Update inventory by subtracting dispatched items.
7. Add inspected, resalable returned items back to inventory.
8. Calculate refunds and net revenue.
9. Compare ordered and dispatched quantities to identify discrepancies.
10. Display order details, revenue, discrepancies, and final stock levels.
11. Stop.

## 4. Flowchart
``` mermaid

flowchart TD
    A([Start]) --> B[Initialize product inventory]
    B --> C[Input order and dispatch details]
    C --> D{Valid quantities and stock?}
    D -- No --> E[Reject order and report error]
    D -- Yes --> F[Calculate order value and discount]
    F --> G[Subtract dispatched quantity from stock]
    G --> H{Any returned items?}
    H -- Yes --> I[Validate return and calculate refund]
    I --> J[Update resalable stock]
    H -- No --> K[Calculate net revenue]
    J --> K
    K --> L{Ordered quantity equals dispatched quantity?}
    L -- No --> M[Report discrepancy]
    L -- Yes --> N[Record reconciled order]
    M --> O[Update financial summary]
    N --> O
    E --> P[Display final inventory and report]
    O --> P
    P --> Q([Stop])

```


## 6. Sample output

```
----- ORDER PROCESSING REPORT -----

Order ID: 101
Product: Laptop
Ordered: 2
Dispatched: 2
Returned: 1
Gross sales: ₹ 80000
Discount: ₹ 8000
Refund: ₹ 36000
Net revenue: ₹ 36000

Order ID: 102
Product: Phone
Ordered: 5
Dispatched: 4
Returned: 1
Gross sales: ₹ 60000
Discount: ₹ 6000
Refund: ₹ 13500
Net revenue: ₹ 40500

Order ID: 103
Product: Headphones
Ordered: 3
Dispatched: 3
Gross sales: ₹ 6000
Discount: ₹ 600
Refund: ₹ 0
Net revenue: ₹ 5400

----- FINAL FINANCIAL SUMMARY -----
Total refunds: ₹ 49500
Net revenue: ₹ 81900

----- DISCREPANCY REPORT -----
Order 102 - Undispatched quantity: 1

----- FINAL INVENTORY SUMMARY -----
Laptop | Price: ₹ 40000 | Remaining stock: 9
Phone | Price: ₹ 15000 | Remaining stock: 17
Headphones | Price: ₹ 2000 | Remaining stock: 27
```

## 7. Test cases

| Test case                                   | Expected result                      |
| ------------------------------------------- | ------------------------------------ |
| Order value ₹6,000                          | 10% discount applied                 |
| Ordered and dispatched quantities match     | No dispatch discrepancy              |
| Ordered quantity 5, dispatched quantity 4   | Flag 1 undispatched item             |
| Return quantity exceeds dispatched quantity | Reject transaction                   |
| Dispatch exceeds available stock            | Reject transaction                   |
| No returned products                        | Refund is ₹0                         |
| Valid return of one resalable product       | Refund calculated and stock restored |

## 8. Conclusion

This project demonstrates Python dictionaries, lists, tuples, loops, conditions, arithmetic operations, and inventory reconciliation. It combines order processing with financial calculations and stock tracking.

Important assumption: Returned products are assumed to be inspected and resalable, so they are added back to inventory. For a real system, damaged returns would need separate tracking, and financial reconciliation would also account for shipping fees, taxes, and payment-processing charges.
