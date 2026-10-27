
# Examination Result and Grace-Mark Validation

students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

if students <= 0 or subjects <= 0:
    print("Invalid number of students or subjects.")

else:
    for i in range(students):
        print("\nStudent", i + 1)
        name = input("Enter student name: ")

        marks = []
        valid = True

        for j in range(subjects):
            mark = float(input(
                f"Enter marks for subject {j + 1}: "
            ))

            if mark < 0 or mark > 100:
                print("Invalid marks. Enter marks from 0 to 100.")
                valid = False
                break

            marks.append(mark)

        if not valid:
            print("Result cannot be processed.")
            continue

        grace = [0] * subjects
        failed = [j for j in range(subjects) if marks[j] < 40]

        # Grace is allowed in exactly one subject,
        # when the shortage is at most 5 marks.
        if len(failed) == 1:
            j = failed[0]
            shortage = 40 - marks[j]

            if shortage <= 5:
                grace[j] = shortage
                marks[j] += shortage

        total = sum(marks)
        maximum = subjects * 100
        percentage = (total / maximum) * 100

        print("\n----- Result -----")
        print("Student:", name)

        for j in range(subjects):
            print(
                f"Subject {j + 1}: "
                f"Final marks = {marks[j]}, "
                f"Grace marks = {grace[j]}"
            )

        print("Total marks:", total, "/", maximum)
        print("Percentage:", round(percentage, 2), "%")

        if any(mark < 40 for mark in marks):
            print("Result: FAIL")
        elif percentage >= 75:
            print("Result: PASS - FIRST CLASS")
        elif percentage >= 60:
            print("Result: PASS - SECOND CLASS")
        else:
            print("Result: PASS - PASS CLASS")

