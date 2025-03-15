import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Data contoh
data = {'Luas': [50, 60, 70, 80, 90], 'Harga': [150000, 180000, 210000, 240000, 270000]}
df = pd.DataFrame(data)

# Memisahkan fitur dan target
X = df[['Luas']]
y = df['Harga']

# Membagi data menjadi train dan test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Membuat model regresi linear
model = LinearRegression()
model.fit(X_train, y_train)

# Melakukan prediksi
prediksi = model.predict(X_test)
print(prediksi)