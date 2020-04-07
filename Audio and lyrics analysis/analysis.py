import csv 
import pandas as pd

file_csv = csv.reader(open(r'user_song_data_ver1 - yy copy.csv',encoding = 'utf-8'))
next(file_csv)
arousal = 0
emotion = 0
value = ""
grid = []
temp = []
final = []
for row in file_csv:
    if (float(row[5]) +float( row[6]))/2 > 0.5:
        if row[11] == 'Positive':
            emotion = 1
            grid.append(emotion)
        elif row[11] == 'Negative':
            emotion = 0
            grid.append(emotion)
        else:
            emotion = 1
            grid.append(emotion)
    elif (float(row[5]) +float( row[6]))/2 == 0.5:
        if row[11] == 'Positive':
            emotion = 1
            grid.append(emotion)
        elif row[11] == 'Negative':
            emotion = -1
            grid.append(emotion)
        else:
            emotion = 0
            grid.append(emotion)
    else:
        if row[11] == 'Positive':
            emotion = 0
            grid.append(emotion)
        elif row[11] == 'Negative':
            emotion = -1
            grid.append(emotion)
        else:
            emotion = -1
            grid.append(emotion)


    if float(row[4]) > -6:
        arousal = 1
        grid.append(arousal)
    elif float(row[4]) == -6:
        arousal = 0
        grid.append(arousal)
    else: 
        arousal = -1
        grid.append(arousal)


    if grid[0] == 1 and grid[1] == 1:
        value = "Happy"
        temp = [row[1],row[2],row[3],row[4],row[5],row[6],row[11],value]
        value = ""
    elif grid[0] == 1 and grid[1] == -1:
        value = "Relax"
        temp = [row[1],row[2],row[3],row[4],row[5],row[6],row[11],value]
        value = ""
    elif grid[0] == -1 and grid[1] == -1:
        value = "Sad"
        temp = [row[1],row[2],row[3],row[4],row[5],row[6],row[11],value]
        value = ""
    elif grid[0] == -1 and grid[1] == 1:
        value = "Tense"
        temp = [row[1],row[2],row[3],row[4],row[5],row[6],row[11],value]
        value = ""
    elif grid[0] == 1 and grid[1] == 0:
        value = "Happy"
        temp = [row[1],row[2],row[3],row[4],row[5],row[6],row[11],value]
        value = ""
    elif grid[0] == 0 and grid[1] == -1:
        value = "Sad"
        temp = [row[1],row[2],row[3],row[4],row[5],row[6],row[11],value]
        value = ""
    elif grid[0] == -1 and grid[1] == 0:
        value = "Sorrow,Disturbing"
        temp = [row[1],row[2],row[3],row[4],row[5],row[6],row[11],value]
        value = ""
    elif grid[0] == 0 and grid[1] == 1:
        value = "Exciting,Disturbing"
        temp = [row[1],row[2],row[3],row[4],row[5],row[6],row[11],value]
        value = ""
    elif grid[0] == 0 and grid[1] == 0:
        value = "Undefined"
        temp = [row[1],row[2],row[3],row[4],row[5],row[6],row[11],value]
        value = ""
    print(row[1])
    final.append(temp)
    grid = []
    temp = []

df = pd.DataFrame(final,columns = ['Song Name','Artist','Spotify Id','loundess','valence','danceability','sentiment','emotion'])
df.to_csv("spotify_Song_emotion_analysis_new.csv")