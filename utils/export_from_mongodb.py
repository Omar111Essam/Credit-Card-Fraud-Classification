from pymongo import MongoClient
import pandas as pd

# =================================================================
# 🛠️ CLOUD CONFIGURATION
# =================================================================
ATLAS_URI = "mongodb+srv://omarkhattab220_db_user:eoQTMUOc4nx1GhdB@cluster0.m5r7r3o.mongodb.net/?appName=Cluster0"
# =================================================================

def get_mongo_data(uri=ATLAS_URI):
    """
    Connects to MongoDB Atlas and returns the cleaned transactions as a DataFrame.
    """
    try:
        # 1. Establish Cloud Connection
        # We use a 5-second timeout so it doesn't hang if your internet is slow
        client = MongoClient(uri, serverSelectionTimeoutMS=5000)
        
        # 2. Verify connection
        client.admin.command('ping')
        print("✅ Connected to MongoDB Atlas successfully!")

        # 3. Access your specific database and collection
        db = client["fraud_db"]
        collection = db["transactions"]
        
        # 4. Fetch all records
        cursor = collection.find({})
        df = pd.DataFrame(list(cursor))

        if df.empty:
            print("⚠️ The database is connected, but the collection is empty.")
            return None
            
        # 5. Drop the MongoDB internal ID for a cleaner ML DataFrame
        if '_id' in df.columns:
            df = df.drop(columns=['_id'])

        return df

    except Exception as e:
        print(f"❌ Connection Failed: {e}")
        print("\n💡 Check: Did you 'Allow Access from Anywhere' in Atlas Network Access?")
        return None

if __name__ == "__main__":
    # This block allows your teammates to run the script directly from a terminal
    print("☁️ Fetching data from the cloud...")
    data = get_mongo_data()
    
    if data is not None:
        filename = "fraud_data_cloud.csv"
        data.to_csv(filename, index=False)
        print(f"✅ Success! {len(data)} records saved to {filename}")

