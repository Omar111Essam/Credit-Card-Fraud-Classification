from pymongo import MongoClient
import pandas as pd

# Use the Atlas URI here now
ATLAS_URI = "mongodb+srv://omarkhattab220_db_user:eoQTMUOc4nx1GhdB@cluster0.m5r7r3o.mongodb.net/?appName=Cluster0"

def get_mongo_data(connection_string=ATLAS_URI):
    try:
        # Note: For Atlas, we often need to install 'dnspython' (pip install dnspython)
        client = MongoClient(connection_string)
        db = client["fraud_db"]
        df = pd.DataFrame(list(db["transactions_clean"].find({})))
        return df
    except Exception as e:
        print(f"❌ Cloud Connection Error: {e}")
        return None

if __name__ == "__main__":
    print("☁️ Fetching data from MongoDB Atlas...")
    df = get_mongo_data()
    if df is not None:
        df.to_csv("transactions_fetched.csv", index=False)
        print("✅ Success! Data retrieved from the cloud.")
