import streamlit as st
from gtts import gTTS
from io import BytesIO

# Diccionario con palabras a traducir
diccionario = {
    'a': 'nuù ',
        'adentro': 'inì ',
        'adonde': 'ndéchi ',
        'al': 'ná ',
        'algo': 'joò ',
        'alli': 'uán ',
        'alto': 'súkú ', 
        'amargo': 'uhà ',
        'amarillo': 'kuáán ',
        'anda': 'jíka ',
        'aquel': 'uán ', 
        'aqui': 'yáha ',
        'asi': 'suán ', 
        'año': 'kuià ',
        'bien': 'kuééni ',
        'blanco': 'yáá ',
        'bonito': 'luu ',
        'borrego': 'rii ',
        'bravo': 'shraán ', 
        'buenos': 'tanìn ',
        'buenas': 'tanì ', 
        'cabeza': 'shini ', 
        'cafe': 'yahá(color) ',
        'camino': 'ichi ',
        'canasta': 'jika ',
        'ceniza': 'yàà ', 
        'chile': 'yaha ', 
        'choches': 'kuaa ',
        'comadre': 'kualiá ',
        'como': 'ndesa ',
        'compadre': 'mpáà ',
        'contiene': 'ñúhu ',
        'convertirse': 'nduu ',
        'cuando': 'nuù ',
        'cueva': 'túnchi ',
        'culebra': 'koó ', 
        'decir': 'kéi ',
        'deidad': 'ñuhú ',
        'despacio': 'kuéé ',
        'dia': 'dí ', 
        'dias': 'díí ',
        'dinero': 'shrúhún ',
        'en': 'nuù ', 
        'encontrarse': 'yóó ', 
        'encuentra': 'yóó ', 
        'enojarse': 'kiti-iní ', 
        'es': 'kúu ', 
        'esa': 'uán ',
        'ese': 'uán ', 
        'esta': 'kúu ',
        'estan': 'kákuu ',
        'estar': 'yóó ',
        'este': 'yàhá ',
        'fiesta': 'víko ', 
        'filoso': 'shraán ', 
        'fuego': 'ñuhú ',
        'grande': 'kánhu ', 
        'guajolote': 'kóhló ',
        'guajolotito': 'pípí ',
        'hacer': 'kisáhaní ',
        'hay': 'yóó ', 
        'hervir': 'hervir ',
        'hijo': 'séhe ',
        'humo': 'yahà(ollin) ',
        'ir': 'ki (futuro) ',
        'irse': 'kihín ', 
        'jaguar': 'kuiní ',
        'la': 'ná ', 
        'lejos': 'jíká ',
        'lengua': 'yaa ',
        'leña': 'ndukú ',
        'llama': 'nání ',
        'llamarse': 'nání ',
        'llamas': 'náníró ',
        'llamo': 'nání ',
        'madera': 'yunu ',
        'madre': 'náà ',
        'maguey': 'yáú ',
        'mano': 'ndaha ', 
        'me': 'ná ',
        'mercado': 'yahu ',
        'mero': 'máá ', 
        'mi': 'ri(ná) ',
        'mirar': 'koto ', 
        'mismo': 'máá ', 
        'monte': 'yuko ',
        'mucho': 'shraán ',
        'musica': 'yàà ',
        'muy': 'shraán ',
        'noche': 'kua ',
        'noches': 'kuaa ',
        'otro': 'inga ', 
        'padre': 'táà ',
        'parados': 'ká-íin',
        'pecho': 'jikà ',
        'petate': 'yuu ',
        'piedra': 'yuú ',
        'pueblo': 'ñuù ',
        'que': 'já ',
        'recoger': 'nastútú ', 
        'regresar': 'yàà ',
        'relajado': 'kuééni ',
        'seco': 'íchí ',
        'ser': 'kúu ',
        'sólido': 'yúú ',
        'su': 'ní ',
        'tamal de helote': 'suu ',
        'tambien': 'suni ',
        'tarde': 'ñín ',
        'tardes': 'ñíni ', 
        'tierra': 'ñuhu ', 
        'trabajo': 'tiun ',
        'tu': 'ró', 
        'un': 'in ',
        'una': 'in ',
        'uno': 'in ',
        'usted': 'ní ',
        'va': 'kihín ',
        'verdura': 'nduà (cruda) yuán (cocida) ',
        'volver': 'nduu ',
        'voy': 'kihín(ri)  ',
        'y': 'te ',
        'yo': 'ri-ná(con respeto)',
}

#def traducir_oracion(oracion):
 #   palabras = oracion.split()
  #  oracion_traducida = " ".join([diccionario.get(palabra.lower(), palabra) for palabra in palabras])
   # return oracion_traducida

st.title("Traductor de español a Mixteco")

# Preguntar al usuario por una oración en inglés
oracion = st.text_input("Ingresa una oración en español:")

# if st.button("Traducir"):
#    oracion_traducida = traducir_oracion(oracion)
#    st.write(f"La oración traducida al mixeco es: {oracion_traducida}")

    # Implementa tu lógica para traducir la oración aquí
   # return oracion
# Función para traducir una oración

def traducir_oracion(oracion):
    # Implementa tu lógica para traducir la oración aquí
    return oracion

# Función para convertir texto a voz
def texto_a_voz(texto):
    tts = gTTS(texto, lang='es')
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)
    return audio_bytes.getvalue()

if st.button("Traducir"):
    oracion_traducida = traducir_oracion(oracion)
    st.write(f"Traducción: {oracion_traducida}")

    # Convertir la traducción en voz
    audio_data = texto_a_voz(oracion_traducida)
    st.audio(audio_data, format='audio/mp3')
