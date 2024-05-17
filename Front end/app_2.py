import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.decomposition import FastICA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from collections import Counter
from app_3 import make_plot 


# normal: 0
# overload: 1
# underload: 2

def read_signal_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            row = line.strip().split()[:8]
            data.append(row)
    return data

def process_signal_file(file_path):
    data = read_signal_file(file_path)
    df = pd.DataFrame(data, columns=['FP1', 'FP2', 'C3', 'C4', 'P7', 'P8', 'O1', 'O2'])
    return df

def gather_data(file_path):
    df = process_signal_file(file_path)
    return df

def convert_to_csv_file(file_path):
    df = gather_data(file_path)
    df.to_csv("data_file_from_website.csv")
    return df

def pre_process_it(df):
    filtered_df_transposed = df.T
    n_components = len(filtered_df_transposed.columns)
    ica = FastICA(n_components=n_components, random_state=42)
    ica_result = ica.fit_transform(filtered_df_transposed.T)
    ica_df = pd.DataFrame(ica_result, columns=df.columns)
    normalized_df = (ica_df - ica_df.mean(axis=0)) / ica_df.std(axis=0)
    scaler = StandardScaler()
    x_test = scaler.fit_transform(normalized_df)
    pred_x = x_test.reshape(x_test.shape[0],x_test.shape[1], 1)
    return pred_x

def model_predict(file_path, model): 
    data = convert_to_csv_file(file_path)
    file_name = make_plot('FP1')
    pred_x = pre_process_it(data)
    predictions = model.predict(pred_x)
    predictions = predictions.argmax(axis=1)
    return predictions, file_name


