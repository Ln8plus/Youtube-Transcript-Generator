import os, sys
transcript = 'transcript.txt'
summary = 'summary.txt'
'''
#Checking if the files to be deleted exist in the directory.
try:    
    if not(os.path.exists(transcript)) and not(os.path.exists(summary)) :
        exit()
except OSError as e:
    print ("Error: %s - %s." % (e.filename, e.strerror))
'''


files = next(os.walk(sys.path[0]), (None, None, []))[2]
for file in files:
    if file.endswith('.mp3') or file.endswith('.m4a'):
        audio_file_name = file



#Deleting the transcript.
try:
    path = os.path.join(sys.path[0], transcript)
    os.remove(path)
except OSError as e:
    print ("Error: %s - %s." % (e.filename, e.strerror))

#Deleting the summary.
try:
    path = os.path.join(sys.path[0], summary)
    os.remove(path)
except OSError as e:
    print ("Error: %s - %s." % (e.filename, e.strerror))

#Deleting the audio file.
try:
    path = os.path.join(sys.path[0], audio_file_name)
    os.remove(path)
except OSError as e:
    print ("Error: %s - %s." % (e.filename, e.strerror))

if not(os.path.exists(audio_file_name)) and not(os.path.exists(transcript)) and not(os.path.exists(summary)):
    print('Audio, Transcript and Summary files have been deleted successfully.')