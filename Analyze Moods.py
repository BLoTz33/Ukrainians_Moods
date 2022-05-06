import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from Spotify import Radar_Plot

# shoutout Mike Moschitto
# Dude got me the playlist I needed
# dataset was too similar to create a
# model that was better than a coin toss
# Also gave me the idea for the polar plots
# #MikeTheHomie check him out
# https://mikemoschitto.medium.com/deep-learning-and-music-mood-classification-of-spotify-songs-b2dda2bf455

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

names = data_dict['Happy'].columns.values
names = np.append(names, [None])
print(names)
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
for key, val in data_dict.items():
    radar, placement, labels = Radar_Plot(val)
    ax.plot(placement, radar, label=key)
    plt.thetagrids(np.degrees(placement), labels=names)
plt.legend()
plt.show()



