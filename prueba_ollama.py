import ollama

messages =[
    {
    'role' : 'user',
    'content': '¿Para qué sirve el rabo de los gatos?'
    },
]

response = ollama.chat(model ='llama3.1:latest', messages=messages)

print(response['message']['content'])