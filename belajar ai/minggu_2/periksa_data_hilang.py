import pandas as pd

# Membaca file CSV
file_path = './wine+quality/winequality-red.csv'  # Ganti dengan path file Anda
df = pd.read_csv(file_path)

# Memeriksa nilai yang hilang
missing_values = df.isnull().sum()
print("Jumlah nilai yang hilang di setiap kolom:")
print(missing_values)