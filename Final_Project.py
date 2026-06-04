import pandas as pd

df = pd.read_csv('EEG_data.csv')

# debugging 
summary_yes_no = 0
if summary_yes_no == 1:
    print(df.shape)
    print(df.dtypes)
    print(df.head())
    print(df.describe())

# create subject dataframes
subject_df = df.groupby('subject_id')

s1 = df[df['subject_id'] == 1]