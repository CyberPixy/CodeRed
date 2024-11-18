import pandas as pd


class DataSchema:
    RATE = "Rate"
    CURRENCY = "Currency"
    DATE = "Date"
    MONTH = "Month"
    YEAR = "Year"


def load_transaction_data(path: str) -> pd.DataFrame:
    # load the data from the CSV file
    data = pd.read_csv(
        path,
        dtype={
            # DataSchema.DATE: str,
            DataSchema.CURRENCY: str,
            DataSchema.RATE: float,
        },
        parse_dates=[DataSchema.DATE],
    )
     # make sure that col DATE is in format: datetime
    data[DataSchema.DATE] = pd.to_datetime(data[DataSchema.DATE], errors='coerce')
    data[DataSchema.YEAR] = data[DataSchema.DATE].dt.year.astype(str)
    data[DataSchema.MONTH] = data[DataSchema.DATE].dt.month.astype(str)
    sorted_data = data.sort_values(by='Date', ascending=False)
    
    return sorted_data