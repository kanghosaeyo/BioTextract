import os
import pandas as pd

def save_to_csv(data, filename, folder="data/raw"):
    """
    Save data (list of dictionaries) to a CSV file.
    """
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, filename)
    df = pd.DataFrame(data)
    df.to_csv(filepath, index=False)
    print(f"Data saved to {filepath}")
