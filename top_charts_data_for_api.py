##import required functions and modules
import pandas as pd
from Automate_Ids import Retrive_ids
from Split_Urls_100 import split_urls_for_api
import requests
import base64
import numpy as np
from create_datafram_tracks import Dataframe_Audio_features
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
#check datasets info
#print(dataset_week_24.info())
#print(dataset_week_03.info())
#print(dataset_week_10.info())
#print(dataset_week_17.info())
#print(dataset_week_03_24.info())
#get Urls for each track from the weeks
Urls_week_24 = Retrive_ids(dataset_week_24,1)
Urls_week_03 = Retrive_ids(dataset_week_03,1)
Urls_week_10 = Retrive_ids(dataset_week_10,1)
Urls_week_17 = Retrive_ids(dataset_week_17,1)
Urls_week_03_24 = Retrive_ids(dataset_week_03_24,1)
#split sets into 1 by 100 elements for spotify's api
Urls_1, Urls_2 = split_urls_for_api(Urls_week_24)
Urls_3, Urls_4 = split_urls_for_api(Urls_week_03)
Urls_5, Urls_6 = split_urls_for_api(Urls_week_10)
Urls_7, Urls_8 = split_urls_for_api(Urls_week_17)
Urls_9, Urls_10 = split_urls_for_api(Urls_week_03_24)
#Create Dict For Urls
Urls_100s = {
    'Week_1_1':Urls_1,
    'Week_1_2':Urls_2,
    'Week_2_1':Urls_3,
    'Week_2_2':Urls_4,
    'Week_3_1':Urls_5,
    'Week_3_2':Urls_6,
    'Week_4_1':Urls_7,
    'Week_4_2':Urls_8,
    'Week_5_1':Urls_9,
    'Week_5_2':Urls_10,
}
#create dict for Audio features

List_for_track_features = [[] for _ in range(10)]
print(len(List_for_track_features))



client_id = '7e203edc04004e5082fd1eb9ec9abfa2'
client_secret = 'a9f71b4ef21b4b1b9f08d918c04c0c89'
auth_url = 'https://accounts.spotify.com/api/token'

Grant_token = {'grant_type': 'client_credentials'}
client_creds = f'{client_id}:{client_secret}'
client_creds_b64 = base64.b64encode(client_creds.encode())
token_header = {
    'Authorization': f'Basic {client_creds_b64.decode()}'
}
auth_response = requests.post(auth_url,data=Grant_token,headers=token_header)

if auth_response.status_code not in range(200,299):
    print('Failed to get Token')
else:
    token_respone = auth_response.json()
    access_token = token_respone['access_token']
    print('Token Aquired')

track_retrive_header = {
    'Content-Type':'application/json',
    'Authorization':f'Bearer {access_token}',
}
id = '5jXocrsUwpKwWyI5BZLKFA'
request_url = f'https://api.spotify.com/v1/audio-features/{id}'

one = np.ones(100,int)
for_iterations = {}
for i in range(10):
    for_iterations[i] = one*i

for key1 in Urls_100s:
    id_list = Urls_100s[key1]
    j = 0
    for i in id_list:
        request_url = f'https://api.spotify.com/v1/audio-features/{i}'
        pr = requests.get(request_url, headers=track_retrive_header)
        if pr.status_code in range(200,299):
            track_features = pr.json()
            track_data_copy = track_features.copy()
            List_for_track_features[j].append(track_data_copy)
            print('yes',i)

        else:
            print('Audio Features failed to aquire!')
            break
    j += 1
    if pr.status_code not in range(200,299):
        print('function did not complete')
        break
#create File Names
Files_Names_csv = [
    'Week_1_1','Week_1_2','Week_2_1','Week_2_2',
    'Week_3_1','Week_3_2','Week_4_1','Week_4_2',
    'Week_5_1','Week_5_2',
]
#formate to dataframes
data1 = Dataframe_Audio_features(List_for_track_features[0])
data2 = Dataframe_Audio_features(List_for_track_features[1])
data3 = Dataframe_Audio_features(List_for_track_features[2])
data4 = Dataframe_Audio_features(List_for_track_features[3])
data5 = Dataframe_Audio_features(List_for_track_features[4])
data6 = Dataframe_Audio_features(List_for_track_features[5])
data7 = Dataframe_Audio_features(List_for_track_features[6])
data8 = Dataframe_Audio_features(List_for_track_features[7])
data9 = Dataframe_Audio_features(List_for_track_features[8])
data10 = Dataframe_Audio_features(List_for_track_features[9])
#covert to csv for future use
data1.to_csv(f'{Files_Names_csv[0]}')
data2.to_csv(f'{Files_Names_csv[1]}')
data3.to_csv(f'{Files_Names_csv[2]}')
data4.to_csv(f'{Files_Names_csv[3]}')
data5.to_csv(f'{Files_Names_csv[4]}')
data6.to_csv(f'{Files_Names_csv[5]}')
data7.to_csv(f'{Files_Names_csv[6]}')
data8.to_csv(f'{Files_Names_csv[7]}')
data9.to_csv(f'{Files_Names_csv[8]}')
data10.to_csv(f'{Files_Names_csv[9]}')
