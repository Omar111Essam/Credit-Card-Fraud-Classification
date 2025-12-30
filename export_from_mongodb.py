from pymongo import MongoClient
import pandas as pd

def get_mongo_data(connection_string="mongodb://localhost:27017", db_name="fraud_db", col_name="transactions_clean"):
    """
    Connects to MongoDB and returns a DataFrame.
    """
    try:
        # We add a timeout so the script doesn't hang forever if the connection fails
        client = MongoClient(connection_string, serverSelectionTimeoutMS=5000)
        client.admin.command('ping') 
        
        db = client[db_name]
        collection = db[col_name]
        
        df = pd.DataFrame(list(collection.find({})))
        return df
    except Exception as e:
        print(f"❌ Connection Error: {e}")
        return None
if __name__ == "__main__":
    MY_IP = "196.153.28.56" 
    
  
    REMOTE_URI = f"mongodb://{MY_IP}:27017/"

    print(f"🔗 Connecting to database at {MY_IP}...")
    
    data = get_mongo_data(connection_string=REMOTE_URI)

    if data is not None and not data.empty:
        filename = "fraud_data_shared.csv"
        data.to_csv(filename, index=False)
        print(f"✅ Success! File saved as: {filename}")
    else:
        print("❌ Failed to fetch data. Check if the host's MongoDB is running and Firewall is open.")
