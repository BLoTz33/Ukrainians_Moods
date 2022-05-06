##import required functions and modules
import pandas as pd

from Spotify import split_Charts, Dataframe_Audio_features, Retrive_ids, SpotifyAPI

##import datasets for each week to retrive urls
dataset_week_24 = pd.read_csv(r'C:\Users\max\OneDrive\Desktop\Ukraine Spotify'
                              r'\regional-ua-weekly-2022-02-24.csv')
dataset_week_03 = pd.read_csv(r'C:\Users\max\OneDrive\Desktop\Ukraine Spotify'
                              r'\regional-ua-weekly-2022-03-03.csv')
dataset_week_10 = pd.read_csv(r'C:\Users\max\OneDrive\Desktop\Ukraine Spotify'
                              r'\regional-ua-weekly-2022-03-10.csv')
dataset_week_17 = pd.read_csv(r'C:\Users\max\OneDrive\Desktop\Ukraine Spotify'
                              r'\regional-ua-weekly-2022-03-17.csv')
dataset_week_03_24 = pd.read_csv(r'C:\Users\max\OneDrive\Desktop\Ukraine Spotify'
                                 r'\regional-ua-weekly-2022-03-24.csv')
# get Urls for each track from the weeks
Urls_week_24 = Retrive_ids(dataset_week_24, 1)
Urls_week_03 = Retrive_ids(dataset_week_03, 1)
Urls_week_10 = Retrive_ids(dataset_week_10, 1)
Urls_week_17 = Retrive_ids(dataset_week_17, 1)
Urls_week_03_24 = Retrive_ids(dataset_week_03_24, 1)
# split sets into 1 by 100 elements for spotify's api
Urls_1, Urls_2 = split_Charts(Urls_week_24)
Urls_3, Urls_4 = split_Charts(Urls_week_03)
Urls_5, Urls_6 = split_Charts(Urls_week_10)
Urls_7, Urls_8 = split_Charts(Urls_week_17)
Urls_9, Urls_10 = split_Charts(Urls_week_03_24)
# Create Dict For Urls
Urls_100s = {
    'Week_1_1': Urls_1,
    'Week_1_2': Urls_2,
    'Week_2_1': Urls_3,
    'Week_2_2': Urls_4,
    'Week_3_1': Urls_5,
    'Week_3_2': Urls_6,
    'Week_4_1': Urls_7,
    'Week_4_2': Urls_8,
    'Week_5_1': Urls_9,
    'Week_5_2': Urls_10,
}
# create dict for Audio features
List_for_track_features = [[] for _ in range(10)]
client_id = '7e203edc04004e5082fd1eb9ec9abfa2'
client_secret = 'a9f71b4ef21b4b1b9f08d918c04c0c89'
token = SpotifyAPI(client_id, client_secret)
SpotifyAPI.Get_Token(token)
SpotifyAPI.Get_audio_features(token, Urls_100s, List_for_track_features)
# create File Names
Files_Names_csv = {
    'Week_1_1.csv': [], 'Week_1_2.csv': [], 'Week_2_1.csv': [], 'Week_2_2.csv': [],
    'Week_3_1.csv': [], 'Week_3_2.csv': [], 'Week_4_1.csv': [], 'Week_4_2.csv': [],
    'Week_5_1.csv': [], 'Week_5_2.csv': [],
}
i = 0
for key in Files_Names_csv:
    Files_Names_csv[key] = Dataframe_Audio_features(List_for_track_features[i])
    i += 1
    Files_Names_csv[key].to_csv(key)
