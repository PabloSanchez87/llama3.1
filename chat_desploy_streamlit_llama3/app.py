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
    st.markdown("<h1 style='text-align: center; color: red;'>Asistente virtual - Llama 3.1</h1>", unsafe_allow_html=True)
    
    # Set the system prompt
    system_prompt = {
        "role": "system",
        "content": "Bienvenido! Soy un asistente virtual, ¿en qué puedo ayudarte?"
    }
    
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []
        st.session_state['messages'].append(system_prompt)
        
    def submit():
        user_input = st.session_state.user_input.strip()
        if user_input.lower() == 'salir':
            st.write('Gracias por usar nuestro chat. ¡Adiós!')
            st.stop()
            
        if user_input:  # Verifica que el mensaje no esté en blanco
            st.session_state['messages'].append({'role': 'user', 'content': user_input})
            
            with st.spinner('Obteniendo respuesta...'):
                ai_response = get_ai_response(st.session_state['messages'])
                st.session_state['messages'].append({'role': 'assistant', 'content': ai_response})

    # Mostrar los mensajes
    if st.session_state['messages']:
        for msg in st.session_state['messages']:
            if msg['role'] == 'user':
                st.markdown(f"<div style='padding: 10px; border-radius: 10px; margin: 10px 0; text-align: left;'><b><u>Tú</u></b><br>{msg['content']}</div>", unsafe_allow_html=True)  
            else:
                st.markdown(f"<div style='background-color: #4D4D4D; color: white; padding: 10px; border-radius: 10px; margin: 10px 0; text-align: left;'><b><u>Asistente</u></b><br>{msg['content']}</div>", unsafe_allow_html=True) 
            
    with st.form(key='chat_form', clear_on_submit=True):
        st.text_input("Tu:", key='user_input')
        st.form_submit_button(label='Enviar', on_click=submit)

    # Añadir el pie de página centrado
    st.markdown("<p style='text-align: right; color: gray'>App desarrollada por Pablo Sánchez.</p>", unsafe_allow_html=True)

if __name__ == '__main__':
    chat()
