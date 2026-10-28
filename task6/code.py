
# Student Email and Identifier Validation

email = input("Enter student email: ")
reg_id = input("Enter registration ID: ")

# Email validation
email_errors = []

if " " in email:
    email_errors.append("Email must not contain spaces.")

if email.count("@") != 1:
    email_errors.append("Email must contain exactly one @ symbol.")
else:
    username, domain = email.split("@")

    if username == "":
        email_errors.append("Username is missing.")

    if domain == "":
        email_errors.append("Domain is missing.")

    if username.startswith(".") or username.endswith("."):
        email_errors.append("Username has a malformed dot.")

    if ".." in username or ".." in domain:
        email_errors.append("Consecutive dots are not allowed.")

    if domain and "." not in domain:
        email_errors.append("Domain must contain a dot.")

    if domain.startswith(".") or domain.endswith("."):
        email_errors.append("Domain has a malformed dot.")

allowed_username = (
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789._-"
)

allowed_domain = (
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789.-"
)

for ch in email:
    if ch not in allowed_username + "@":
        email_errors.append("Email contains invalid characters.")
        break

if "@" in email and email.count("@") == 1:
    for ch in domain:
        if ch not in allowed_domain:
            email_errors.append("Domain contains invalid characters.")
            break

    if "." in domain:
        parts = domain.split(".")
        if any(part == "" for part in parts):
            email_errors.append("Domain contains an empty component.")

print("\n--- Email Validation ---")

if len(email_errors) == 0:
    print("Email is valid.")
else:
    for error in email_errors:
        print(error)

# Registration ID validation
id_errors = []

if not reg_id.startswith("NRI"):
    id_errors.append("Registration ID must start with NRI.")

if len(reg_id) != 11:
    id_errors.append("Registration ID must contain 11 characters.")

if len(reg_id) >= 3:
    digits = reg_id[3:]

    if len(digits) != 8 or not digits.isdigit():
        id_errors.append("NRI must be followed by exactly 8 digits.")

print("\n--- Registration ID Validation ---")

if len(id_errors) == 0:
    print("Registration ID is valid.")
else:
    for error in id_errors:
        print(error)

