
# Hospital Billing and Patient Classification

n = int(input("Enter number of patients: "))

for i in range(n):
    print("\nPatient", i + 1)

    patient_id = input("Enter patient ID: ")
    consultation = float(input("Enter consultation charges: "))
    diagnostic = float(input("Enter diagnostic charges: "))
    treatment = float(input("Enter treatment charges: "))

    if consultation < 0 or diagnostic < 0 or treatment < 0:
        print("Invalid charges. Charges cannot be negative.")
        continue

    total = consultation + diagnostic + treatment

    if total >= 10000:
        concession = total * 0.10
    elif total >= 5000:
        concession = total * 0.05
    else:
        concession = 0

    final_bill = total - concession

    print("Total bill: ₹", round(total, 2))
    print("Concession: ₹", round(concession, 2))
    print("Final bill: ₹", round(final_bill, 2))

    payment = float(input("Enter amount paid: ₹"))

    if payment < 0 or payment > final_bill:
        print("Invalid payment amount.")
        continue

    balance = final_bill - payment

    if balance == 0:
        status = "Fully Paid"
    elif payment > 0:
        status = "Partially Paid"
    else:
        status = "Unpaid"

    print("Amount paid: ₹", round(payment, 2))
    print("Outstanding balance: ₹", round(balance, 2))
    print("Patient classification:", status)

