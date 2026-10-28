
# Multi-Stage Scholarship Shortlisting

n = int(input("Enter number of applicants: "))
quota = int(input("Enter scholarship quota: "))

eligible = []
rejected = []

if n <= 0 or quota < 0:
    print("Invalid number of applicants or quota.")

else:
    for i in range(n):
        print("\nApplicant", i + 1)

        name = input("Enter student name: ")

        m1 = float(input("Enter marks in subject 1: "))
        m2 = float(input("Enter marks in subject 2: "))
        m3 = float(input("Enter marks in subject 3: "))

        attendance = float(
            input("Enter attendance percentage: ")
        )
        income = float(
            input("Enter annual family income: ₹")
        )

        marks = [m1, m2, m3]

        if (any(mark < 0 or mark > 100 for mark in marks)
                or attendance < 0 or attendance > 100
                or income < 0):
            print("Invalid candidate data.")
            rejected.append((name, "Invalid data"))
            continue

        aggregate = sum(marks) / len(marks)
        reasons = []

        if aggregate < 75:
            reasons.append("Aggregate below 75%")

        if any(mark < 60 for mark in marks):
            reasons.append("Subject marks below 60")

        if attendance < 75:
            reasons.append("Attendance below 75%")

        if income > 100000:
            reasons.append("Family income exceeds limit")

        if len(reasons) == 0:
            eligible.append(
                (name, aggregate, attendance, income)
            )
            print("Eligible for merit ranking.")
        else:
            rejected.append((name, ", ".join(reasons)))
            print("Not eligible:", ", ".join(reasons))

    # Rank by aggregate, then attendance
    eligible.sort(
        key=lambda student: (student[1], student[2]),
        reverse=True
    )

    selected = eligible[:quota]

    print("\n----- SCHOLARSHIP SELECTION -----")

    if len(selected) == 0:
        print("No candidates selected.")

    for rank, student in enumerate(selected, start=1):
        print(
            rank, student[0],
            "| Aggregate:", round(student[1], 2), "%",
            "| Attendance:", student[2], "%"
        )

    print("\n----- ELIGIBLE BUT NOT SELECTED -----")

    for student in eligible[quota:]:
        print(student[0], "- Quota filled")

    print("\n----- REJECTED CANDIDATES -----")

    for student in rejected:
        print(student[0], "-", student[1])

    print("\nTotal eligible:", len(eligible))
    print("Total selected:", len(selected))
    print("Unfilled quota:", max(0, quota - len(selected)))

