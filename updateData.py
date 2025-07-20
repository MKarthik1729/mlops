import pandas as pd
import os


# read the csv file

location = "data"
file_name = "sample_data.csv"
file_path = os.path.join(location, file_name)

df = pd.read_csv(file_path)

# add a column to the csv file
df["salary"] = [30000, 40000, 50000]

# save the csv file
df.to_csv(file_path, index=False)



# save the csv file