# University Scholarship Allocation System – Python Case Study

## 1. Problem Statement

The University Scholarship Allocation System is designed to evaluate scholarship applicants based on their academic performance, subject-wise minimum marks, attendance percentage, and family income.

The system checks whether each applicant satisfies all eligibility criteria. Eligible students are ranked according to their aggregate marks in descending order. If two students have the same aggregate marks, the system resolves ties using higher attendance, followed by lower family income. If all these values are equal, the student with the lower application ID receives the higher rank.

The program displays each applicant's eligibility status and the final ranking of eligible students.

## 2. Algorithm

1. Start the program.
2. Read the number of applicants.
3. For each applicant, input their application ID, name, aggregate marks, subject-wise marks, attendance percentage, and annual family income.
4. Check the eligibility criteria:
   - Aggregate marks must be at least 75%.
   - Every subject must have at least 60 marks out of 100.
   - Attendance must be at least 75%.
   - Annual family income must not exceed ₹2,00,000.
5. Store eligible applicants separately from ineligible applicants.
6. Sort eligible applicants using these rules:
   - Higher aggregate marks first.
   - Higher attendance first when aggregate marks are equal.
   - Lower family income first when both are equal.
   - Lower application ID first when all previous criteria are equal.
7. Assign ranks to eligible students.
8. Display the eligibility status and ranking.
9. Stop the program.

Note: The scholarship thresholds are sample values for this case study and can be changed according to university rules.

## 3. Flowchart

Mermaid
```
flowchart TD
    A([Start]) --> B[/Input number of applicants/]
    B --> C[/Input applicant details and marks/]
    C --> D{Aggregate >= 75?}
    D -- No --> I[Mark Ineligible]
    D -- Yes --> E{Every subject >= 60?}
    E -- No --> I
    E -- Yes --> F{Attendance >= 75?}
    F -- No --> I
    F -- Yes --> G{Income <= 200000?}
    G -- No --> I
    G -- Yes --> H[Mark Eligible]
    H --> J{More applicants?}
    I --> J
    J -- Yes --> C
    J -- No --> K[Collect eligible applicants]
    K --> L[Sort by aggregate descending]
    L --> M[Break ties by attendance descending]
    M --> N[Break ties by income ascending]
    N --> O[Break remaining ties by ID ascending]
    O --> P[Assign ranks and display results]
    P --> Q([Stop])
```

### 5. Sample Input

The following example contains three applicants, each with three subjects.

```
Enter number of applicants: 3

Enter details of applicant 1
Application ID: 103
Student name: Ravi
Aggregate marks (%): 82
Number of subjects: 3
Marks in subject 1: 80
Marks in subject 2: 85
Marks in subject 3: 81
Attendance (%): 90
Annual family income (Rs): 150000

Enter details of applicant 2
Application ID: 101
Student name: Priya
Aggregate marks (%): 90
Number of subjects: 3
Marks in subject 1: 95
Marks in subject 2: 88
Marks in subject 3: 87
Attendance (%): 85
Annual family income (Rs): 120000

Enter details of applicant 3
Application ID: 102
Student name: Sita
Aggregate marks (%): 78
Number of subjects: 3
Marks in subject 1: 65
Marks in subject 2: 55
Marks in subject 3: 80
Attendance (%): 92
Annual family income (Rs): 100000
```

## 6. Sample Output

```
--- Eligibility Results ---
Ravi - Eligible
Priya - Eligible
Sita - Ineligible

--- Scholarship Ranking ---
1 Priya | Aggregate: 90.0 | Attendance: 85.0 | Income: Rs 120000.0
2 Ravi | Aggregate: 82.0 | Attendance: 90.0 | Income: Rs 150000.0
```
