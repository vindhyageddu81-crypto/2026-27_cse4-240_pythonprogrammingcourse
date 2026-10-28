
# Integrated E-Commerce Order Processing and Reconciliation

inventory = {
    "Laptop": {"price": 40000, "stock": 10},
    "Phone": {"price": 15000, "stock": 20},
    "Headphones": {"price": 2000, "stock": 30}
}

# (Order ID, Product, Ordered, Dispatched, Returned)
orders = [
    (101, "Laptop", 2, 2, 1),
    (102, "Phone", 5, 4, 1),
    (103, "Headphones", 3, 3, 0)
]

total_revenue = 0
total_refunds = 0
discrepancies = []

print("----- ORDER PROCESSING REPORT -----")

for order in orders:
    order_id, product, ordered, dispatched, returned = order

    if product not in inventory:
        print("Order", order_id, ": Unknown product")
        continue

    item = inventory[product]
    price = item["price"]
    stock = item["stock"]

    if (ordered <= 0 or dispatched < 0
            or dispatched > ordered or returned < 0
            or returned > dispatched):
        print("Order", order_id, ": Invalid quantities")
        continue

    if dispatched > stock:
        print("Order", order_id, ": Insufficient stock")
        continue

    # Discount is based on the dispatched value
    gross_sales = dispatched * price

    if gross_sales >= 5000:
        discount = gross_sales * 0.10
    else:
        discount = 0

    sales_after_discount = gross_sales - discount

    # Refund uses the discounted price per item
    unit_price = sales_after_discount / dispatched if dispatched else 0
    refund = returned * unit_price

    # Update stock: dispatch decreases stock;
    # returned, resalable items are added back
    inventory[product]["stock"] -= dispatched
    inventory[product]["stock"] += returned

    net_order_revenue = sales_after_discount - refund

    total_revenue += net_order_revenue
    total_refunds += refund

    print("\nOrder ID:", order_id)
    print("Product:", product)
    print("Ordered:", ordered)
    print("Dispatched:", dispatched)
    print("Returned:", returned)
    print("Gross sales: ₹", gross_sales)
    print("Discount: ₹", round(discount, 2))
    print("Refund: ₹", round(refund, 2))
    print("Net revenue: ₹", round(net_order_revenue, 2))

    if ordered != dispatched:
        difference = ordered - dispatched
        discrepancies.append((order_id, difference))
        print("Discrepancy: Ordered and dispatched quantities differ.")
        print("Quantity difference:", difference)
    else:
        print("Dispatch status: Reconciled")

print("\n----- FINAL FINANCIAL SUMMARY -----")
print("Total refunds: ₹", round(total_refunds, 2))
print("Net revenue: ₹", round(total_revenue, 2))

print("\n----- DISCREPANCY REPORT -----")

if len(discrepancies) == 0:
    print("No discrepancies found.")
else:
    for order_id, difference in discrepancies:
        print(
            "Order", order_id,
            "- Undispatched quantity:", difference
        )

print("\n----- FINAL INVENTORY SUMMARY -----")

for product, details in inventory.items():
    print(
        product,
        "| Price: ₹", details["price"],
        "| Remaining stock:", details["stock"]
    )

