
# Hospital Resource Allocation and Capacity Monitoring

wards = [
    ["Emergency", 20, 20, 3, 6, 2, 4],
    ["General", 15, 30, 8, 8, 5, 5],
    ["ICU", 10, 10, 4, 6, 3, 5],
    ["Pediatrics", 10, 25, 6, 5, 4, 4]
]

# Each row:
# [Ward, Occupied Beds, Total Beds,
#  Available Staff, Required Staff,
#  Available Equipment, Required Equipment]

report = []

for ward in wards:
    name = ward[0]
    occupied = ward[1]
    total_beds = ward[2]
    staff = ward[3]
    required_staff = ward[4]
    equipment = ward[5]
    required_equipment = ward[6]

    if (occupied < 0 or total_beds <= 0
            or occupied > total_beds
            or staff < 0 or required_staff < 0
            or equipment < 0 or required_equipment < 0):
        print("Invalid resource data for", name)
        continue

    available_beds = total_beds - occupied

    bed_shortage = occupied == total_beds
    staff_shortage = staff < required_staff
    equipment_shortage = equipment < required_equipment

    shortage_count = (
        int(bed_shortage)
        + int(staff_shortage)
        + int(equipment_shortage)
    )

    if bed_shortage:
        priority = 1
    elif staff_shortage or equipment_shortage:
        priority = 2
    else:
        priority = 3

    report.append([
        priority, -shortage_count, name,
        available_beds, staff_shortage,
        equipment_shortage, shortage_count
    ])

# Sort by priority, then by number of shortages
report.sort()

print("\n----- HOSPITAL RESOURCE REPORT -----")

for item in report:
    priority, neg_count, name, beds, staff_low, equip_low, count = item

    print("\nWard:", name)
    print("Available beds:", beds)
    print("Staff shortage:", "Yes" if staff_low else "No")
    print("Equipment shortage:", "Yes" if equip_low else "No")
    print("Total shortage categories:", count)
    print("Priority:", priority)

