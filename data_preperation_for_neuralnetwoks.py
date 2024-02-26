import pandas as pd
import os
import glob
from functions import *
import csv
import numpy as np


for i in range(49):

    folder_path = "data/e production=ep sanyo ep sanyo 0"+ str(i)
    print(folder_path) 
    csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

    dataframes = []
    dfarrnames = []

    dataframesCU = []
    dfarrnamesCU = []

    # Loop through the CSV files and load only those ending with "Format01=Kreis 5-064" and "TBA_CU"
    for csv_file in csv_files:
        if "Format01=Kreis" in csv_file:
            if "TBA_Zyk" in csv_file:
                dfarr = pd.read_csv(csv_file, skiprows=[1])
                dfarr['Zeit'] = dfarr['Zeit'].apply(convert_to_linear_time)
                dfarr['Zeit'] = dfarr['Zeit'] - dfarr['Zeit'].iloc[0]
                dfarr['Zeit'] = dfarr['Zeit'] / 3600
                dataframes.append(dfarr)
                dfarrnames.append(csv_file)
            if "TBA_CU" in csv_file:
                dfarr = pd.read_csv(csv_file, skiprows=[1])
                dfarr['Zeit'] = dfarr['Zeit'].apply(convert_to_linear_time)
                dfarr['Zeit'] = dfarr['Zeit'] - dfarr['Zeit'].iloc[0]
                dfarr['Zeit'] = dfarr['Zeit'] / 3600
                dataframesCU.append(dfarr)
                dfarrnamesCU.append(csv_file)


    valid_dataframes = []
    valid_dataframesCU = []

    for i, (df, dfCu) in enumerate(zip(dataframes, dataframesCU)):
        # Check if the 16th column is named 'Spannung' (Python uses zero-based indexing)
        if len(df.columns) > 15 and df.columns[15] == 'Spannung':
            valid_dataframes.append(df)
            valid_dataframesCU.append(dfCu)
        else:
            print('deleted:', i)

    # Update dataframes with valid dataframes
    dataframes = valid_dataframes
    dataframesCU = valid_dataframesCU


    valid_dataframes = []
    valid_dataframesCU = []

    for i, (df, dfCu) in enumerate(zip(dataframes, dataframesCU)):
        # Check if the 16th column is named 'Spannung' (Python uses zero-based indexing)
        if len(dfCu.columns) > 15 and dfCu.columns[15] == 'Spannung':
            valid_dataframes.append(df)
            valid_dataframesCU.append(dfCu)
        else:
            print('deleted:', i)

    # Update dataframes with valid dataframes
    dataframes = valid_dataframes
    dataframesCU = valid_dataframesCU

    filtered_dataframes = []

    for df in dataframesCU:
        schritt_mask = ((df['Schritt'] == 4) | (df['Schritt'] == 5)) & (df['Zeit'] >= 10)
        start_index = df[schritt_mask]
        start_time = start_index.iloc[0]['Zeit']
        end_time = start_time + 4

        time_mask = (df['Zeit'] >= start_time) & (df['Zeit'] <= end_time) & ((df['Schritt'] == 4) | (df['Schritt'] == 5))

        filtered_df = df[time_mask]
        filtered_dataframes.append(filtered_df)

    columns_to_extract = [9]

    max_values_list = []
    min_values_list = []
    capacity_values_list = []
    iteration_range = range(len(dataframes))

    for df in filtered_dataframes:
        max_values = max_threshold(columns_to_extract, df, 0, 35)
        min_values = min_threshold(columns_to_extract, df, 0, 35)
        
        max_values_list .append(max_values)
        min_values_list.append(min_values)
        capacity = max_values[0]-min_values[0]
        capacity_values_list.append(capacity)

    skip_indices = []

    extracted_capacity_values = [value for i, value in enumerate(capacity_values_list) if i not in skip_indices]

    iteration_range = range(len(extracted_capacity_values))

    with open('input(50)=3.2-3.6 ahakku , output(1)=4.2 ahakku train.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)

        I = 0
        for i, df in enumerate(dataframes):
            filtered_df = df[(df['Zyklus'] == 1)]
            quarter_len = len(filtered_df) // 4
            filtered_df = filtered_df.iloc[quarter_len:]

            filtered_df_ahakku = filtered_df[(filtered_df['Spannung'] >= 3.65) & (filtered_df['Spannung'] <= 3.85)]

            ahakku_values = filtered_df_ahakku['AhAkku'].values
            
            if len(ahakku_values) > 0:
                # Interpolate 50 values
                interpolated_values = np.interp(np.linspace(0, len(ahakku_values) - 1, 50), np.arange(len(ahakku_values)), ahakku_values)

                writer.writerow(list(interpolated_values) + [extracted_capacity_values[I]])

            I += 1