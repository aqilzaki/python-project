import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# Membaca file CSV
file_path = './wine+quality/winequality-red.csv'  # Ganti dengan path file Anda
df = pd.read_csv(file_path, sep=';')

# Menghapus spasi dari nama kolom
df.columns = df.columns.str.strip()

# Menampilkan 5 baris pertama
print(df.head())

# Memeriksa nama kolom
print("Nama kolom dalam DataFrame:")
print(df.columns.tolist())

# Membuat histogram untuk kolom 'alcohol'
plt.figure(figsize=(10, 6))
sns.histplot(df['alcohol'], bins=30, kde=True)
plt.title('Distribusi Alkohol')
plt.xlabel('Kadar Alkohol')
plt.ylabel('Frekuensi')
plt.show()

# Membuat scatter plot antara 'alcohol' dan 'quality'
plt.figure(figsize=(10, 6))
sns.scatterplot(x='alcohol', y='quality', data=df)
plt.title('Hubungan antara Kadar Alkohol dan Kualitas')
plt.xlabel('Kadar Alkohol')
plt.ylabel('Kualitas')
plt.show()

# Membuat box plot untuk kolom 'quality'
plt.figure(figsize=(10, 6))
sns.boxplot(x='quality', y='alcohol', data=df)
plt.title('Box Plot Kadar Alkohol berdasarkan Kualitas')
plt.xlabel('Kualitas')
plt.ylabel('Kadar Alkohol')
plt.show()


# Membaca file CSV
file_path = './wine+quality/winequality-white.csv'  # Ganti dengan path file Anda
df = pd.read_csv(file_path, sep=';')

# Menghapus spasi dari nama kolom
df.columns = df.columns.str.strip()

# Menampilkan 5 baris pertama
print(df.head())

# Memeriksa nama kolom
print("Nama kolom dalam DataFrame:")
print(df.columns.tolist())

# Membuat histogram untuk kolom 'alcohol'
plt.figure(figsize=(10, 6))
sns.histplot(df['alcohol'], bins=30, kde=True)
plt.title('Distribusi Alkohol')
plt.xlabel('Kadar Alkohol')
plt.ylabel('Frekuensi')
plt.show()

# Membuat scatter plot antara 'alcohol' dan 'quality'
plt.figure(figsize=(10, 6))
sns.scatterplot(x='alcohol', y='quality', data=df)
plt.title('Hubungan antara Kadar Alkohol dan Kualitas')
plt.xlabel('Kadar Alkohol')
plt.ylabel('Kualitas')
plt.show()

# Membuat box plot untuk kolom 'quality'
plt.figure(figsize=(10, 6))
sns.boxplot(x='quality', y='alcohol', data=df)
plt.title('Box Plot Kadar Alkohol berdasarkan Kualitas')
plt.xlabel('Kualitas')
plt.ylabel('Kadar Alkohol')
plt.show()