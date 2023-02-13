# Youtube-Transcript-Generator
- Simple scripts made using AssemblyAI API & yt-dlp.
- These scripts can be used to get the transcript and AI generated summary text files of any public YouTube video.
- To use these on your own machine or environment be sure to install the dependencies given in the requirements file.
- This project also uses ffmpeg which you'll have to install on your system.
- To use this project you'll need to provide your own AssemblyAI API key in the api_key file.
- AssemblyAI API docs: https://www.assemblyai.com/docs
- yt-dlp docs: https://github.com/yt-dlp/yt-dlp
- ffmpeg's official site: https://ffmpeg.org/


# How to use ?
- You'll need to make an account over at assemblyai's site and get yourself an api key.
- Store the api key in a file called "api_key.txt" in the project's root folder.
- Run main.py after installing relevant dependencies.
- Or you can also run the files one by one. [AudioDownloder > TranscriptGenerator > FileDeleter]
- Use python -m <file_name> to run the scripts on a terminal. 
- eg. "python -m AudioDownloder" or "python3 -m AudioDownloder".

- AudioDownloader takes the video's url and fetches the corresponding audio file.

- TranscriptGenerator uploads the audio file to AssemblyAI's servers.
- It gets the transcript & summary files.

- FileDeleter deletes the current audio, transcript & summary files.
- The working directory needs to be clear of those files for the next iteration.


####

![image](https://drive.google.com/uc?export=view&id=1PaEBO5KtX_aVjALsDA8_ATO82KLTXvYK)
