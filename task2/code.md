# Case Study 3: Hospital Billing and Patient Classification

## 1. Problem statement

Develop a Python program to calculate hospital bills based on consultation fees, diagnostic charges, and treatment costs. The program should apply concessions according to predefined conditions, validate billing constraints, and classify patients based on their final payable amount and payment status.

## 2. Algorithm

1. Start.
2. Input the number of patients.
3. For each patient, enter patient ID, consultation fee, diagnostic charges, treatment charges, and payment amount.
4. Validate that all charges and payments are non-negative.
5. Calculate the total bill by adding consultation, diagnostic, and treatment charges.
6. Apply eligible concessions according to the hospital's policy.
7. Calculate the final payable amount after concessions.
8. Validate that the payment does not exceed the final bill.
9. Calculate the outstanding balance.
10. Classify the patient as Fully Paid, Partially Paid, or Unpaid.
11. Display the bill details and patient classification.
12. Repeat for all patients and stop.

## 3. Sample billing policy

These values are illustrative rules for the project, not actual hospital policies.

| Condition                                       | Policy         |
| ----------------------------------------------- | -------------- |
| Total bill ≥ ₹10,000                            | 10% concession |
| Total bill ≥ ₹5,000 but below ₹10,000           | 5% concession  |
| Total bill below ₹5,000                         | No concession  |
| Payment equals final bill                       | Fully Paid     |
| Payment is greater than ₹0 but below final bill | Partially Paid |
| Payment equals ₹0                               | Unpaid         |

## 4. Flowchart
``` mermaid

flowchart TD
    A([Start]) --> B[/Input number of patients/]
    B --> C[/Input patient details and charges/]
    C --> D{Charges and payment valid?}
    D -- No --> E[Display validation error]
    E --> C
    D -- Yes --> F[Calculate total bill]
    F --> G{Total bill >= 10000?}
    G -- Yes --> H[Apply 10% concession]
    G -- No --> I{Total bill >= 5000?}
    I -- Yes --> J[Apply 5% concession]
    I -- No --> K[No concession]
    H --> L[Calculate final bill]
    J --> L
    K --> L
    L --> M{Payment exceeds final bill?}
    M -- Yes --> N[Display payment error]
    N --> C
    M -- No --> O[Calculate outstanding balance]
    O --> P{Payment equals final bill?}
    P -- Yes --> Q[Fully Paid]
    P -- No --> R{Payment > 0?}
    R -- Yes --> S[Partially Paid]
    R -- No --> T[Unpaid]
    Q --> U[/Display bill and classification/]
    S --> U
    T --> U
    U --> V{More patients?}
    V -- Yes --> C
    V -- No --> W([Stop])

```


## 6. Sample output

Example patient record

Consultation charges

₹2,000

Diagnostic charges

₹3,000

Treatment charges

₹6,000

Total bill

₹11,000

Concession (10%)

−₹1,100

Final bill

₹9,900

Amount paid

₹5,000

Outstanding balance

₹4,900

Patient classification

Partially Paid

## 7. Test cases

| Test | Total bill               | Payment | Expected result               |
| ---- | ------------------------ | ------- | ----------------------------- |
| 1    | ₹4,000                   | ₹4,000  | No concession; Fully Paid     |
| 2    | ₹6,000                   | ₹2,000  | 5% concession; Partially Paid |
| 3    | ₹12,000                  | ₹12,000 | 10% concession; Fully Paid    |
| 4    | ₹8,000                   | ₹0      | 5% concession; Unpaid         |
| 5    | Negative charge          | —       | Invalid charges               |
| 6    | ₹6,000 before concession | ₹10,000 | Invalid payment               |

Important: This version treats classification as a payment-status category. If your assignment provides a separate patient classification policy (such as inpatient/outpatient or insurance/self-pay), those rules should be added separately.
