# Importamos las librerías necesarias
import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from config import set_page_config

# Inicializamos el modelo de lenguaje llamando a la clase Ollama y seleccionando el modelo 'llama3.1:latest'
llm = Ollama(model='llama3.1:latest')

# Definimos la función principal que ejecutará la aplicación
def main():
    # Configuramos la página de Streamlit
    set_page_config()
    
    # Añadimos un título centrado y en color rojo a la aplicación
    st.markdown("<h1 style='text-align: center; color: red;'>Asistente virtual - Llama 3.1</h1>", unsafe_allow_html=True)

    # Dividimos la página en dos columnas con diferentes proporciones
    c1, c2 = st.columns([1, 5])
    
    # En la primera columna, dejamos un espacio y añadimos un campo de entrada de texto para el nombre del bot
    with c1:
        c1.write(" ")
        c1.write(" ")
        bot_name = st.text_input('Nombre del asistente virtual', value='Bot')
        

    # En la segunda columna, añadimos un área de texto para el prompt inicial de la IA
    with c2:
        prompt = f'''Eres un asistente virtual, te llamas {bot_name}. Si no se especifica un tema debes preguntarme sobre qué quiero hablar o sobre qué necesito información. Una vez te facilite esa información debes mantener ese contexto salvo que se indique lo contrario'''
        bot_descripcion = st.text_area("Prompt inicial de la IA (editable)", value=prompt, height=120)
    
    # Creamos una plantilla de prompt para el chatbot usando el prompt inicial
    prompt_template = ChatPromptTemplate.from_messages(
        [
            ('system', bot_descripcion),  # Mensaje inicial del sistema
            MessagesPlaceholder(variable_name='chat_history'),  # Placeholder para el historial de chat
            ('human', '{input}')  # Mensaje del usuario
        ]
    )
    
    # Encadenamos la plantilla del prompt con el modelo de lenguaje
    chain = prompt_template | llm
    
    # Inicializamos el historial del chat si no existe en el estado de la sesión
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    # Función para manejar el envío de mensajes
    def handle_send():
        user_input = st.session_state.user_input
        if user_input.lower() == 'adios':  # Si el usuario dice "adios"
            response = "Gracias por usar nuestro asistente virtual. Puedes cerrar la aplicación cuando quieras."
            st.session_state['chat_history'].append(HumanMessage(content=user_input))
            st.session_state['chat_history'].append(AIMessage(content=response))
        else:
            # Obtenemos la respuesta del modelo de lenguaje
            response = chain.invoke({'input': user_input, 'chat_history': st.session_state['chat_history']})
            st.session_state['chat_history'].append(HumanMessage(content=user_input))
            st.session_state['chat_history'].append(AIMessage(content=response))

    # Campo de entrada de chat para el usuario
    user_input = st.chat_input("Escribe tu pregunta:")
    if user_input:  # Si el usuario ha escrito algo
        st.session_state.user_input = user_input
        handle_send()  # Maneja el envío del mensaje

    # Mostramos el historial del chat en la interfaz
    for message in st.session_state['chat_history']:
        if isinstance(message, HumanMessage):  # Si el mensaje es del usuario
            with st.chat_message("user"):
                st.write(f"Tu: {message.content}")
        elif isinstance(message, AIMessage):  # Si el mensaje es del asistente
            with st.chat_message("assistant"):
                st.write(f"{bot_name}")
                st.write(f"{message.content}")

    # Añadir el pie de página centrado
    st.markdown("<p style='text-align: right; color: gray'>App desarrollada por Pablo Sánchez.</p>", unsafe_allow_html=True)

# Punto de entrada de la aplicación
if __name__ == '__main__':
    main()
