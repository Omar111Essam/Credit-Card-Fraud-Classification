from pymongo import MongoClient
import pandas as pd

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")

# Select database and collection
db = client["fraud_db"]
collection = db["transactions_clean"]

# Fetch data from MongoDB
cursor = collection.find({})
df = pd.DataFrame(list(cursor))

# Export to CSV
df.to_csv("transactions_clean.csv", index=False)

print("Export completed successfully.")
