import pandas as pd

# Function to initialize or reset the CSV file
def init_csv(file_name):
    # Create an empty DataFrame and save it as a CSV with headers
    df = pd.DataFrame(columns=['x', 'y', 'z'])
    df.to_csv(file_name, index=False)

# Function to append new points to the CSV file
def update_csv(file_name, new_points):
    df = pd.DataFrame(new_points, columns=['x', 'y', 'z'])
    df.to_csv(file_name, mode='a', header=False, index=False)

# Function to read points from CSV and return as a list of tuples
def read_points(file_name):
    df = pd.read_csv(file_name)
    return list(zip(df['x'], df['y'], df['z']))