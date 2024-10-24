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
            print(f'{i} has been removed (too many missing values)')
            temp.append(i)

        else:
            k = 0
            while k < df.shape[0]:
                if not pd.isna(df[i][k]):
                    break
                k += 1
            # Cast column data to appropriate type
            print(f"{df[i][k]} is type {type(df[i][k])}")
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


# Maakt een kolom aan voor de totale functiehersteltijd en filtert de data zodat alleen rijen overblijven met een totale functiehersteltijd van tussen de 5 minuten en 8 uur.
def filter_data(df):
    # Converteren van strings naar Timestamps.
    df['stm_fh_ddt'] = pd.to_datetime(df['stm_fh_ddt'], format="%d/%m/%Y %H:%M:%S")
    df['stm_sap_meld_ddt'] = pd.to_datetime(df['stm_sap_meld_ddt'], format="%d/%m/%Y %H:%M:%S")

    # Kolom aanmaken voor totale funciehersteltijd, dus vanaf melding tot aan functieherstel.
    df['totale_functiehersteltijd'] = df['stm_fh_ddt'] - df['stm_sap_meld_ddt']

    # Limieten voor filter
    limiet_laag = pd.Timedelta(minutes=5)
    limiet_hoog = pd.Timedelta(hours=8)

    # Filter op alleen de rijen met totale_functiehersteltijd tussen de 5 mins en 8 uur.
    filtered_df = df[(df['totale_functiehersteltijd'] >= limiet_laag) & (df['totale_functiehersteltijd'] <= limiet_hoog)]

    return filtered_df


# Function to save cleaned data
def save_data(df, output_file):
    df.to_csv(output_file, index=False)
