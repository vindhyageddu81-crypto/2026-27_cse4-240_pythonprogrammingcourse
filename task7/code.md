# Case Study: Multi-Stage Scholarship Shortlisting

## 1. Problem statement

Develop a Python program to shortlist scholarship candidates by applying minimum academic marks, attendance requirements, family income limits, and merit-based ranking rules. The program should identify eligible candidates, rank them according to their academic performance, and select candidates within a fixed scholarship quota.

## 2. Sample scholarship policy

These are illustrative rules for the project, not official scholarship requirements.

| Eligibility condition         | Requirement            |
| ----------------------------- | ---------------------- |
| Minimum aggregate marks       | 75%                    |
| Minimum marks in each subject | 60%                    |
| Minimum attendance            | 75%                    |
| Maximum annual family income  | ₹1,00,000              |
| Scholarship quota             | 3 students             |
| Ranking rule                  | Higher aggregate first |

If two candidates have the same aggregate, the candidate with higher attendance ranks first.

## 3. Algorithm

1. Start.
2. Input the number of applicants and scholarship quota.
3. Enter each candidate's name, subject marks, attendance percentage, and annual family income.
4. Validate all input values.
5. Check aggregate marks against the minimum requirement.
6. Check whether every subject meets the minimum marks.
7. Check attendance and family income eligibility.
8. Add candidates who satisfy every condition to the eligible list.
9. Sort eligible candidates by aggregate marks in descending order, then attendance in descending order.
10. Select candidates up to the scholarship quota.
11. Display selected candidates, rejected candidates, and the reasons for rejection.
12. Stop.

## 4. Flowchart

``` mermaid

flowchart TD
    A([Start]) --> B[/Input applicants and quota/]
    B --> C[/Input candidate details and marks/]
    C --> D[Calculate aggregate percentage]
    D --> E{All subject marks >= 60?}
    E -- No --> R[Reject candidate]
    E -- Yes --> F{Aggregate >= 75%?}
    F -- No --> R
    F -- Yes --> G{Attendance >= 75%?}
    G -- No --> R
    G -- Yes --> H{Income <= 100000?}
    H -- No --> R
    H -- Yes --> I[Add to eligible list]
    R --> J{More applicants?}
    I --> J
    J -- Yes --> C
    J -- No --> K[Rank eligible candidates]
    K --> L[Select candidates up to quota]
    L --> M[/Display selected and rejected candidates/]
    M --> N([Stop])

```




## 6. Sample output

Suppose five applicants apply for three scholarships.

| Student | Aggregate | Attendance | Annual income | Status   |
| ------- | --------- | ---------- | ------------- | -------- |
| Anu     | 90%       | 92%        | ₹80,000       | Selected |
| Ravi    | 85%       | 88%        | ₹95,000       | Selected |
| Priya   | 80%       | 90%        | ₹70,000       | Selected |
| Kiran   | 78%       | 80%        | ₹1,50,000     | Rejected |
| Sita    | 72%       | 85%        | ₹60,000       | Rejected |

Expected selection: Anu, Ravi, and Priya, assuming their individual subject marks also meet the minimum requirement.

## 7. Test cases

| Test case                                                         | Expected result                         |
| ----------------------------------------------------------------- | --------------------------------------- |
| Aggregate 80%, all subjects ≥ 60%, attendance 80%, income ₹80,000 | Eligible                                |
| Aggregate 70%                                                     | Rejected                                |
| One subject has 55 marks                                          | Rejected                                |
| Attendance is 70%                                                 | Rejected                                |
| Family income is ₹1,20,000                                        | Rejected                                |
| Four eligible students compete for two scholarships               | Top two selected                        |
| Only one eligible student for three scholarships                  | One selected; two quota places unfilled |

## 8. Conclusion

This program demonstrates Python lists, loops, conditional statements, sorting, and list slicing. It applies multiple eligibility filters before merit ranking, ensuring that only eligible candidates compete for the limited scholarship quota.
