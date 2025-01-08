import pandas as pd

class DataCleaning:
    def __init__(self):
        self.class_name = self.__class__.__name__

    # Define a reusable function to handle missing values
    def handle_missing_values(self, df: pd.DataFrame, method='mean', fill_value=None):
        """
        Handle missing values in a DataFrame
        :param fill_value: The value to fill with in the missing values
        :param method: The method to use to handle missing values
        :param df: The DataFrame to handle missing values
        Usage:
        df = pd.DataFrame(data)
        # Use the function to handle missing values by filling with the mean
        cleaned_df = handle_missing_values(df, method='mean')
        """
        tag: str = f"{self.class_name}::handle_missing_values::"
        if method not in ['drop', 'fill', 'mean', 'median', 'mode']:
            raise ValueError(f"Invalid method {method} provided")

        if method == 'drop':
            return df.dropna()
        elif method == 'fill':
            return df.fillna(fill_value)
        elif method == 'mean':
            return df.fillna(df.mean())
        elif method == 'median':
            return df.fillna(df.median())
        elif method == 'mode':
            return df.fillna(df.mode().iloc[0])
        else:
            raise ValueError(f"{tag}Invalid method provided")

    # Define a function to remove duplicates based on specific columns
    def remove_duplicates(self, df: pd.DataFrame, subset=None):
        """
        Remove duplicates from a DataFrame based on the subset of columns
        :param df: The DataFrame to remove duplicates from
        :param subset: The subset of columns to use to identify duplicates
        Usage:
        # Remove duplicates based on the 'Name' column
        In this example, we used the subset parameter to specify which columns to check for duplicates.
        This prevents accidental removal of rows where only some columns might be repeated.

        Common Mistake:
        Many beginners use the drop_duplicates() function without checking which columns contribute to duplicates,
        which can lead to the loss of important information.
        Code:
        df = pd.DataFrame(data)
        cleaned_df = remove_duplicates(df, subset=['Name'])
        print(cleaned_df)
        """
        tag: str = f"{self.class_name}::remove_duplicates::"
        return df.drop_duplicates(subset=subset)

    # Define a function to transform data types
    def transform_data_types(self, df: pd.DataFrame, col_types) -> pd.DataFrame:
        """
        Transform data types in a DataFrame
        :param df: The DataFrame to transform data types
        :param col_types: The dictionary of columns and their data types
        :return: The DataFrame with transformed data types
        Usage:
        df = pd.DataFrame(data)
        # Use the function to transform data types
        # Example dataset with incorrect data types
        data = {'Name': ['Alice', 'Bob', 'David'],
                'Age': ['25', '30', '22'],
                'Salary': ['50000', '60000', '45000']}
        df = pd.DataFrame(data)

        # Specify the correct data types
        col_types = {'Age': 'int', 'Salary': 'float'}

        # Apply the transformation
        cleaned_df = transform_data_types(df, col_types)
        print(cleaned_df.dtype)
        """
        tag: str = f"{self.class_name}::transform_data_types::"
        for col, dtype in col_types.items():
            df[col] = df[col].astype(dtype)
        return df

    # Define a function to handle outliers
    # Build a complete data cleaning pipeline
    def data_cleaning_pipeline(self,
                               df: pd.DataFrame,
                               missing_values_method='mean',
                               fill_value=None,
                               subset=None,
                               col_types=None) -> pd.DataFrame:
        # Handle missing values
        df = self.handle_missing_values(df, method=missing_values_method, fill_value=fill_value)

        # Remove duplicates
        df = self.remove_duplicates(df, subset=subset)

        # Transform data types
        if col_types:
            df = self.transform_data_types(df, col_types)

        return df
