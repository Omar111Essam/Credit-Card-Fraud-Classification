from pymongo import MongoClient
import pandas as pd

# =================================================================
# 🛠️ CONFIGURATION - PASTE YOUR ATLAS LINK HERE
# Replace <password> with the password for omarkhattab220_db_user
# =================================================================
ATLAS_URI = "mongodb+srv://omarkhattab220_db_user:eoQTMUOc4nx1GhdB@cluster0.m5r7r3o.mongodb.net/?appName=Cluster0"
# =================================================================

def get_mongo_data(uri=ATLAS_URI):
    try:
        # Connect to Cloud
        client = MongoClient(uri, serverSelectionTimeoutMS=5000)
        client.admin.command('ping') 
        print("✅ Cloud Connection Successful!")

        db = client["fraud_db"]
        collection = db["transactions"]
        
        # Pull data into a DataFrame
        df = pd.DataFrame(list(collection.find({})))
        
        if '_id' in df.columns:
            df = df.drop(columns=['_id'])
        return df

    except Exception as e:
        print(f"❌ Connection Failed: {e}")
        return None

if __name__ == "__main__":
    print("☁️ Fetching data from MongoDB Atlas...")
    data = get_mongo_data()
    if data is not None:
        data.to_csv("fraud_data_cloud.csv", index=False)
        print(f"✅ Success! {len(data)} rows saved to fraud_data_cloud.csv")
