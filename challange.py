import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# Fungsi untuk membaca data
def read_data(file_name):
    try:
        if file_name.endswith('.csv'):
            data = pd.read_csv(file_name)
        elif file_name.endswith('.xlsx'):
            data = pd.read_excel(file_name)
        else:
            print("Format file tidak didukung. Gunakan CSV atau Excel.")
            return None
        print("Data berhasil dimuat!")
        return data
    except Exception as e:
        print(f"Gagal membaca file: {e}")
        return None

# Fungsi untuk memilih algoritma
def get_algorithm(name):
    if name.lower() == 'linear_regression':
        return LinearRegression(), 'Linear Regression'
    elif name.lower() == 'decision_tree':
        return DecisionTreeRegressor(), 'Decision Tree'
    elif name.lower() == 'random_forest':
        return RandomForestRegressor(), 'Random Forest'
    else:
        print("Algoritma tidak dikenali. Gunakan: linear_regression, decision_tree, atau random_forest.")
        return None, None

# Fungsi utama
while True:
    print("\n--- Analisis Data ---")
    file_name = input("Masukkan nama file (CSV/Excel, atau 'exit' untuk keluar): ")
    if file_name.lower() == 'exit':
        print("Keluar dari program.")
        break

    data = read_data(file_name)
    if data is None:
        continue

    print(f"Kolom yang tersedia: {list(data.columns)}")
    target = input("Masukkan nama kolom target: ")

    if target not in data.columns:
        print("Kolom target tidak ditemukan dalam data.")
        continue

    features = input("Masukkan kolom fitur (pisahkan dengan koma): ").split(',')
    features = [col.strip() for col in features if col.strip() in data.columns]

    if not features:
        print("Kolom fitur tidak valid atau tidak ditemukan.")
        continue

    X = data[features]
    y = data[target]

    # Membagi data menjadi data latih dan data uji
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    algorithm_name = input("Masukkan algoritma yang diinginkan (linear_regression, decision_tree, random_forest): ")
    model, algo_name = get_algorithm(algorithm_name)

    if model is None:
        continue

    # Melatih model pertama
    print(f"Melatih model dengan {algo_name}...")
    model.fit(X_train, y_train)
    print(f"Skor pada data uji menggunakan {algo_name}: {model.score(X_test, y_test):.4f}")

    # Analisis menggunakan algoritma tambahan
    print("\nAnalisis dengan algoritma lain:")
    for alt_algo_name in ['linear_regression', 'decision_tree', 'random_forest']:
        if alt_algo_name == algorithm_name:
            continue

        alt_model, alt_algo_label = get_algorithm(alt_algo_name)
        alt_model.fit(X_train, y_train)
        print(f"Skor pada data uji menggunakan {alt_algo_label}: {alt_model.score(X_test, y_test):.4f}")

    print("\nAnalisis selesai.")
