import pandas as pd

def load_data(path):
    """
    Load raw dataset
    """
    df = pd.read_csv(path, encoding='ISO-8859-1')
    return df


def clean_data(df):
    """
    Clean dataset:
    - Remove null CustomerID
    - Remove duplicates
    - Remove negative quantities
    - Convert date
    - Add Revenue column
    """

    # Drop missing CustomerID
    df = df.dropna(subset=['CustomerID'])

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove negative quantities (returns)
    df = df[df['Quantity'] > 0]

    # Convert to datetime
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    # Create Revenue column
    df['Revenue'] = df['Quantity'] * df['UnitPrice']

    return df


def save_data(df, path):
    """
    Save cleaned data
    """
    df.to_csv(path, index=False)
    