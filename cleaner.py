import pandas as pd

# load the data
import sys

file_name = sys.argv[1]
df = pd.read_csv(file_name)
original_rows = df.shape[0]

# clean the data
df = df.dropna()
df = df.drop_duplicates()

cleaned_rows = df.shape[0]
removed_rows = original_rows - cleaned_rows

# save cleaned data
df.to_csv("cleaned_data.csv", index=False)

# create report
with open("report.txt", "w") as f:
    f.write(f"Rows after cleaning: {df.shape[0]}\n")
    f.write(f"Columns: {df.shape[1]}\n\n")

    f.write("Column Names:\n")
    f.write(str(list(df.columns)) + "\n\n")

    f.write("Summary Statistics:\n")
    f.write(str(df.describe()) + "\n\n")

    # AI-style summary
    f.write("Summary:\n")
    f.write(f"The dataset originally contained {original_rows} rows. ")
    f.write(f"After cleaning, {cleaned_rows} rows remained. ")
    f.write(f"A total of {removed_rows} rows were removed due to missing values or duplicates.\n")

print("Cleaning done!")