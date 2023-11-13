import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

def plot(columns_to_plot, df):
    """
    The function `plot` takes a list of column indices and a DataFrame as input, and plots the specified
    columns over time.
    
    :param columns_to_plot: The `columns_to_plot` parameter is a list of column indices that you want to
    plot from the DataFrame `df`. Each element in the list represents the index of the column you want
    to plot
    :param df: The parameter `df` is a pandas DataFrame that contains the data you want to plot. It
    should have a column named "Zeit" that represents the time values, and other columns that you want
    to plot
    """
    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed

    for col_idx in columns_to_plot:
        col_name = df.columns[col_idx]
        plt.plot(df["Zeit"], df.iloc[:, col_idx], label=f"Column {col_name}")

    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.title("Columns Over Time")
    plt.grid(True)
    plt.legend()
    plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
    #plt.xticks([])  # Hide x-axis tick labels
    #plt.yticks([])  # Hide y-axis tick labels
    plt.tight_layout()
    plt.show()

def plot_threshold(columns_to_plot, df, start_time, end_time):
    """
    The function `plot_threshold` plots specified columns of a DataFrame within a specified time range.
    
    :param columns_to_plot: The `columns_to_plot` parameter is a list of column indices that you want to
    plot from the DataFrame `df`. Each index corresponds to a specific column in the DataFrame
    :param df: The dataframe containing the data to plot
    :param start_time: The start time is the beginning of the time range you want to plot. It should be
    in the same format as the "Zeit" column in your dataframe
    :param end_time: The `end_time` parameter specifies the end time of the time range for which you
    want to plot the data
    """
    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed

    # Filter data within the specified time range
    mask = (df["Zeit"] >= start_time) & (df["Zeit"] <= end_time)
    df_filtered = df[mask]

    for col_idx in columns_to_plot:
        col_name = df.columns[col_idx]
        plt.plot(df_filtered["Zeit"], df_filtered.iloc[:, col_idx], label=f"Column {col_name}")

    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.title("Columns Over Time")
    plt.grid(True)
    plt.legend()
    plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
    #plt.xticks([])  # Hide x-axis tick labels
    #plt.yticks([])  # Hide y-axis tick labels
    plt.tight_layout()
    plt.show()

def plot_threshold_same_plot(columns_to_plot, df, start_time, end_time, existing_plt=None, y_min=None, y_max=None,i=0):
    """
    The function `plot_threshold` plots specified columns of a DataFrame within a specified time range.

    :param columns_to_plot: The `columns_to_plot` parameter is a list of column indices that you want to
    plot from the DataFrame `df`. Each index corresponds to a specific column in the DataFrame.
    :param df: The dataframe containing the data to plot.
    :param start_time: The start time is the beginning of the time range you want to plot. It should be
    in the same format as the "Zeit" column in your dataframe.
    :param end_time: The `end_time` parameter specifies the end time of the time range for which you
    want to plot the data.
    :param existing_plt: (Optional) The existing Matplotlib plt object where you want to plot the data.
    If None, a new figure and axes will be created.
    :param y_min: (Optional) The minimum value for the y-axis.
    :param y_max: (Optional) The maximum value for the y-axis.
    """
    if existing_plt is None:
        plt.figure(figsize=(10, 6))  # Adjust the figure size as needed

    colors = [
    (0.8, 0.8, 1.0),
    (0.76, 0.76, 0.95),
    (0.72, 0.72, 0.9),
    (0.68, 0.68, 0.85),
    (0.64, 0.64, 0.8),
    (0.6, 0.6, 0.75),
    (0.56, 0.56, 0.7),
    (0.52, 0.52, 0.65),
    (0.48, 0.48, 0.6),
    (0.44, 0.44, 0.55),
    (0.4, 0.4, 0.5),
    (0.36, 0.36, 0.45),
    (0.32, 0.32, 0.4),
    (0.28, 0.28, 0.35),
    (0.24, 0.24, 0.3),
    (0.2, 0.2, 0.25),
    (0.16, 0.16, 0.2),
    (0.12, 0.12, 0.15),
    (0.08, 0.08, 0.1),
    (0.04, 0.04, 0.05)
    ]

    # Filter data within the specified time range
    mask = (df["Zeit"] >= start_time) & (df["Zeit"] <= end_time)
    df_filtered = df[mask]
    df_filtered.loc[:, "Zeit"] -= start_time

    for idx, col_idx in enumerate(columns_to_plot):
        col_name = df.columns[col_idx]
        line_color = colors[i%20]  # Cycle through 15 different shades of blue
        if existing_plt is not None:
            existing_plt.plot(df_filtered["Zeit"], df_filtered.iloc[:, col_idx], label=f"Column {col_name}", color=line_color)
        else:
            plt.plot(df_filtered["Zeit"], df_filtered.iloc[:, col_idx], label=f"Column {col_name}", color=line_color)

    if y_min is not None and y_max is not None:
        if existing_plt is not None:
            existing_plt.ylim(y_min, y_max)
        else:
            plt.ylim(y_min, y_max)

    if existing_plt is None:
        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.title("Columns Over Time")
        plt.grid(True)
        plt.legend()
        plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
        plt.tight_layout()

def print_times_near_threshold(columns_to_plot, df, start_time, end_time, threshold=3.6, tolerance=0.01):
    """
    The function `print_times_near_threshold` prints the times when the value of the y-axis is within a tolerance
    range of the specified threshold.

    :param columns_to_plot: The `columns_to_plot` parameter is a list of column indices that you want to
    print times for from the DataFrame `df`. Each index corresponds to a specific column in the DataFrame.
    :param df: The dataframe containing the data to check for values near the threshold.
    :param start_time: The start time is the beginning of the time range you want to check. It should be
    in the same format as the "Zeit" column in your dataframe.
    :param end_time: The `end_time` parameter specifies the end time of the time range for which you
    want to check the data.
    :param threshold: The threshold value to compare against on the y-axis.
    :param tolerance: The tolerance range within which values are considered "near" the threshold.
    """
    mask = (df["Zeit"] >= start_time) & (df["Zeit"] <= end_time)
    df_filtered = df[mask]

    for col_idx in columns_to_plot:
        col_name = df.columns[col_idx]
        in_tolerance_range = False  # Flag to track if we're in the tolerance range

        # Iterate through the rows to find times when the value is within the tolerance range
        for index, row in df_filtered.iterrows():
            value = row.iloc[col_idx]
            if abs(value - threshold) <= tolerance:
                if not in_tolerance_range:
                    print(f"{col_name} , {threshold} t = {row['Zeit']}")
                    in_tolerance_range = True
            else:
                in_tolerance_range = False

def plotAll(data_frame):
    """
    The function `plotAll` takes a data frame as input and plots each column against time in a grid
    layout.
    
    :param data_frame: The parameter `data_frame` is expected to be a pandas DataFrame object. It should
    contain the data that you want to plot. Each column of the DataFrame represents a different variable
    or feature that you want to plot over time. The DataFrame should have a column named "Zeit" which
    represents the time
    """
    num_columns = len(data_frame.columns)
    num_rows = (num_columns + 2) // 3  # Create a grid with 3 columns

    plt.figure(figsize=(15, 5 * num_rows))  # Adjust the figure size as needed

    for i, col in enumerate(data_frame.columns):
        plt.subplot(num_rows, 3, i + 1)  # Create a subplot
        plt.plot(data_frame["Zeit"], data_frame[col])
        plt.xlabel("Time")  # Set x-axis label to empty string to hide it
        plt.ylabel(col)
        plt.title(f"{col} Over Time")
        plt.grid(True)
        plt.xticks([])  # Hide x-axis tick labels
        plt.yticks([])  # Hide y-axis tick labels

    plt.tight_layout()
    plt.show()

def convert_to_linear_time(date_time_str):
    input_format = "%Y-%m-%d %H:%M:%S.%f"
    dt_object = datetime.strptime(date_time_str, input_format)
    linear_time = dt_object.timestamp()
    
    return linear_time

def max_threshold(columns, df, start_time, end_time):
    mask = (df["Zeit"] >= start_time) & (df["Zeit"] <= end_time)
    df_filtered = df[mask]

    max_values = []

    for col_idx in columns:
        col_name = df.columns[col_idx]
        max_value = df_filtered[col_name].max()
        max_values.append(max_value)

    return max_values

def min_threshold(columns, df, start_time, end_time):
    mask = (df["Zeit"] >= start_time) & (df["Zeit"] <= end_time)
    df_filtered = df[mask]

    min_values = []

    for col_idx in columns:
        col_name = df.columns[col_idx]
        min_value = df_filtered[col_name].min()
        min_values.append(min_value)

    return min_values

def crop_values(columns, df, start_time, end_time, startvalue, endvalue):
    # Create a mask for the specified time range
    time_mask = (df["Zeit"] >= start_time) & (df["Zeit"] <= end_time)

    # Apply the time mask to the DataFrame
    df_filtered = df[time_mask]

    # Iterate over the specified columns and crop values
    for col_idx in columns:
        col_name = df.columns[col_idx]

        # Crop values within the specified range
        df_filtered.loc[df_filtered[col_name] < startvalue, col_name] = startvalue
        df_filtered.loc[df_filtered[col_name] > endvalue, col_name] = endvalue

    return df_filtered