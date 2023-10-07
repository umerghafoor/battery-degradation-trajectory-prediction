import pandas as pd
import matplotlib.pyplot as plt

def plot(columns_to_plot):
    for col in columns_to_plot:
        plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
        plt.plot(df["Zeit"], df[col])
        plt.xlabel("Time")
        plt.ylabel(col)
        plt.title(f"{col} Over Time")
        plt.grid(True)
        plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
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

csv_file = "e production=ep sanyo 049=BOL Part 2=Massenalterung=2013-01-25 190910=TBA_BOL_P2_EIS=EIS00001  Format01=EISkanal 07-4.csv"
df = pd.read_csv(csv_file, skiprows=[1])  # Skip the second row with headers

print( df.head())

columns_to_plot = ["VRelativ","AAmplitude","RemTime"]  # Replace with the actual column names you want to plot

selected_columns = [ 1,2, 3,4, 5]  # Replace with the time column and column indices you want to plot
#plot(columns_to_plot)
plotAll(df)

