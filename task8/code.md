
# Case Study: Hospital Resource Allocation and Capacity Monitoring

## 1. Problem statement

Develop a Python program to analyze bed occupancy, available staff, and medical equipment across multiple hospital wards using nested lists. The program should identify resource shortages, assign priority levels based on predefined rules, and display wards in order of priority.

## 2. Sample resource allocation policy

| Condition                                                  | Priority   |
| ---------------------------------------------------------- | ---------- |
| Beds are fully occupied                                    | Priority 1 |
| Beds are available, but staff or equipment is insufficient | Priority 2 |
| No resource shortages                                      | Priority 3 |

If two wards have the same priority, the ward with more resource shortages is listed first.

## 3. Algorithm

1. Start.
2. Store ward names and resource details in nested lists.
3. Record occupied beds, total beds, available staff, required staff, available equipment, and required equipment.
4. Validate all resource values.
5. Calculate available beds.
6. Identify bed, staff, and equipment shortages.
7. Assign a priority level to each ward.
8. Sort wards by priority and shortage count.
9. Display resource availability and priority for each ward.
10. Stop.

## 4. Flowchart
``` mermaid

flowchart TD
    A([Start]) --> B[Store ward resource data]
    B --> C[Read each ward's resources]
    C --> D{Resource values valid?}
    D -- No --> E[Report invalid data]
    D -- Yes --> F[Calculate available beds]
    F --> G[Identify staff and equipment shortages]
    G --> H{Beds fully occupied?}
    H -- Yes --> I[Assign Priority 1]
    H -- No --> J{Staff or equipment shortage?}
    J -- Yes --> K[Assign Priority 2]
    J -- No --> L[Assign Priority 3]
    I --> M[Record ward priority and shortages]
    K --> M
    L --> M
    M --> N{More wards?}
    N -- Yes --> C
    N -- No --> O[Sort wards by priority]
    O --> P[Display resource report]
    P --> Q([Stop])

```



## 6. Sample output

```
----- HOSPITAL RESOURCE REPORT -----

Ward: Emergency
Available beds: 0
Staff shortage: Yes
Equipment shortage: Yes
Total shortage categories: 3
Priority: 1

Ward: ICU
Available beds: 0
Staff shortage: Yes
Equipment shortage: Yes
Total shortage categories: 3
Priority: 1

Ward: General
Available beds: 15
Staff shortage: No
Equipment shortage: No
Total shortage categories: 0
Priority: 3

Ward: Pediatrics
Available beds: 15
Staff shortage: No
Equipment shortage: No
Total shortage categories: 0
Priority: 3
```

## 7. Test cases

| Test case                                 | Expected result       |
| ----------------------------------------- | --------------------- |
| Occupied beds equal total beds            | Priority 1            |
| Beds available but staff insufficient     | Priority 2            |
| Beds available but equipment insufficient | Priority 2            |
| All resources meet requirements           | Priority 3            |
| Occupied beds exceed capacity             | Invalid resource data |
| Negative staff or equipment values        | Invalid resource data |

## 8. Conclusion

This program demonstrates nested lists, loops, conditional statements, sorting, and data validation in Python. It helps identify resource shortages and organize wards according to the sample priority policy.

Note: The priority rules are illustrative for an academic project. Actual hospital resource allocation must also consider clinical urgency, patient safety, and professional judgment.
