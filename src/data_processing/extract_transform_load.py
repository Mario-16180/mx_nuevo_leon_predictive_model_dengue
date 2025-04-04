import polars as pl

# This module is responsible for extracting, transforming, and loading data, specially for the csv, parquet, and xlsx formats.


def extract_xlsx(file_path: str) -> pl.DataFrame:
    """
    Extract data from an Excel file and return it as a Polars DataFrame.
    """
    df = pl.read_excel(file_path)
    return df


if __name__ == "__main__":
    # Example usage
    file_path = "data\sinave 31122024.xlsx"
    df = extract_xlsx(file_path)
    print(df.head())
