# SocialScienceAI

Una aplicación web especializada en ciencias sociales que integra modelos de IA como OpenAI (GPT) y Google Gemini.

## Características

- **Análisis de Textos**: Analiza documentos y datos cualitativos desde perspectivas de ciencias sociales
- **Asistente de Investigación**: Obtén respuestas a preguntas específicas por disciplina
- **Generador de Hipótesis**: Desarrolla hipótesis basadas en teorías y variables
- **Resumen de Literatura**: Sintetiza artículos académicos 
- **Metodología de Investigación**: Asistencia en diseño de investigaciones

## Configuración

Para ejecutar localmente:

1. Clonar este repositorio
2. Crear un archivo `.env` con tu clave API de OpenAI:
   ```
   OPENAI_API_KEY=tu_clave_aquí
   ```
3. Instalar dependencias: `pip install -r requirements.txt`
4. Ejecutar: `streamlit run app.py`

## Despliegue

Esta aplicación está desplegada en Streamlit Cloud y puede accederse desde [aquí](https://socialscienceai.streamlit.app).