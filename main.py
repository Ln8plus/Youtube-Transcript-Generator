from p1 import AudioFetcher
from p2 import FileHandler
from p3 import FileDeleter
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