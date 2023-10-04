import pandas as pd

# Step 1: Read the data from plugin.txt
with open('plugin.txt', 'r') as f:
    lines = f.readlines()

# Step 2: Parse the data
data = []
for line in lines:
    parts = line.split(', ')
    name = parts[0].replace('Plugin Name: ', '').strip()
    link = parts[1].replace('Link: ', '').strip()
    stars = int(parts[2].replace('Stars: ', '').strip())
    data.append([name, link, stars])

# Step 3: Write the parsed data to a CSV file
df = pd.DataFrame(data, columns=['Name', 'Link', 'Stars'])
df.to_csv('plugins.csv', index=False)

# Step 4: Sort by stars and write the sorted data to another CSV file
sorted_df = df.sort_values(by='Stars', ascending=False)
sorted_df.to_csv('plugins_sorted.csv', index=False)
