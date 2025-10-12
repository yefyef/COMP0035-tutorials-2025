import pandas as pd
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
     print(df.info)
