from scipy import signal
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os 
import random

import matplotlib
matplotlib.use('Agg')

eeg_df = pd.read_csv('data_file_from_website.csv')

def make_plot(column, save_dir='static/uploads'):
    # Ensure the save directory exists
    os.makedirs(save_dir, exist_ok=True)

    # Generate a unique filename 
    random_number = random.randint(1000, 9999)
    file_name = f'plot_image_{random_number}.png'
    save_path = os.path.join(save_dir, file_name)
    
    fs = 500
    frequency_bands = {'delta': (0.5, 4),
                   'theta': (5, 8),
                   'alpha': (8, 12),
                   'beta': (12, 30),
                   'gamma': (30, 40)}

    colors = plt.cm.viridis(np.linspace(0, 1, len(frequency_bands)))

    f, Pxx = signal.welch(eeg_df[column], fs, nperseg=1024)  # Adjust nperseg as needed

    # Plot the PSD with different line styles/colors for each band
    for i, (band, (low, high)) in enumerate(frequency_bands.items()):
        indices = np.where((f >= low) & (f <= high))
        plt.semilogy(f[indices], Pxx[indices], label=f'{band}', color=colors[i])

    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power/Frequency (dB/Hz)')
    plt.title('Power Spectral Density of EEG Signals for FP1')
    
    plt.legend()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.clf()
    return file_name