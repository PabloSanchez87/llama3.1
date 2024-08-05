import os
from dotenv import load_dotenv

load_dotenv()  # Carga las variables desde el archivo .env

# Variables de entorno
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# -------------- CONFIGURACIÓN STREAMLIT--------------
page_title = "Asistente virtual con Llama 3.1"  # Título de la página de la aplicación
page_icon = "💬" # Icono de la página
layout = "centered"  

# Configuración de Streamlit
def set_page_config():
    import streamlit as st
    st.set_page_config(
        page_title=page_title,
        page_icon=page_icon,
        layout=layout,
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://www.linkedin.com/in/pablosancheztorres/',
            'Report a bug': 'https://github.com/PabloSanchez87/Utils_with_Python/issues',
            'About': "# Chat generado con Llama 3.1\nEsta aplicación genera un chat con memoria personalizable.\n\nCreada por Pablo Sánchez.\nPara soporte, envíe un correo a sancheztorrespablo@gmail.com."
        },
        
    )
    