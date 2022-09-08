import requests
import wikipedia

def wiki(topic):
    results = wikipedia.summary(topic, sentences=2)
    return results

