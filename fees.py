import pandas as pd
df = pd.read_csv('Sample_Task2.csv')

df['change'] = df['fee'].diff()

df_filtered = df[df['change'] != 0].to_csv('change_in_fees.csv', index=False)