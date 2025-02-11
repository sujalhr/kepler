import pandas as pd
import random

# Load the existing CSV file
df = pd.read_csv("places.csv")

# Add a new column 'lead_time' with random integers between 1 and 99
df["lead_time"] = [random.randint(1, 99) for _ in range(len(df))]

# Save the updated DataFrame back to the CSV file
df.to_csv("places.csv", index=False)

print("Column 'lead_time' added successfully and saved!")
