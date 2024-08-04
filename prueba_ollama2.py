import ollama

messages =[
    {
    'role' : 'user',
    'content': 'Escribe una descipción para un curriculum de un desarrollador web junior'
    },
]

stream = ollama.chat(model ='llama3.1:latest', messages=messages, stream=True)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)