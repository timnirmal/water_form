import pandas as pd

# show all the columns
pd.set_option('display.max_columns', None)

URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQnxMS3my42BtJpFyxl1A0y9fYN7HiBB7tnjEOzPQ528okNH88F_Ad6KHXPdPbboV613m1A-z7DbpbO/pub?output=csv"


# URL = "https://docs.google.com/spreadsheets/d/1UoKzzRzOCt-FXLLqDKLbryEKEgllGAQUEJ5qtmmQwpU/edit#gid=0"
# csv_url = URL.replace('/edit#gid=', '/export?format=csv&gid=')

df = pd.read_csv(URL, encoding='utf-8')

# split to two dataframes by language
df_en = df[df['Choose your language'] == 'English']
df_si = df[df['Choose your language'] == 'Sinhala']

# from df_en drop all columns after 71
df_en = df_en.drop(df_en.columns[71:], axis=1)

# from df_si keep all the column after 71
df_si = df_si.drop(df_si.columns[2:71], axis=1)

# save to csv
df_en.to_csv('data_en.csv', index=False)
df_si.to_csv('data_si.csv', index=False)


# get length of the dataframes (number of columns)
if len(df_en.columns) == len(df_si.columns):
    print("Number of columns are equal")
else:
    print("Number of columns are not equal")


# now merge the two dataframes but first we need to rename the columns of the second dataframe
df_si.columns = df_en.columns

# merge the two dataframes
df = pd.concat([df_en, df_si])

# sort by timestamp
df = df.sort_values(by='Timestamp')

# save to csv
df.to_csv('data.csv', index=False)
