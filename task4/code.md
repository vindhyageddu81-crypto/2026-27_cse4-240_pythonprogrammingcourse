# Case Study 11: Examination Result and Grace-Mark Validation

## 1. Problem statement

Develop a Python program to process student marks across multiple subjects, check subject-wise pass criteria, apply a specified grace-mark policy, and generate the final result classification. The program must validate marks, ensure grace marks do not exceed the maximum allowed, and prevent final marks from exceeding the maximum marks for any subject.

## 2. Sample examination policy

These are illustrative rules for the project, not official university regulations.

| Rule                      | Policy                                                                           |
| ------------------------- | -------------------------------------------------------------------------------- |
| Maximum marks per subject | 100                                                                              |
| Minimum pass marks        | 40                                                                               |
| Maximum grace marks       | 5 per subject                                                                    |
| Grace eligibility         | Student is short by at most 5 marks in one subject                               |
| Overall classification    | First Class: 75% or above; Second Class: 60% to below 75%; Pass Class: below 60% |
| Failure                   | Any subject remains below 40 marks after permitted grace                         |

Grace marks are awarded only when the student meets the specified eligibility conditions. A student who fails multiple subjects will not receive grace under this example policy.

## 3. Algorithm

1. Start.
2. Input the number of students and subjects.
3. For each student, input their name and subject-wise marks.
4. Validate that every mark is between 0 and 100.
5. Check how many subjects are below the pass mark of 40.
6. If exactly one subject is failed by no more than 5 marks, award the required grace marks, subject to the policy limit.
7. Ensure the revised marks do not exceed 100.
8. Check whether the student passes every subject after grace marks.
9. Calculate total marks and percentage.
10. Classify the student as Failed, Pass Class, Second Class, or First Class.
11. Display original marks, grace marks awarded, final marks, percentage, and result.
12. Repeat for all students and stop.

## 4. Flowchart
``` mermaid

flowchart TD
    A([Start]) --> B[/Input student details and subject marks/]
    B --> C{Are all marks between 0 and 100?}
    C -- No --> D[Display invalid marks]
    D --> B
    C -- Yes --> E[Count failed subjects]
    E --> F{Exactly one failed subject?}
    F -- Yes --> G{Short by at most 5 marks?}
    G -- Yes --> H[Apply required grace marks]
    G -- No --> I[Keep original marks]
    F -- No --> I
    H --> J[Validate revised marks]
    I --> K{Every subject has 40 or more?}
    J --> K
    K -- No --> L[Classify as Failed]
    K -- Yes --> M[Calculate total and percentage]
    M --> N{Percentage >= 75?}
    N -- Yes --> O[First Class]
    N -- No --> P{Percentage >= 60?}
    P -- Yes --> Q[Second Class]
    P -- No --> R[Pass Class]
    L --> S[/Display final result/]
    O --> S
    Q --> S
    R --> S
    S --> T([Stop])

```



## 6. Sample output

```
Enter number of students: 1
Enter number of subjects: 3

Student 1
Enter student name: Ravi
Enter marks for subject 1: 75
Enter marks for subject 2: 38
Enter marks for subject 3: 80

----- Result -----
Student: Ravi
Subject 1: Final marks = 75.0, Grace marks = 0
Subject 2: Final marks = 40.0, Grace marks = 2.0
Subject 3: Final marks = 80.0, Grace marks = 0
Total marks: 195.0 / 300
Percentage: 65.0 %
Result: PASS - SECOND CLASS
```

## 7. Test cases

| Test case | Input marks | Expected result                           |
| --------- | ----------- | ----------------------------------------- |
| 1         | 80, 75, 90  | First Class                               |
| 2         | 65, 62, 70  | Second Class                              |
| 3         | 45, 50, 55  | Pass Class                                |
| 4         | 75, 38, 80  | 2 grace marks; Second Class               |
| 5         | 70, 30, 80  | Failed; grace not applicable              |
| 6         | 70, 38, 35  | Failed; multiple subjects below pass mark |
| 7         | 70, 105, 80 | Invalid marks                             |

## 8. Important observations

- Grace marks are applied only to the eligible subject.
- The revised subject mark cannot exceed the maximum of 100.
- Students who still fail any subject are classified as FAIL, regardless of their overall percentage.
- The program uses a sample classification policy. Actual institutional rules may differ.
