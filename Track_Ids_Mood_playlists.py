#import required functions
import requests
import base64
import pandas as pd
from create_datafram_tracks import Dataframe_Audio_features
client_id = 'xxxxxx'
client_secret = 'xxxxx'
auth_url = 'https://accounts.spotify.com/api/token'
base_url = 'https://api.spotify.com/v1/playlist/'

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


headers = {
    'Accept': 'application/json',
    'Content-Type':'application/json',
    'Authorization':f'Bearer {access_token}',
}

dict_of_playlist_ids = {'Happy':'5DnBWoczKx4mgk1pkSdrtu',
                        'Relaxed':'0B1cW8x7Mopg6Du5BJ4spM',
                        'Energized':'6HU206rbi8DmcaKh5LUnOe',
                        'Angry':'3aBeWOxyVcFupF8sKMm2k7',
                        'Sad':'4rFp8l9vekheKOpeJLVkar',
                        }

dict_of_track_ids = {'Happy':set(),
                        'Relaxed':set(),
                        'Energized':set(),
                        'Angry':set(),
                        'Sad':set(),
                     }



for key in dict_of_playlist_ids:
    playlist_id = dict_of_playlist_ids[key]
    request_url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
    pr = requests.get(request_url,headers=headers)
    if pr.status_code:
        playlist_data = pr.json().get('items')
        for tr in playlist_data:
            track_id = tr.get('track').get('id')
            dict_of_track_ids[key].add(track_id)

track_retrive_header = {
    'Content-Type':'application/json',
    'Authorization':f'Bearer {access_token}',
}

list_for_track_features = [[] for _ in range(5)]

j = 0
for key in dict_of_track_ids:
    Id_list = dict_of_track_ids[key]
    for i in Id_list:
        request_url = f'https://api.spotify.com/v1/audio-features/{i}'
        pr = requests.get(request_url, headers=track_retrive_header)
        if pr.status_code in range(200,299):
            track_features = pr.json()
            track_data_copy = track_features.copy()
            list_for_track_features[j].append(track_data_copy)
            print('yes', i)

        else:
            print('Audio Features failed to aquire!')
            break
    j += 1
    if pr.status_code not in range(200,299):
        print('function did not complete')
        break
#Create Names
Files_Names_csv = ['Happy.csv','Relaxed.csv','Energized.csv','Angry.csv','Sad.csv']
#formate to dataframes
data1 = Dataframe_Audio_features(list_for_track_features[0])
data2 = Dataframe_Audio_features(list_for_track_features[1])
data3 = Dataframe_Audio_features(list_for_track_features[2])
data4 = Dataframe_Audio_features(list_for_track_features[3])
data5 = Dataframe_Audio_features(list_for_track_features[4])
#covert to csv for future use
data1.to_csv(f'{Files_Names_csv[0]}')
data2.to_csv(f'{Files_Names_csv[1]}')
data3.to_csv(f'{Files_Names_csv[2]}')
data4.to_csv(f'{Files_Names_csv[3]}')
data5.to_csv(f'{Files_Names_csv[4]}')
