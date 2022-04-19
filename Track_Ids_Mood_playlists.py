import requests
import base64

client_id = 'xxxxxxxxxxx'
client_secret = 'xxxxxxxxxxxxx'
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

list_of_playlist_ids = {'Happy':'5DnBWoczKx4mgk1pkSdrtu',
                        'Relaxed':'0B1cW8x7Mopg6Du5BJ4spM',
                        'Energized':'6HU206rbi8DmcaKh5LUnOe',
                        'Angry':'3aBeWOxyVcFupF8sKMm2k7',
                        'Sad':'4rFp8l9vekheKOpeJLVkar',
                        }

list_of_track_ids = {'Happy':set(),
                        'Relaxed':set(),
                        'Energized':set(),
                        'Angry':set(),
                        'Sad':set(),
                     }


for key in list_of_playlist_ids:
    playlist_id = list_of_playlist_ids[key]
    request_url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
    pr = requests.get(request_url,headers=headers)
    if pr.status_code:
        playlist_data = pr.json().get('items')
        for tr in playlist_data:
            track_id = tr.get('track').get('id')
            list_of_track_ids[key].add(track_id)









