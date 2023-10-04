import pandas as pd

# Step 1: Read the data from plugins.csv
df = pd.read_csv('plugins_sorted.csv')

# Step 2: Convert the DataFrame to markdown format
markdown_table = df.to_markdown(index=False)

# Step 3: Write the markdown data to an MD file
with open('plugins_sorted.md', 'w') as f:
    f.write(markdown_table)

