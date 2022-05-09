import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
#info for labels
# Energized, Happy, Relaxed, Sad
#import data sets
Week_1_1 = pd.read_csv(r'C:\Users\max\OneDrive\Desktop\Charts_Csvs\Week_1_1.csv',index_col=[0])
Week_1_2 = pd.read_csv(r'C:\Users\max\OneDrive\Desktop\Charts_Csvs\Week_1_2.csv',index_col=[0])
Week_2_1 = pd.read_csv(r'C:\Users\max\OneDrive\Desktop\Charts_Csvs\Week_2_1.csv',index_col=[0])
Week_2_2 = pd.read_csv(r'C:\Users\max\OneDrive\Desktop\Charts_Csvs\Week_2_2.csv',index_col=[0])
Week_3_1 = pd.read_csv(r'C:\Users\max\OneDrive\Desktop\Charts_Csvs\Week_3_1.csv',index_col=[0])
Week_3_2 = pd.read_csv(r'C:\Users\max\OneDrive\Desktop\Charts_Csvs\Week_3_2.csv',index_col=[0])
Week_4_1 = pd.read_csv(r'C:\Users\max\OneDrive\Desktop\Charts_Csvs\Week_4_1.csv',index_col=[0])
Week_4_2 = pd.read_csv(r'C:\Users\max\OneDrive\Desktop\Charts_Csvs\Week_4_2.csv',index_col=[0])
Week_5_1 = pd.read_csv(r'C:\Users\max\OneDrive\Desktop\Charts_Csvs\Week_5_1.csv',index_col=[0])
Week_5_2 = pd.read_csv(r'C:\Users\max\OneDrive\Desktop\Charts_Csvs\Week_5_2.csv',index_col=[0])
#combine data sets for each week
Com_Week1 = pd.concat([Week_1_1,Week_1_2])
Com_Week1 = Com_Week1.drop(['mode', 'type', 'id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature'],axis=1).values
Com_Week2 = pd.concat([Week_2_1,Week_2_2])
Com_Week2 = Com_Week2.drop(['mode', 'type', 'id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature'],axis=1).values
Com_Week3 = pd.concat([Week_3_1,Week_3_2])
Com_Week3 = Com_Week3.drop(['mode', 'type', 'id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature'],axis=1).values
Com_Week4 = pd.concat([Week_4_1,Week_4_2])
Com_Week4 = Com_Week4.drop(['mode', 'type', 'id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature'],axis=1).values
Com_Week5 = pd.concat([Week_5_1,Week_5_2])
Com_Week5 = Com_Week5.drop(['mode', 'type', 'id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature'],axis=1).values
filename = 'Finalized_Model.sav'
RanFor = pickle.load(open(filename,'rb'))
first_week = RanFor.predict(Com_Week1)
second_week = RanFor.predict(Com_Week2)
third_week = RanFor.predict(Com_Week3)
fourth_week = RanFor.predict(Com_Week4)
fifth_week = RanFor.predict(Com_Week5)
print(pd.DataFrame(first_week).describe())
print(pd.DataFrame(second_week).describe())
print(pd.DataFrame(third_week).describe())
print(pd.DataFrame(fourth_week).describe())
print(pd.DataFrame(fifth_week).describe())