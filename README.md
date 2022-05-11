Analysis of Audio Features from Ukraine

Project Implementation:
    As we all know at this point Russia has invaded Ukraine. This war is highly driven by technology, something that no war in history has ever had to this scale. Large amounts of data are generated every day from the region. Thanks to Spotify we are able to get the Top 200 tracks charts for Ukraine. The basis of this project is the connection between music and the emotions they invoke and amplify. I decided to create a model for determining the emotional levels found in the top 200 Charts for the first 5 weeks of the Russian invasion. For this 4 moods would be used: Energized, Relaxed, Happy, and Sadness.

    Spotify has their own way of generating data for each song cataloged on their app. These data points are called audio features. Each of the audio features represents a different metric; a list of these audio features and their definitions can be found on the Spotify API documentation:

Energy: Represents a perceptual measure of intensity and activity
Liveness: Detects the presence of an audience in the recording
Tempo: The overall estimated tempo of a track in beats per minute (BPM)
Speechiness: Detects the presence of spoken words in a track
Acousticness: A confidence measure of whether the track is acoustic
Instrumentalness: Predicts whether a track contains no vocals
Danceability: Describes how suitable a track is for dancing
Duration: The duration of the track in milliseconds
Loudness: The overall loudness of a track in decibels (dB)
Valence: Describes the musical positiveness conveyed by a track

All these values besides Loudness are between 0-1. While Loudness is measured from -60db to 0db.
This project was undertaken in  three parts. The first being data aggregation. This was all undertaken using the Spotify api and the Spotify App. Getting chart data was simple. Download the top 200 Chart data into a CSV file. From this extract the track ids and input them into the API, then it returns a list of the audio features associated with each track. The first issue I ran into was getting accurate mood data.
    As mood is a purely human concept it is hard for machines to quantify or identify different moods. To ensure that my model would be able to classify moods; I had to check that each mood data set was differentiable from one another. The first set of moods gathered when analyzed, were too similar. For this my gathering technique may have created this issue as I was taking playlist names at face values. During my research I stumbled across an article on Medium by Mike Moschitto. Here He used Songs from Dr.AS playlists and used radar plots to check each dataset. I decided to use the playlist he mentioned and there was a significant decrease in similarities of audio features.     With this I had all the data needed to proceed, and was able to move on to step two, creating a machine learning model.  
    For the ML model the sklearn library available with python 3 was used. As the majority of the data was normalized between 0-1, I decided to skip preprocessing the data and move straight into deciding which model would be used. For this I created models of each available multi classification algorithm. The sklearn.tree sub-library had the best results as each algorithm from this section were all above the 80 percentile. Ultimately I settled on DecisionTreeClassifier as it had an accuracy score of  92%.  The next step was using the model to predict the moods of tracks for each week's chart data.
    This step is fairly easy as the data was not preprocessed when the model was trained. Thus all I had to do was input the data into the models Predict feature. This generated predicted values for each track. With these predicted values I gathered the mean values for each mood generated. As they would all be values between 0-1 these values would always add up to a total of 1 representing the total percentage of tracks that represent each emotion. I decided to chart this data vs each week. 
    
This chart was not able to show the change of each emotion in comparison to last week very well. I was hoping to show change in comparison to themselves for each week. Using the MinMaxScaler available in sklearn to normalize the data to itself I was able to get a chart that showed the total amount of change for each emotion compared for each week.
This chart Represents change each week compared to the total increase or decrease in songs labeled with each emotion. As you can see there was an increase in sad songs for each week besides from week 4 to 5. Happy almost maintained its level of play. While energetic songs decreased over time. I found a high correlation between relaxed and sad songs as most of their movements emulated each other.
Project Conclusions:
    There were many things that I was not happy with during this project. The first being the minimal amount of mood data I was able to gather. For this project I was only able to gather 246 tracks for training the model. While I am turning this in I plan on gathering more mood data to hopefully get a larger training dataset to make sure my model is able to label songs properly. Another issue, mood is a human concept and different songs may invoke different emotions depending on the cultural heritage of the person listening. The data used for moods may have been biased in this sense and thus unable to correctly determine the moods of song Ukrainianes may listen to.
    One of the main things that stumped me was the accuracy of the model. Which is Usually a good thing but can also mean that there was some data leakage occurring. The reason I was concerned by this was that the majority of mood classification models found online the average accuracy achieved was around 75-80 percent. With my model being 92% percent I wanted to make sure there was nothing wrong. I double checked the code but was unable to determine where, if any, data leakage would have occurred. I am hoping with more data I will be able to use a larger test set and get a model that may be less accurate, but is better at determining new data. 
    
References:
All my code can be found here:
https://github.com/BLoTz33/Ukrainians_Moods
I also used the Spotify package I developed found here:
https://github.com/BLoTz33/Python_Functions
Articles I used to help me with this assignment:
https://medium.com/geekculture/simple-emotion-classification-in-python-40fb24692541
https://medium.com/codex/music-mood-classification-using-neural-networks-and-spotifys-web-api-d73b391044a4
https://mikemoschitto.medium.com/deep-learning-and-music-mood-classification-of-spotify-songs-b2dda2bf455

