# Case Study: Student Email and Identifier Validation

## 1. Problem statement

Develop a Python program to validate student email addresses and registration identifiers according to predefined formatting rules. The program should identify malformed separators, invalid characters, missing components, and incorrect identifier formats, then display appropriate validation messages.

## 2. Validation rules

These are sample rules for the project.

Student email

- Must contain exactly one `@` symbol.
- Must contain a username and a domain.
- The domain must contain a dot (`.`).
- Must not contain spaces.
- The username and domain cannot start or end with a dot.

Registration identifier

- Must follow the format `NRI` followed by exactly 8 digits.
- Example valid ID: `NRI26000240`
- Must not contain spaces or special characters.

## 3. Algorithm

1. Start.
2. Input the student's email address and registration ID.
3. Check whether the email contains spaces.
4. Check whether it contains exactly one `@` symbol.
5. Validate the username and domain components.
6. Check the domain separator and identify malformed dots.
7. Validate the registration ID prefix, length, and numeric characters.
8. Display the errors found for each input.
9. Display whether each input is valid or invalid.
10. Stop.

## 4. Flowchart
``` mermaid

flowchart TD
    A([Start]) --> B[/Input email and registration ID/]
    B --> C{Email contains spaces?}
    C -- Yes --> D[Report spaces]
    C -- No --> E{Exactly one @?}
    D --> E
    E -- No --> F[Report malformed separator]
    E -- Yes --> G[Check username and domain]
    F --> H[Validate registration ID]
    G --> H
    H --> I{Prefix NRI and 8 digits?}
    I -- No --> J[Report invalid identifier]
    I -- Yes --> K[Identifier is valid]
    J --> L[/Display validation results/]
    K --> L
    L --> M([Stop])

```



## 6. Sample output

Input

```
Enter student email: student..abc@gmail.com
Enter registration ID: NRI26AB0240
```

Output

```
--- Email Validation ---
Consecutive dots are not allowed.

--- Registration ID Validation ---
NRI must be followed by exactly 8 digits.
```

## 7. Test cases

| Test input               | Expected result                    |
| ------------------------ | ---------------------------------- |
| `student@gmail.com`      | Valid email                        |
| `studentgmail.com`       | Missing or incorrect `@` separator |
| `@gmail.com`             | Missing username                   |
| `student@`               | Missing domain                     |
| `student..abc@gmail.com` | Consecutive dots                   |
| `student@gmail`          | Missing domain dot                 |
| `NRI26000240`            | Valid registration ID              |
| `NRI26AB0240`            | Invalid character group            |
| `ABC26000240`            | Invalid prefix                     |

## 8. Conclusion

This program demonstrates string manipulation, `if-else` statements, loops, `split()`, `count()`, `startswith()`, and `isdigit()` in Python. It helps detect common formatting errors in student emails and registration identifiers.

Note: These are simplified educational validation rules. A real email address may follow additional standards, and actual university registration formats may differ.
