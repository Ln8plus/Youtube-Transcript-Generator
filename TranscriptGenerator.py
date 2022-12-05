import os
import sys
import time
import json
import requests


#Uploading file at endpoint url and getting it's generated url.
def FileHandler():
    files = next(os.walk('./'), (None, None, []))[2]
    for file in files:
        if file.endswith('.mp3') or file.endswith('.m4a'):
            audio_file_name = file



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


    #Fetching the transcript id from the api's response.
    headers = {'authorization':api_key, 
                'content-type':'application/json'}
    response = requests.post(upload_endpoint, headers = headers, data = read_file(audio_file_name))

    audio_url = response.json()['upload_url']


    j = {'audio_url':audio_url, "summarization": True,
        "summary_model": "informative",
        "summary_type": "bullets_verbose"}


    transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
    response = requests.post(transcript_endpoint, headers = headers, json = j)

    with open(os.path.join(sys.path[0], 'post_response.json'), 'w') as f:
        json_object = json.dumps(response.json(), indent=4)
        f.write(json_object)

    transcript_id = '/' + response.json()['id']





    #Fetching our transcript as a text file:

    endpoint = ''.join([transcript_endpoint, transcript_id])


    status = ''
    while status != 'completed':

        response_result = requests.get(endpoint, headers = headers)
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
            #name = audio_file_name[:audio_file_name.index('.')]
            summary_name = "Summary.txt"
            with open(os.path.join(sys.path[0], summary_name), 'w') as f:
                f.write(summary)

            transcript_name = "Transcript.txt"    
            with open(os.path.join(sys.path[0], transcript_name), 'w') as f:
                f.write(transcript)