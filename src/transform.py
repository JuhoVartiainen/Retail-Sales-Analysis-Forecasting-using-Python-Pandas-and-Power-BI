import pandas as pd
import numpy as np


def transform(df:pd.DataFrame):
    """
    Define column datatypes and add calculated column 'Profit margin'

    Args:
        df: Pandas dataframe containing sales data
    
    Returns:
        df: Processed dataframe
    """

    # Datetime columns
    date_cols = ["Order Date", "Ship Date"]
    for col in date_cols:
        df[col] = pd.to_datetime(df[col].str.strip(), format="%m/%d/%Y", errors="coerce")

    # Numeric columns
    num_cols = ["Sales", "Quantity", "Discount", "Profit"]
    for col in num_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Add calculated column Profit margin
    df["Profit margin"] =  np.where(df["Sales"]!=0, df["Profit"] / df["Sales"], np.nan)

    return df


if __name__ == "__main__":
    df = pd.read_csv("../data/Superstore.csv", sep=",", decimal=".", encoding="cp1252")
    df_new = transform(df)
    df_new.to_csv("../outputs/sales_processed.csv", sep=",", decimal=".", encoding="cp1252", index=False)
