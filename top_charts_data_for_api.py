##import required functions and modules
import pandas as pd
from Automate_Ids import Retrive_ids
from Split_Urls_100 import split_urls_for_api
import numpy as np
import requests
import base64
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

List_for_track_features = [[],[],[],[],[],[],[],[],[],[]]
print(len(List_for_track_features))



client_id = 'xxxxxxxxxx'
client_secret = 'xxxxxxxxxxx'
auth_url = 'https://accounts.spotify.com/api/token'

Grant_token = {'grant_type': 'client_credentials'}
client_creds = f'{client_id}:{client_secret}'
client_creds_b64 = base64.b64encode(client_creds.encode())
token_header = {
    'Authorization': f'Basic {client_creds_b64.decode()}'
}
auth_response = requests.post(auth_url,data=Grant_token,headers=token_header)

if auth_response.status_code not in range(200,299):
    print('Failed')
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


for key in Urls_100s:
    Id_list = Urls_100s[key]
    j = 0
    for i in Id_list:
        request_url = f'https://api.spotify.com/v1/audio-features/{i}'
        pr = requests.get(request_url, headers=track_retrive_header)
        if pr.status_code in range(200,299):
            track_features = pr.json()
            track_data_copy = track_features.copy()
            List_for_track_features[j].append(track_data_copy)
        else:
            print('Failed')
    j += 1




