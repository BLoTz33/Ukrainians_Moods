import pandas as pd
import numpy as np
csv_dict = {
    'Happy': 'Happy.csv',
    'Sad': 'Sad.csv',
    'Relaxed': 'Relaxed.csv',
    'Energized': 'Energized.csv',
}
data_dict = {
    'Happy': [],
    'Sad': [],
    'Relaxed': [],
    'Energized': [],
}
for key, val in csv_dict.items():
    path = f'C:/Users/max/OneDrive/Desktop/Moods_Csv/{val}'
    datatest = pd.read_csv(path, index_col=[0])
    data_dict[key] = datatest.drop(
        ['mode', 'type', 'id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature'], axis=1)
    data_dict[key] = data_dict[key]
new = pd.concat(data_dict)
new.to_csv('Combined_Moods.csv')


