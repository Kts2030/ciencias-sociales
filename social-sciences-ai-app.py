# app.py - Aplicación principal
import streamlit as st
from langchain.llms import OpenAI
from langchain.openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

# Cargar variables de entorno (API keys)
load_dotenv()

# Configuración de la página
st.set_page_config(
    page_title="SocialScienceAI",
    page_icon="🧠",
    layout="wide"
)

# Título y descripción
st.title("SocialScienceAI")
st.markdown("### Una plataforma de asistencia para investigación en ciencias sociales")

# Sidebar para navegación
st.sidebar.title("Navegación")
option = st.sidebar.selectbox(
    "Selecciona una herramienta:",
    ["Inicio", "Análisis de Textos", "Asistente de Investigación", "Generador de Hipótesis", 
     "Resumen de Literatura", "Metodología de Investigación"]
)

# Función para obtener respuesta del modelo
def get_ai_response(prompt, model_choice):
    try:
        if model_choice == "OpenAI":
            llm = ChatOpenAI(
                temperature=0.7,
                model_name="gpt-4",
                openai_api_key=os.getenv("OPENAI_API_KEY")
            )
        elif model_choice == "Google Gemini":
            # Nota: La integración con Gemini requeriría su API específica
            st.warning("La integración con Google Gemini está en desarrollo")
            return "Integración con Google Gemini próximamente disponible."
        
        response = llm.predict(prompt)
        return response
    except Exception as e:
        return f"Error al comunicarse con el modelo: {str(e)}"

# Páginas de la aplicación
if option == "Inicio":
    st.markdown("""
    ## Bienvenido a SocialScienceAI
    
    Esta plataforma está diseñada específicamente para académicos, investigadores y estudiantes
    de ciencias sociales que quieren aprovechar el poder de la inteligencia artificial para
    potenciar su trabajo.
    
    ### Características principales:
    - **Análisis de textos**: Analiza documentos, transcripciones o datos cualitativos
    - **Asistente de investigación**: Obtén respuestas a preguntas específicas de ciencias sociales
    - **Generador de hipótesis**: Desarrolla hipótesis basadas en teorías y datos existentes
    - **Resumen de literatura**: Sintetiza artículos académicos
    - **Metodología de investigación**: Asistencia en diseño de investigaciones
    
    Selecciona una herramienta en el menú lateral para comenzar.
    """)

elif option == "Análisis de Textos":
    st.header("Análisis de Textos")
    
    text_input = st.text_area("Ingresa el texto a analizar:", height=200)
    
    col1, col2 = st.columns(2)
    with col1:
        analysis_type = st.selectbox(
            "Tipo de análisis:",
            ["Análisis temático", "Análisis de discurso", "Codificación cualitativa", 
             "Análisis de sentimiento", "Extracción de conceptos clave"]
        )
    with col2:
        model_choice = st.selectbox("Selecciona el modelo:", ["OpenAI", "Google Gemini"])
    
    if st.button("Analizar"):
        if text_input:
            with st.spinner("Analizando texto..."):
                template = f"""
                Realiza un {analysis_type} del siguiente texto desde una perspectiva de ciencias sociales.
                
                TEXTO: {text_input}
                
                Proporciona un análisis detallado y estructurado considerando marcos teóricos relevantes
                en ciencias sociales. Incluye:
                1. Resumen del análisis
                2. Conceptos o temas principales identificados
                3. Conexiones con teorías de ciencias sociales
                4. Implicaciones potenciales
                """
                
                response = get_ai_response(template, model_choice)
                st.markdown("### Resultados del análisis")
                st.write(response)
        else:
            st.error("Por favor ingresa un texto para analizar.")

elif option == "Asistente de Investigación":
    st.header("Asistente de Investigación")
    
    # Campos de especialidad en ciencias sociales
    specialty = st.selectbox(
        "Área de especialidad:",
        ["Sociología", "Antropología", "Ciencias Políticas", "Economía", 
         "Psicología Social", "Historia", "Geografía Humana", "Estudios Culturales"]
    )
    
    question = st.text_area("¿Qué deseas investigar?", 
                           placeholder="Ej: ¿Cómo ha evolucionado el concepto de capital social en la última década?")
    
    model_choice = st.selectbox("Selecciona el modelo:", ["OpenAI", "Google Gemini"])
    
    if st.button("Consultar"):
        if question:
            with st.spinner("Buscando información..."):
                template = f"""
                Actúa como un experto investigador en {specialty} respondiendo a la siguiente pregunta
                desde una perspectiva académica de ciencias sociales. Proporciona información basada
                en teorías, investigaciones y datos relevantes hasta octubre de 2024. Incluye referencias
                a autores clave y conceptos fundamentales. La pregunta es:
                
                {question}
                """
                
                response = get_ai_response(template, model_choice)
                st.markdown("### Respuesta")
                st.write(response)
        else:
            st.error("Por favor ingresa una pregunta de investigación.")

elif option == "Generador de Hipótesis":
    st.header("Generador de Hipótesis")
    
    col1, col2 = st.columns(2)
    with col1:
        research_area = st.text_input("Área de investigación:", 
                                      placeholder="Ej: Movilidad social intergeneracional")
    with col2:
        variables = st.text_input("Variables de interés (separadas por comas):", 
                                 placeholder="Ej: educación, ingresos, género, origen étnico")
    
    theoretical_framework = st.text_area("Marco teórico de referencia (opcional):", 
                                        placeholder="Ej: Teoría de la reproducción social de Bourdieu")
    
    model_choice = st.selectbox("Selecciona el modelo:", ["OpenAI", "Google Gemini"])
    
    if st.button("Generar hipótesis"):
        if research_area and variables:
            with st.spinner("Generando hipótesis..."):
                template = f"""
                Genera 3-5 hipótesis de investigación para un estudio en el área de {research_area},
                considerando las siguientes variables: {variables}.
                
                {f"El estudio se basa en el marco teórico: {theoretical_framework}" if theoretical_framework else ""}
                
                Para cada hipótesis, proporciona:
                1. La hipótesis claramente formulada
                2. Justificación teórica
                3. Posible metodología para probarla
                4. Variables dependientes e independientes
                5. Posibles limitaciones
                """
                
                response = get_ai_response(template, model_choice)
                st.markdown("### Hipótesis generadas")
                st.write(response)
        else:
            st.error("Por favor completa los campos requeridos.")

elif option == "Resumen de Literatura":
    st.header("Resumen de Literatura")
    
    paper_text = st.text_area("Ingresa el texto del artículo académico:", height=300,
                             placeholder="Pega aquí el texto completo del artículo o abstract para resumir...")
    
    col1, col2 = st.columns(2)
    with col1:
        summary_length = st.select_slider("Longitud del resumen:", 
                                        options=["Muy breve", "Breve", "Moderado", "Detallado", "Muy detallado"],
                                        value="Moderado")
    with col2:
        focus = st.multiselect("Enfocar el resumen en:", 
                              ["Metodología", "Hallazgos", "Marco teórico", "Implicaciones", "Limitaciones"],
                              default=["Hallazgos", "Implicaciones"])
    
    model_choice = st.selectbox("Selecciona el modelo:", ["OpenAI", "Google Gemini"])
    
    if st.button("Resumir"):
        if paper_text:
            with st.spinner("Generando resumen..."):
                focus_str = ", ".join(focus) if focus else "todos los aspectos"
                template = f"""
                Resume el siguiente artículo académico de ciencias sociales con un nivel de detalle {summary_length.lower()},
                enfocándote principalmente en: {focus_str}.
                
                ARTÍCULO: {paper_text}
                
                Estructura el resumen incluyendo:
                - Objetivo principal del estudio
                - Contexto teórico
                - Metodología empleada
                - Hallazgos clave
                - Implicaciones para la teoría y práctica
                - Limitaciones del estudio
                """
                
                response = get_ai_response(template, model_choice)
                st.markdown("### Resumen del artículo")
                st.write(response)
        else:
            st.error("Por favor ingresa el texto del artículo para resumir.")

elif option == "Metodología de Investigación":
    st.header("Asistente de Metodología de Investigación")
    
    research_question = st.text_area("Pregunta de investigación:", 
                                    placeholder="Ej: ¿Cómo influye el capital cultural en el rendimiento académico de estudiantes universitarios de primera generación?")
    
    col1, col2 = st.columns(2)
    with col1:
        approach = st.selectbox("Enfoque metodológico preferido:", 
                               ["Cualitativo", "Cuantitativo", "Métodos mixtos", "No estoy seguro"])
    with col2:
        constraints = st.text_input("Limitaciones o restricciones:", 
                                  placeholder="Ej: Presupuesto limitado, acceso a 100 participantes")
    
    model_choice = st.selectbox("Selecciona el modelo:", ["OpenAI", "Google Gemini"])
    
    if st.button("Generar diseño metodológico"):
        if research_question:
            with st.spinner("Diseñando metodología..."):
                template = f"""
                Diseña una metodología de investigación para la siguiente pregunta en ciencias sociales:
                
                PREGUNTA: {research_question}
                
                Enfoque preferido: {approach}
                Limitaciones: {constraints if constraints else "No especificadas"}
                
                Proporciona un diseño metodológico completo que incluya:
                1. Método de investigación recomendado y justificación
                2. Diseño de muestreo
                3. Métodos de recolección de datos
                4. Instrumentos sugeridos
                5. Estrategia de análisis de datos
                6. Consideraciones éticas
                7. Limitaciones metodológicas
                8. Cronograma sugerido
                """
                
                response = get_ai_response(template, model_choice)
                st.markdown("### Diseño metodológico")
                st.write(response)
        else:
            st.error("Por favor ingresa una pregunta de investigación.")

# Pie de página
st.markdown("---")
st.markdown("SocialScienceAI - Desarrollada para investigadores en ciencias sociales")
