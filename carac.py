"""
Este codigo contiene la función principal para tomar la
información del archivo XML y en especifico la información
de los ventriculos para guardarlos en un formato csv y ubicandolos
en una nueva carpeta llamada 'datanotclean' 

"""

import pandas as pd
import xml.etree.ElementTree as ET
#from acces_arch import file_data
#from main import extr_data

def get_vent(data):
    
    tree = ET.parse(data)
    root = tree.getroot()

    # Crear diccionario para almacenar los datos de las señales
    signal_data = {}
    
    for ventri in root.findall('.//WaveformData'):
        lead_name = ventri.get('lead')  # Obtener el nombre de la señal
        signal_values = ventri.text.strip()  # Obtener los valores de la señal (como cadena)
        signal_data[lead_name] = signal_values.split(',')  # Dividir los valores en una lista

    # Crear DataFrame a partir del diccionario
    df_vent = pd.DataFrame(signal_data)

    return df_vent


# Ruta del archivo XML (ajusta según la ubicación real del archivo)

#df_ventriculos = get_vent(path_data)

#df_ventriculos