import pandas as pd
import matplotlib.pyplot as plt

def plot(columns_to_plot, df):
    for col_idx in columns_to_plot:
        col_name = df.columns[col_idx]
        plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
        plt.plot(df["Zeit"], df.iloc[:, col_idx])
        plt.xlabel("Time")
        plt.ylabel(col_name)
        plt.title(f"Column {col_name} Over Time")
        plt.grid(True)
        plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
        plt.xticks([])  # Hide x-axis tick labels
        plt.yticks([])  # Hide y-axis tick labels
        plt.tight_layout()
        plt.show()

def plotAll(data_frame):
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


csv_file = "data\e production=ep sanyo 002=ZYK=Massenalterung=2013-01-09 150506=TBA_Zyk=TS010620  Format01=Kreis 5-064.csv"
df = pd.read_csv(csv_file, skiprows=[1])  # Skip the second row with headers

print( df.head())

num_rows, num_columns = df.shape

print(f"Number of rows (length): {num_rows}")
print(f"Number of columns (width): {num_columns}")

columns_to_plot = [16]  # Replace with the actual column names you want to plot
plot(columns_to_plot,df)