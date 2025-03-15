import pandas as pd

# 1. Membaca file CSV
file_path = '../data_csv/SampleXLSFile_38kb.xls'  # Ganti dengan path file Anda
df = pd.read_excel(file_path)

name = df['Eldon Base for stackable storage shelf, platinum']
average = df[3].mean()
print(f'{name}Rata-rata nilai: {average}')
