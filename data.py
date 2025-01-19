import pandas as pd

xls = pd.ExcelFile(
    path_or_buffer="sample_superstore.xlsx",
    engine="openpyxl",
)
orders_df = pd.read_excel(
    io=xls,
    sheet_name="Orders"
)
returns_df = pd.read_excel(
    io=xls,
    sheet_name="Returns"
)

merged_df = pd.merge(
    orders_df,
    returns_df,
    on="Order ID",
    how="left"
)
merged_df.fillna("No", inplace=True)

superstore_data = merged_df
