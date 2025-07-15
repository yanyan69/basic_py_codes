from groq import Groq
from dotenv import dotenv_values

config = dotenv_values('.env')

client = Groq(
    api_key=config['API_KEY']
    )
def generate_blog(paragraph_topic):
    response = client.chat.completions.create(
        model = 'meta-llama/llama-4-scout-17b-16e-instruct',
        messages = [
            {
                'role': 'user', 'content': f'Write a single-paragraph blog post about: {paragraph_topic}, end it naturally knowing your limit is 120 tokens.'
            }
        ],
        max_tokens = 120,
        temperature = 1.0,
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
    

