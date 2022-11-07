import openai

def open_file(filepath):
    with open(filepath, 'r', encoding = 'utf-8') as infile:
        return infile.read()
        

openai.api_key = open_file('openaisecuritykey.txt')

def gpt3_completion(prompt, engine='text-davinci-002', temp=0.7, top_p=1.0, tokens=400, freq_pen=0.0, pres_pen=0.0, stop=['<<END>>']):
    prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temp,
        max_tokens=tokens,
        top_p=top_p,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen,
        stop=stop)
    text = response['choices'][0]['text'].strip()
    return text

if __name__=='__main__':
    prompt = 'Write a list of famous American Actors:'
    response = gpt3_completion(prompt)
    print(response)

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

