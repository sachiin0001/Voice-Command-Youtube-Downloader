from emailing.readingemail import *
from emailing.sendingemail import *

print(__name__)

from iovoice.input import voiceinput
from iovoice.output import speak

from media.accessmedia import *
from media.downloadmedia import *

from searching.google import *
from searching.wiki import *

flag = True

while True:
    if flag:
        speak("Hi. I am your voice command youtube downloader.")
        flag = False
    command = voiceinput("What would you like me to do ?")

    if 'mail' in command or 'send' in command:
        pass
    elif 'play' in command or 'song' in command or 'download':
        term = voiceinput("Tell me about the media.")
        searchandplay(term)
    elif 'search' in command or 'find' in command:
        findurls(command)
    elif 'exit' in command or 'quit' in command:
        break
    else:
        speak('Sorry I could not get that please repeat.')

if __name__ == "__main__":
    pass