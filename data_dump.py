import pandas as pd
import json
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load the MongoDB URL from your .env file
load_dotenv()
uri = os.getenv("MONGO_DB_URL")

# Connect to MongoDB
client = MongoClient(uri)

# Use your new database and collection names
DATABASE_NAME = "customer_categorizer"
COLLECTION_NAME = "marketing_data"

# Read your dataset (assuming it's the tab-separated marketing_campaign.csv)
# Change the filename and sep="," if you are using dataset.csv instead
df = pd.read_csv("notebooks/marketing_campaign.csv", sep="\t")

# Convert DataFrame to JSON format for MongoDB
df.reset_index(drop=True, inplace=True)
json_record = list(json.loads(df.T.to_json()).values())

# Insert the data into MongoDB
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

print(f"Successfully inserted {len(json_record)} records into MongoDB!")