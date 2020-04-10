import csv 
import pandas as pd
# sudo code part 1

# extract the file 
file_csv = csv.reader(open(r'user_song_data_ver1 - yy copy.csv',encoding = 'utf-8'))
next(file_csv)

#store song rows 
above_low = []
low =[]

# for each song 
for row in file_csv:
    #user emotional state is medium and song is tense
    if row[12] == 'tense' and row[14] != 'low': 
        above_low.append(row)
    elif row[12] == 'tense' and row[14] != 'low':
        low.append(row)

#store unique user IDs
UID_med = []
UID_low = []

#store unique above med ids
for row in above_low:
    if row[0] not in UID_med:
        UID_med.append(row[0])

#store unique below med ids
for row in low:
    if row[0] not in UID_low:
        UID_low.append(row[0])

 

print("exepected output : 90% ")
print ("percentage of higher than mid tense song listeners",
        len(UID_low)/len(UID_low.size))

#part 2 

#sudo code part 2  
mental_low = []
mental_high = []

"""
for row in file_csv:
    if song == "upbeat" & user mental:       
            mental_low.append(unique user_id)
        else:
            mental_high.append(unique user id)

print (mental low / mental high x 100% ) # to show that users have good mental health 
            """