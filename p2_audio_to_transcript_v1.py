import os
import sys
import time
import json
import requests


#Step 1 : Uploading file at endpoint url and getting it's generated url.
files = next(os.walk('./'), (None, None, []))[2]
for file in files:
    if file.endswith('.mp3') or file.endswith('.m4a'):
        audio_file_name = file
print(audio_file_name)


upload_endpoint = 'https://api.assemblyai.com/v2/upload'
with open(os.path.join(sys.path[0], 'api_key.txt'), 'rt')as f:
    while True: 
        api_key = ''.join(f.readlines())
        if not f.readlines():
            break


def read_file(audio_file_name, chunk_size = 5242880):
    with open(os.path.join(sys.path[0], audio_file_name), 'rb') as f:
        while True:
            data = f.read(chunk_size)
            if not data:
                break
            yield data



headers = {'authorization':api_key, 
            'content-type':'application/json'}
response = requests.post(upload_endpoint, headers = headers, data = read_file(audio_file_name))

audio_url = response.json()['upload_url']


j = {'audio_url':audio_url, "summarization": True,
    "summary_model": "informative",
    "summary_type": "bullets_verbose"}



#Step 2 : Fetching the transcript id from the api's response.
#transcript_endpoint = 'https://api.assemblyai.com/v2/transcript'
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
response = requests.post(transcript_endpoint, headers = headers, json = j)



with open(os.path.join(sys.path[0], 'post_response.json'), 'w') as f:
    json_object = json.dumps(response.json(), indent=4)
    f.write(json_object)

transcript_id = '/' + response.json()['id']





#Step 3 Fetching our transcript as a text file:
polling_endpoint = ''.join([transcript_endpoint, transcript_id])
print(polling_endpoint)

status = ''
while status != 'completed':

    response_result = requests.get(polling_endpoint, headers = headers)
    status = response_result.json()['status']
    print(f'Status: {status}')


    if status == 'error':
        sys.exit('Audio file failed to process.')
    elif status != 'completed':
        time.sleep(60)

    if status == 'completed':
        transcript = response_result.json()['text']
        summary = response_result.json()['summary']
        
        #Saving the summary and transcript files.
        summary_name = audio_file_name[:audio_file_name.index('.')] + " Summary.txt"
        with open(os.path.join(sys.path[0], summary_name), 'w') as f:
            f.write(summary)

        transcript_name = audio_file_name[:audio_file_name.index('.')] + " Transcript.txt"    
        with open(os.path.join(sys.path[0], transcript_name), 'w') as f:
            f.write(transcript)