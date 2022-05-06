from Spotify import Dataframe_Audio_features, SpotifyAPI
client_id = xxxxxxxx
client_secret = xxxxxxx
initial = SpotifyAPI(Client_ID=client_id,Client_Secret=client_secret)
SpotifyAPI.Get_Token(initial)
dict_of_playlist_ids = {'Happy': '5FsxoaKvSUZyl9noSlYlwx',
                        'Relaxed': '37i9dQZF1DX36Xw4IJIVKA',
                        'Energized': '37XoFkuajvPUsLZfidsFAP',
                        'Sad': '4J6O4ytzIfPzjCIgToiEkY',
                        }

dict_of_track_ids = {'Happy': set(),
                     'Relaxed': set(),
                     'Energized': set(),
                     'Sad': set(),
                     }
SpotifyAPI.Get_track_ids(initial,dict_of_playlist_ids,dict_of_track_ids)
list_for_track_features = [[] for _ in range(5)]
SpotifyAPI.Get_audio_features(initial,dict_of_track_ids,list_for_track_features)
file_names = {
    'Happy.csv': [],
    'Relaxed.csv': [],
    'Energized.csv': [],
    'Sad.csv': [],
}
i = 0
for key in file_names:
    file_names[key] = Dataframe_Audio_features(list_for_track_features[i])
    i += 1
    file_names[key].to_csv(key)
