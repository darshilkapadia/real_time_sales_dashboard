import pandas as pd
import random
import uuid
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()
Faker.seed(42)  # Ensures repeatable results

NUM_SALES = 50  # Adjust to generate more data

# --- Generate Stores ---
stores = [{"store_id": f"S{str(i).zfill(3)}", "name": fake.company(), "location": fake.city()} for i in range(1, 11)]
pd.DataFrame(stores).to_csv("stores.csv", index=False)

# --- Generate Products ---
categories = ["Electronics", "Fashion", "Grocery", "Home & Furniture"]
brands = ["Apple", "Samsung", "Nike", "Adidas", "Sony", "Dell"]
products = [
    {
        "product_id": f"P{str(i).zfill(3)}",
        "name": fake.word(),
        "category": random.choice(categories),
        "brand": random.choice(brands),
        "price": round(random.uniform(10, 2000), 2),
        "tax_rate": 7.5
    }
    for i in range(1, 21)
]
pd.DataFrame(products).to_csv("products.csv", index=False)

# --- Generate Customers ---
customers = [
    {
        "customer_id": f"C{str(i).zfill(3)}",
        "name": fake.name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "location": fake.city()
    }
    for i in range(1, 51)
]
pd.DataFrame(customers).to_csv("customers.csv", index=False)

# --- Generate Payment Methods ---
payment_methods = [
    {"payment_id": f"PM{str(i).zfill(2)}", "type": t} for i, t in enumerate(["Credit Card", "Debit Card", "Cash", "PayPal"], 1)
]
pd.DataFrame(payment_methods).to_csv("payment_methods.csv", index=False)

# --- Generate Inventory ---
inventory = [
    {
        "inventory_id": f"I{str(i).zfill(3)}",
        "store_id": random.choice([s["store_id"] for s in stores]),
        "product_id": random.choice([p["product_id"] for p in products]),
        "stock_level": random.randint(1, 500)
    }
    for i in range(1, 51)
]
pd.DataFrame(inventory).to_csv("inventory.csv", index=False)

# --- Generate Sales Data ---
sales = []
start_date = datetime.now() - timedelta(days=30)  # Last 30 days
for i in range(1, NUM_SALES + 1):
    product = random.choice(products)
    quantity = random.randint(1, 5)
    price_per_unit = product["price"]
    total_price = round(quantity * price_per_unit, 2)

    sales.append({
        "sale_id": f"SA{str(i).zfill(3)}",
        "sale_date": (start_date + timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d %H:%M:%S'),
        "store_id": random.choice([s["store_id"] for s in stores]),
        "customer_id": random.choice([c["customer_id"] for c in customers]),
        "product_id": product["product_id"],
        "quantity": quantity,
        "price_per_unit": price_per_unit,
        "total_price": total_price,
        "payment_id": random.choice([p["payment_id"] for p in payment_methods])
    })

pd.DataFrame(sales).to_csv("sales.csv", index=False)

print("✅ CSV files generated successfully: stores.csv, products.csv, customers.csv, payment_methods.csv, inventory.csv, sales.csv")