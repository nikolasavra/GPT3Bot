import openai
import numpy as np

def open_file(filepath):
    with open(filepath, 'r', encoding = 'utf-8') as infile:
        return infile.read()
        

openai.api_key = open_file('openaisecuritykey.txt')


def gpt3_embedding(content, engine = 'text-similarity-ada-001'):
    content = content.encode(encoding = 'ASCII', errors = 'ignore').decode()
    response = openai.Embedding.create(input=content, engine = engine)
    vector = respone['data'][0]['embedding'] 
    return vector
   
def similarity(v1,v2):
    return np.dot(v1,v2)
    
    
def save_debug(label, content):
    filename = '%s_%s.txt' % (time(), label)
    with open('debug/%s % filename', 'w') as outfile:
        outfile.write(content)

