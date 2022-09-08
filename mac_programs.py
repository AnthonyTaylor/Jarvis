import os

def calculator():
    os.system('open -a Calculator.app')

def chrome(url=None):
    if url is not None:
        os.system(f'open /Applications/Google\ Chrome.app/ \'https://{url}\'')
    else:
        os.system('open /Applications/Google\ Chrome.app')