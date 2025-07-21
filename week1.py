
from datetime import datetime
from IPython.nbformat import v4


nb = v4.new_notebook()


intro_md = v4.new_markdown_cell("""
# Week 1 - Deforestation Detection Using Satellite Fire Data

This notebook contains the Week 1 milestone for the Deforestation Detection internship project using MODIS fire data (2021-2023).
""")


import_cell = v4.new_code_cell("""
import pandas as pd
import matplotlib.pyplot as plt
""")


load_data_cell = v4.new_code_cell("""
# Load all three datasets
df_2021 = pd.read_csv("dataset/fire_data_2021.csv")
df_2022 = pd.read_csv("dataset/fire_data_2022.csv")
df_2023 = pd.read_csv("dataset/fire_data_2023.csv")
""")


merge_clean_cell = v4.new_code_cell("""
# Merge all into one DataFrame
df = pd.concat([df_2021, df_2022, df_2023], ignore_index=True)

# Convert acquisition date to datetime
df['acq_date'] = pd.to_datetime(df['acq_date'])

# Extract year
df['year'] = df['acq_date'].dt.year
""")


trend_plot_cell = v4.new_code_cell("""
# Group by year and count detections
trend = df.groupby('year').size()

# Plot the trend
plt.figure(figsize=(8, 5))
plt.plot(trend.index, trend.values, marker='o', color='green')
plt.title("Yearly Fire Detections (Possible Deforestation Events)")
plt.xlabel("Year")
plt.ylabel("Number of Fire Detections")
plt.grid(True)
plt.tight_layout()
plt.show()
""")


summary_md = v4.new_markdown_cell("""
## Summary

In this Week 1 milestone, the dataset was loaded and merged from three years (2021–2023), and fire detection trends were visualized to observe patterns over time.

This forms the basis for deeper geographic or seasonal analysis in upcoming weeks.
""")


nb.cells = [intro_md, import_cell, load_data_cell, merge_clean_cell, trend_plot_cell, summary_md]

from nbformat import write
notebook_path = "/mnt/data/fire_trend_analysis.ipynb"
with open(notebook_path, "w", encoding="utf-8") as f:
    write(nb, f)

notebook_path
