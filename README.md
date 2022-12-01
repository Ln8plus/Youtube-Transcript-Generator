# Youtube-Transcript-Generator
- Simple scripts made using AssemblyAI API & yt-dlp.
- These scripts can be used to get the transcript and AI generated summary text files of any public YouTube video.
- To use these on your own machine or environment be sure to install the dependencies given in the requirements file.
- This project also uses ffmpeg which you'll have to install on your system.

- AssemblyAI API docs: https://www.assemblyai.com/docs
- yt-dlp docs: https://github.com/yt-dlp/yt-dlp
- ffmpeg's official site: https://ffmpeg.org/


# How to use ?
- Use python -m <file_name> to run the scripts. 
- Run them sequentially to get proper outputs. p1 > p2 > p3
- eg. "python -m p1" or "python3 -m p1".

- p1 takes the video's url and fetches the corresponding audio file.

- p2 uploads the audio file to AssemblyAI's servers.
- It gets the transcript & audio files.

- p3 deletes the current audio, transcript & summary files.
- The working directory needs to be clear of those files for the next iteration.