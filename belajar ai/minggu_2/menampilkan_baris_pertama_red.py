import pandas as pd
file_path = './wine+quality/winequality-red.csv'  # Ganti dengan path file Anda

df = pd.read_csv(file_path)

print(f"5 baris pertama\n{df.head()}\n")#5 baris pertama

print(f"baris pertama saja\n{df.iloc[0]}\n")#baris pertama

tipe_data = df.dtypes

print(f"\n{tipe_data}")