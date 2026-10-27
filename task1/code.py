# University Scholarship Allocation System

applicants = []
n = int(input("Enter number of applicants: "))

for i in range(n):
    print("\nEnter details of applicant", i + 1)

    app_id = int(input("Application ID: "))
    name = input("Student name: ")
    aggregate = float(input("Aggregate marks (%): "))

    subjects = int(input("Number of subjects: "))
    subject_marks = []

    for j in range(subjects):
        mark = float(input(f"Marks in subject {j + 1}: "))
        subject_marks.append(mark)

    attendance = float(input("Attendance (%): "))
    income = float(input("Annual family income (Rs): "))

    # Check eligibility
    if (aggregate >= 75
            and all(mark >= 60 for mark in subject_marks)
            and attendance >= 75
            and income <= 200000):

        status = "Eligible"
    else:
        status = "Ineligible"

    applicants.append({
        "id": app_id,
        "name": name,
        "aggregate": aggregate,
        "attendance": attendance,
        "income": income,
        "status": status
    })

# Select eligible students
eligible = [
    student for student in applicants
    if student["status"] == "Eligible"
]

eligible.sort(
    key=lambda s: (
        -s["aggregate"],
        -s["attendance"],
        s["income"],
        s["id"]
    )
)


print("\n--- Eligibility Results ---")
for student in applicants:
    print(student["name"], "-", student["status"])


print("\n--- Scholarship Ranking ---")

if eligible:
    for rank, student in enumerate(eligible, start=1):
        print(
            rank, student["name"],
            "| Aggregate:", student["aggregate"],
            "| Attendance:", student["attendance"],
            "| Income: Rs", student["income"]
        )
else:
    print("No eligible applicants found.")
