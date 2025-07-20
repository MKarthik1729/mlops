# create a csv file in data

import pandas as pd
import os


#create a sample data 
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["New York", "Los Angeles", "Chicago"]
}

#select a location to create a csv file

location = "data"

#create a directory if it doesn't exist
if not os.path.exists(location):
    os.makedirs(location)

file_name = "sample_data.csv"
file_path = os.path.join(location, file_name)

#create a csv file with data 
df = pd.DataFrame(data)
df.to_csv(file_path, index=False)

print(f"CSV file created successfully at {file_path}")

#read the csv file
# df = pd.read_csv(file_path)