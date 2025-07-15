from groq import Groq
from dotenv import dotenv_values

config = dotenv_values('.env')

client = Groq(
    api_key=('API_KEY'),
    )
def generate_blog(paragraph_topic):
    response = client.chat.completions.create(
        model = 'llama-3.3-70b-versatile',
        messages = [
            {
                'role': 'user', 'content': f'Write a blog post about: {paragraph_topic}'
            }
        ],
        max_tokens = 100,
        temperature = 0.3
    )
    
    return response.choices[0].message.content


keep_writing = True
while keep_writing:
    answer = input('Write a paragraph? (y/n): ')
    if answer == 'y':
        paragraph_topic = input('What topic should the paragraph be about? ')
        print(generate_blog(paragraph_topic))
    else:
        keep_writing = False
        break
    

