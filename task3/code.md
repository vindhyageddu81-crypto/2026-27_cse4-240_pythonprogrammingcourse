# Case Study 10: Campus Event Financial Planning

## 1. Problem statement

Develop a Python program to prepare a financial plan for a college event by calculating venue, equipment, catering, transport, and certificate expenses. The program should calculate total expenditure, determine the participant registration fee, calculate sponsorship shortfalls, and identify the minimum number of registrations required to break even.

## 2. Algorithm

1. Start.
2. Input the number of expected participants.
3. Input venue, equipment, catering, transport, and certificate costs.
4. Calculate total event expenditure.
5. Input the sponsorship amount and registration fee per participant.
6. Calculate the remaining amount to be funded after sponsorship.
7. Calculate the minimum number of registrations required to cover the costs.
8. Calculate the expected registration revenue.
9. Compare total revenue with total expenditure.
10. Display the financial summary and indicate whether the event makes a profit, breaks even, or incurs a loss.
11. Stop.

## 3. Formulas

- Total cost = Venue + Equipment + Catering + Transport + Certificates
- Sponsorship shortfall = Total cost − Sponsorship amount, with a minimum of ₹0
- Registration revenue = Number of registrations × Fee per participant
- Break-even registrations = Minimum whole number of participants needed to cover the remaining cost after sponsorship.

Revenue

Total cost

Loss

Profit

10203040506050010001500Quantity₹Q\*

\\(Q^\*=\frac{F}{p-v}=\frac{\text{600}}{\text{35}-\text{15}}=\text{30}\\)

Q\* is the break-even quantity where total revenue matches total cost.

\\(F\\)

₹

\\(v\\)

₹/unit

\\(p\\)

₹/unit

Give feedback

## 4. Sample budget

These are illustrative costs for a college event.

| Expense                               | Amount  |
| ------------------------------------- | ------- |
| Venue                                 | ₹10,000 |
| Equipment                             | ₹5,000  |
| Catering (₹150 × 100 participants)    | ₹15,000 |
| Transport                             | ₹4,000  |
| Certificates (₹20 × 100 participants) | ₹2,000  |
| Total expenditure                     | ₹36,000 |

Assume the event receives ₹12,000 in sponsorship and charges ₹250 per participant.

- Remaining cost after sponsorship: ₹24,000
- Minimum registrations required: 96 participants
- Expected revenue at 100 registrations: ₹12,000 + ₹25,000 = ₹37,000
- Expected surplus: ₹1,000

## 5. Flowchart
``` mermaid
flowchart TD
    A([Start]) --> B[/Input expected participants/]
    B --> C[/Input five expense amounts/]
    C --> D[Calculate total expenditure]
    D --> E[/Input sponsorship and registration fee/]
    E --> F[Calculate remaining cost]
    F --> G[Calculate break-even registrations]
    G --> H[Calculate expected revenue]
    H --> I{Revenue >= Total cost?}
    I -- Yes --> J[Calculate surplus]
    I -- No --> K[Calculate deficit]
    J --> L[/Display financial summary/]
    K --> L
    L --> M([Stop])

```



## 7. Sample output

Using the sample budget above:

```
----- Event Financial Report -----
Total expenditure: ₹ 36000
Sponsorship: ₹ 12000
Sponsorship shortfall: ₹ 24000
Break-even registrations: 96
Expected registration revenue: ₹ 25000
Total expected revenue: ₹ 37000
Expected surplus: ₹ 1000
```

## 8. Test cases

| Test case                          | Expected result             |
| ---------------------------------- | --------------------------- |
| Sponsorship covers all costs       | Break-even registrations: 0 |
| Remaining cost ₹24,000; fee ₹250   | 96 registrations            |
| Remaining cost ₹24,100; fee ₹250   | 97 registrations            |
| Revenue equals total expenditure   | Break-even                  |
| Revenue exceeds total expenditure  | Surplus                     |
| Revenue is below total expenditure | Deficit                     |
| Negative expense or sponsorship    | Invalid input               |

Important improvement: For a more realistic event budget, catering and certificates should be calculated from the actual number of registered participants, because these costs usually increase as registrations increase. The current program treats the entered expenses as fixed totals, which is suitable for a basic beginner-level case study.
