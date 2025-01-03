
import streamlit as st

# Function to generate ideas in different stages
def generate_ideas_with_roles(input_idea):
    imagineering_version = (
        f"En el estadio Imagineering, el visionario propone diseñar '{input_idea}' "
        "enfocándose en la creatividad humana. La ejecución se realiza mediante "
        "métodos tangibles y tradicionales, con un bajo uso de tecnología avanzada, "
        "resaltando la originalidad de la idea."
    )
    
    reimagineering_version = (
        f"En el estadio ReImagineering, el arquitecto toma la idea de '{input_idea}' y la "
        "reinterpreta integrando tecnología moderada. La propuesta mantiene el núcleo "
        "creativo humano, pero optimiza la ejecución mediante herramientas modernas y "
        "metodologías avanzadas que potencian el impacto del proyecto."
    )
    
    aimagineering_version = (
        f"En el estadio AImagineering, el curador supervisa la transformación de '{input_idea}' "
        "en una propuesta impulsada por tecnología avanzada. La creatividad está parcialmente "
        "asistida por inteligencia artificial, y la ejecución se automatiza para ofrecer "
        "personalización masiva e innovación continua."
    )
    
    return {
        "Imagineering (Visionario)": imagineering_version,
        "ReImagineering (Arquitecto)": reimagineering_version,
        "AImagineering (Curador)": aimagineering_version
    }

# Streamlit app interface
st.title("Generador de Propuestas: Imagineering, ReImagineering y AImagineering")

# Input field for the idea
input_idea = st.text_input("Ingresa tu idea:", "")

# Button to generate the ideas
if st.button("Generar Propuestas"):
    if input_idea:
        output = generate_ideas_with_roles(input_idea)
        for stage, idea in output.items():
            st.subheader(stage)
            st.write(idea)
    else:
        st.warning("Por favor, ingresa una idea para continuar.")
