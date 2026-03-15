import pandas as pd

def load_csv(file_path):
    df = pd.read_csv(file_path)
    return df 

def generate_summary(df):
    print("\nDataset Info")
    print("--------------")
    print(df.info())

    print ("Basic statistics")
    print("-----------------------")
    print(df.describe())

    print("\n columns means")
    print("------------------")
    print(df.mean(numeric_only = True))

    print("\nMissing values")
    print("----------------")
    print(df.isnull().sum())

def main():
    file_path = "D:\Passion\csv-summary-project\data\ganesh\sample.csv"
    df = load_csv(file_path)
    generate_summary(df)

if __name__ =="__main__":
    main()