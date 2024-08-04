import ollama

def chat_ollama():
    print('Chat Llama 3.1! Escribe "salir" para finalizar la conversación.')
    while True:
        user_input = input('Tu: ')
        
        if user_input.lower() == 'salir':
            print('Adios!!')
            break
    
        response = ollama.generate(model='llama3.1:latest', prompt=user_input)
        print("Bot: ", response['response'])
        
chat_ollama()
        
    