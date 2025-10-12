from pathlib import Path
import pandas as pd
py_root= Path(__file__).parent.parent
csv_file= py_root. joinpath('data','paralympics_raw.csv')
#print(csv_file.exists())

#from importlib import resources
#from activities import data
#csv_file=resources.files(data).joinpath("paralympics_raw.csv")
#print(csv_file.exists())

xlsx_file= py_root. joinpath('data','paralympics_all_raw.xlsx')
csv_df = pd.read_csv(csv_file)
xlsx1_df=pd.read_excel(xlsx_file, sheet_name=0)
xlsx2_df=pd.read_excel(xlsx_file, sheet_name=1)


def describe_dataframe(df):
     """Summary or description of the function
 
        Parameters:
        df (int): Description of argument1
 
        Returns:
        int: Description of the returning value
 
     """

     print(df.shape)
     print(df.head())
     print(df.tail())
     print(df.columns)
     print(df.dtypes)
     print(df.info())
     print(df.describe())


     print("\n Missing values per column:")
     print(df.isna().sum())

     missing_rows = df[df.isna().any(axis=1)]
     print("\nRows with missing values:")
     print(missing_rows)

     missing_columns = df.columns[df.isna().any(axis=0)]
     print("\nColumns with missing values:")
     print(missing_columns)

if __name__ == "__main__":
   
    # Call the function named 'describe_dataframe' - you may have a different name for your function
    describe_dataframe(csv_df)
    describe_dataframe(xlsx1_df)
    describe_dataframe(xlsx2_df)
