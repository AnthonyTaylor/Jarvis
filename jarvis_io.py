from gtts import gTTS
import os

class jarvis_io:
    def __init__(self, listen_mode='mic'):
        self.r = sr.Recognizer()
        self.listen_mode = listen_mode
        self.nicknames = ['Ant', 'Anthony', 'User']
        self.greetings = ['']

    def listen(self):
        if self.listen_mode == 'text':
            return input('Enter statement here: ')
        elif self.listen_mode == 'mic':
            pass
        else:
            raise KeyError('listen_mode argument incorrect, supports: text, mic')
    

    def say(self, message):
        gTTS(message).save('message.mp3')
        # play audio file back (on mac)
        # -r is rate of playback 1 is defualt
        os.system(f'afplay -r 1.2 message.mp3')
    

    def greet(self):
        pass