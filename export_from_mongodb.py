from pymongo import MongoClient
import pandas as pd

def get_mongo_data(db_name="fraud_db", col_name="transactions_clean"):
    """
    Connects to MongoDB and fetches data directly into a pandas DataFrame.
    
    Returns:
        df: A pandas DataFrame containing the collection's data.
    """
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017")
    
    # Select database and collection
    db = client[db_name]
    collection = db[col_name]
    
    # Fetch data from MongoDB and convert cursor to list then DataFrame
    df = pd.DataFrame(list(collection.find({})))
    
    return df

# Example usage for a Notebook:
# df = get_mongo_data()
# print(df.head())
