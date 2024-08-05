from config import GROQ_API_KEY, set_page_config
from groq import Groq
import streamlit as st

# Inicializamos el cliente de Groq
client = Groq(api_key=GROQ_API_KEY)

def get_ai_response(messages):
    completion = client.chat.completions.create(
        model='llama-3.1-70b-versatile',
        messages=messages,
        temperature=0.7,
        max_tokens=1024,
        stream=False
    )
    
    # Obtener el contenido de la respuesta del asistente
    response = completion.choices[0].message.content
    return response

def chat():
    set_page_config()
    st.title('¡Bienvenido! Chatea con LLama 3.1')
    
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []
        
    def submit():
        user_input = st.session_state.user_input
        if user_input.lower() == 'salir':
            st.write('Gracias por usar nuestro chat. ¡Adiós!')
            st.stop()
            
        st.session_state['messages'].append({'role': 'user', 'content': user_input})
        
        with st.spinner('Obteniendo respuesta...'):
            ai_response = get_ai_response(st.session_state['messages'])
            st.session_state['messages'].append({'role': 'assistant', 'content': ai_response})

    # Mostrar los mensajes
    if st.session_state['messages']:
        for msg in st.session_state['messages']:
            role = "Tu" if msg['role'] == 'user' else "Asistente"
            st.write(f"**{role}:** {msg['content']}")
            
    with st.form(key='chat_form', clear_on_submit=True):
        st.text_input("Tu:", key='user_input')
        submit_button = st.form_submit_button(label='Enviar', on_click=submit)

if __name__ == '__main__':
    chat()
