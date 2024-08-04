import streamlit as st

from langchain_community.llms import Ollama
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from config import set_page_config

llm = Ollama(model='llama3.1:latest')

def main():
    
    with st.container():
        c1, caux, c2 = st.columns([4,0.5,5])
        bot_name = c1.text_input('Nombre del asistente virtual (editable)', value='Bot')
        prompt =f'''Eres un asistente virtual, te llamas {bot_name}. Si no te especifico un tema debes preguntarme sobre que quiero hablar o sobre que necesito información. Una vez te facilite esa información debes centrarte en ese tema para ser lo más concreto posible.'''
        bot_descripcion = c1.text_area("Descripción del asistente virtual (editable)", value=prompt)
        
        if 'chat_history' not in st.session_state:
            st.session_state['chat_history'] = []
            
        prompt_template = ChatPromptTemplate.from_messages(
            [
                ('system', bot_descripcion), # contexto
                MessagesPlaceholder(variable_name='chat_history'), # Variable de history
                ('human', '{input}') # input del humano
            ]
        )
        
        chain = prompt_template | llm

        user_input = c1.text_input('Escribe tu pregunta:', key='user_input')
        
        if c1.button('Enviar', type='primary'):
            if user_input.lower() == 'adios':
                st.stop()
            else:
                response = chain.invoke({'input': user_input,
                                        'chat_history': st.session_state['chat_history']})
                st.session_state['chat_history'].append(HumanMessage(content=user_input))
                st.session_state['chat_history'].append(AIMessage(content=response))
                
        chat_display = ''

        for msg in st.session_state['chat_history']:
            if isinstance(msg, HumanMessage):
                chat_display += f'<div style="text-align: right;">🙋 Tú: {msg.content}</div><br>'
            if isinstance(msg, AIMessage):
                chat_display += f'<div style="text-align: left;">🤖 {bot_name}: {msg.content}</div><br>'

        c2.markdown(chat_display, unsafe_allow_html=True)
        

# Running...
if __name__ == '__main__':
    set_page_config()
    
    main()
