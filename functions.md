## Plot Function
The code defines a function called `plot` that takes two parameters: `columns_to_plot` and `df`.
it plot all the selected columns in the data frame


```
plot(columns_to_plot, df)
```


The `plot_threshold` function is a custom function that plots the values of specified columns in a DataFrame over a specified time range.

```
plot_threshold(columns_to_plot, df, start_time, end_time)
```

```
plot_threshold_same_plot(columns_to_plot, df, start_time, end_time, existing_plt=None, y_min=None, y_max=None,i=0)
```

```
print_times_near_threshold(columns_to_plot, df, start_time, end_time, threshold=3.6, tolerance=0.01)
```

## Plot All Function
The code defines a function called `plotAll` that takes a data frame as input & Plot all the parameter along the time axis.

```
plotAll(data_frame)
```

The code defines a function called `convert_to_linear_time` that takes a string representing a date and time as input & convert it into linear Time.

```
convert_to_linear_time(date_time_str)

```

The code defines a function called `max_threshold` that takes four parameters: `columns_for_max`, `df`, `start_time`, and `end_time`.
The function `max_threshold` takes a list of column indices, a DataFrame, a start time, and an end time, and returns the maximum values for the specified columns within the specified time range.
- A list of `column` indices for which you want to find the maximum or minimun values in the dataframe
- The parameter `df` is a pandas DataFrame that contains the data you want to analyze. It is assumed that the DataFrame has a column named "Zeit" that represents the time values
- The `start time` is the lower bound of the time range you want to filter the dataframe on. It represents the earliest time you want to include in the analysis
- The `end_time` parameter is the maximum time value for which you want to filter the
    data
- `return` a list of maximum values for the specified columns in the given dataframe within the
    specified time range.

```
 max_threshold(columns, df, start_time, end_time)
 min_threshold(columns, df, start_time, end_time)
```

```
crop_values(columns, df, start_time, end_time, startvalue, endvalue)
```

## Plot All Dates
function to take an array of DataFrames and plot the specified columns from each DataFrame in a single plot


```
def plotAllDates( columns_to_plot,dataframes):
    for df in dataframes:
        for col_idx in columns_to_plot:
            col_name = df.columns[col_idx]
            plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
            plt.plot(df["Zeit"], df.iloc[:, col_idx])
            plt.xlabel("Time")
            plt.ylabel(col_name)
            plt.title(f"Column {col_name} Over Time")
            plt.grid(True)
            #plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
            plt.xticks([])  # Hide x-axis tick labels
            #plt.yticks([])  # Hide y-axis tick labels
            plt.tight_layout()
            plt.show()
```