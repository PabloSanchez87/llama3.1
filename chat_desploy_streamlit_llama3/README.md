
# Asistente Virtual con Llama 3.1

Este proyecto es una aplicación web que funciona como un asistente virtual. Utiliza el modelo de inteligencia artificial Llama 3.1 proporcionado por la API de Groq para responder a preguntas y participar en conversaciones con los usuarios.

## Características

- **Asistente Virtual**: Utiliza Llama 3.1 para procesar y responder a entradas de texto en tiempo real.
- **Interfaz de Usuario Amigable**: Desarrollado con Streamlit, la aplicación presenta una interfaz clara y simple.
- **Historial de Chat**: Mantiene un historial de la conversación durante la sesión para un contexto continuo.

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal.
- **Streamlit**: Framework para crear aplicaciones web rápidamente con Python.
- **Groq API**: Proporciona acceso al modelo Llama 3.1 para el procesamiento del lenguaje natural.

## Probar la Aplicación

La aplicación está desplegada y puede ser probada directamente en el navegador a través del siguiente enlace:
[Prueba la aplicación aquí](https://chat-llama3.streamlit.app/)

## Configuración y Uso Local

Para ejecutar esta aplicación localmente, necesitarás Python instalado en tu sistema, así como las dependencias mencionadas en el archivo `requirements.txt`.

1. Clona el repositorio:
   ```
   git clone https://github.com/PabloSanchez87/llama3.1.git

2. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```
3. Ejecuta la aplicación:
   ```
   cd chat_desploy_streamlit_llama3
   streamlit run app.py
   ```

## Documentación de la API de Groq

La aplicación utiliza la [API de Groq](https://console.groq.com/docs/quickstart) para interactuar con el modelo Llama 3.1. Esta API permite realizar solicitudes de procesamiento de lenguaje natural y obtener respuestas en tiempo real. Es necesario tener una clave API válida para autenticar las solicitudes.

Para más detalles sobre la configuración y opciones de la API, visita la documentación oficial de Groq.

## Autor

- **Pablo Sánchez** - _Desarrollador inicial de la aplicación_
  - [LinkedIn](https://www.linkedin.com/in/pablosancheztorres/)
  - [GitHub](https://github.com/PabloSanchez87/)

## Contribuciones
¡Las contribuciones son bienvenidas! Por favor, haga un fork del repositorio y envíe un pull request con sus mejoras.
