import pandas as pd
import numpy as np

# Function to load data
def load_data(file_path):
    df = pd.read_csv(file_path, low_memory=False)
    return df

# Function to drop unnecessary columns
def drop_columns(df, columns_to_drop):
    df = df.drop(columns=columns_to_drop, errors='ignore')
    df.dropna(subset=['stm_progfh_in_invoer_dat'], inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

# Function to clean data (remove columns with too many NaNs and fill missing values)
def clean_data(df):
    non_nan = df.notna().sum()
    nan = df.isna().sum()
    
    temp = []  # To store columns to be removed
    avg_list = {}  # To store columns with average values
    mode_list = {}  # To store columns with mode values

    for i in df.columns:
        non_nan_count = non_nan[i]
        nan_count = nan[i]
        total = non_nan_count + nan_count
        
        # If more than 20% of data is missing, remove the column
        if non_nan_count < total * 0.8:
            temp.append(i)
        else:
            k = 0
            while k < df.shape[0]:
                if not pd.isna(df[i][k]):
                    break
                k += 1
            # Cast column data to appropriate type
            df[i] = df[i].astype(type(df[i][k]), errors='raise')

            # If column is numeric, fill NaN values with the mean
            if isinstance(df[i][k], (float, np.float64, np.int64)):
                avg = df[i].mean()
                df[i] = df[i].fillna(avg)
                avg_list[i] = avg
            else:
                # Clean string-based columns and fill NaN with mode
                df[i] = df[i].str.strip().str.lower().replace(['nan', 'none'], np.nan)
                mode = df[i].mode(dropna=True)
                if not mode.empty:
                    df[i] = df[i].fillna(mode[0])
                mode_list[i] = mode[0] if not mode.empty else np.nan

    # Drop columns with excessive missing values
    df.drop(temp, axis=1, inplace=True)
    
    return df, avg_list, mode_list

# Function to preprocess the data
def preprocess_data(df):
    # Convert `stm_geo_mld` to numeric values, filling NaNs with the column mean
    df['stm_geo_mld'] = pd.to_numeric(df['stm_geo_mld'], errors='coerce')
    df['stm_geo_mld'].fillna(df['stm_geo_mld'].mean(), inplace=True)

    # Convert `stm_sap_meldtijd` to seconds
    def time_to_seconds(t):
        if pd.notnull(t) and t != '':
            try:
                h, m, s = map(int, t.split(':'))
                return h * 3600 + m * 60 + s
            except ValueError:
                return np.nan
        return np.nan
    
    df['stm_sap_meldtijd'] = df['stm_sap_meldtijd'].apply(time_to_seconds)

    # Convert date columns to datetime and calculate total recovery time
    df['stm_fh_ddt'] = pd.to_datetime(df['stm_fh_ddt'], format="%d/%m/%Y %H:%M:%S", errors='coerce')
    df['stm_sap_meld_ddt'] = pd.to_datetime(df['stm_sap_meld_ddt'], format="%d/%m/%Y %H:%M:%S", errors='coerce')
    df['totale_functiehersteltijd'] = df['stm_fh_ddt'] - df['stm_sap_meld_ddt']

    # Filter rows with recovery time between 5 minutes and 8 hours
    limiet_laag = pd.Timedelta(minutes=5)
    limiet_hoog = pd.Timedelta(hours=8)
    df = df[(df['totale_functiehersteltijd'] >= limiet_laag) & (df['totale_functiehersteltijd'] <= limiet_hoog)]

    return df

# Function to save cleaned data
def save_data(df, output_file):
    df.to_csv(output_file, index=False)
