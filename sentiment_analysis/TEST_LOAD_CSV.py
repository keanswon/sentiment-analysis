# file to test loading and reading data from csv
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    filepath = os.environ.get('filepath')
    df = pd.read_csv(filepath, header=0)

    for title in df['title']:
        print(title)

if __name__ == "__main__":
    main()