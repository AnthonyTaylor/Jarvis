from jarvis_io import jarvis_io
import web_requests
import mac_programs

jarvis = jarvis_io(listen_mode='text')



# jarvis = jarvis_io(listen_mode='mic')
# jarvis.say(jarvis.listen())
# jarvis.say(web_requests.wiki('list of marvel cinematic universe movies'))
# mac_programs.calculator()
# jarvis.say('Hello World!')

# '''
while True:
    statement = jarvis.listen().lower()
    if statement.startswith('open'):
        if 'calculator' in statement:
            mac_programs.calculator()
        elif 'chrome' in statement:
            mac_programs.chrome(statement.split(' ', 1)[1].split(' ', 1)[1])
    #if you start with 'wiki' send rest of statement to wiki search
    elif statement.startswith('wiki'):
        jarvis.say(web_requests.wiki(statement.split(' ', 1)[1]))
# '''