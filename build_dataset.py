import os

# consts
dir_path = 'raw/'
dataset_path = 'stock_dataset.csv'

# get list of csvs
csvs = []
for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        if 'csv' in path: csvs.append(path)

# build dataframe
df = []

# build labels
labels = ['Date']
for csv in csvs:
    ticker = csv.replace('.csv', '')
    labels.append(ticker)
df.append(labels)

# build dates (use whatever the first csv is)
with open(dir_path + csvs[0], 'r') as file: lines = file.readlines()
for i in range(len(lines)): lines[i] = lines[i].replace('\n', '')
for i in range(1, len(lines)):
    date = lines[i].split(',')[0]
    df.append([date]) # wrapped in brackets to be a row

# fill in stock prices
for i in range(len(csvs)):
    with open(dir_path + csvs[i], 'r') as file: lines = file.readlines()
    for i in range(len(lines)): lines[i] = lines[i].replace('\n', '')
    df_pos = 1
    for i in range(1, len(lines)):
        price = lines[i].split(',')[1]
        df[df_pos].append(price)
        df_pos += 1

# append all df rows to a dataset
for i in range(len(df)):
    line = ','.join(df[i])
    with open(dataset_path, 'a') as file: file.write(line + '\n')