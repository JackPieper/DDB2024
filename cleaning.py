import pandas as pd
import numpy as np

# Function to load data
def load_data(file_path):
    df = pd.read_csv(file_path, low_memory=False)
    return df

# Function to drop unnecessary columns
def drop_columns(df, columns_to_drop):
    df = df.drop(columns=columns_to_drop, errors='ignore')
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
            # Cast column data to appropriate type
            df[i] = df[i].astype(type(df[i][1]), errors='raise')
            
            # If column is numeric, fill NaN values with the mean
            if isinstance(df[i][1], (float, np.float64, np.int64)):
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

# Function to save cleaned data
def save_data(df, output_file):
    df.to_csv(output_file, index=False)
