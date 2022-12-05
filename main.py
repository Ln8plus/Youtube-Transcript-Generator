from AudioDownloader import AudioFetcher
from TranscriptGenerator import FileHandler
from FileDeleter import FileDeleter
import subprocess as sb

def App():
    AudioFetcher()
    FileHandler()
    sb.run(["dir"])
    choice = input("Do you want to delete the transcribed files ? [y/N]:")
    if choice.lower() == 'y':
        FileDeleter()
        sb.run(["dir"])
App()