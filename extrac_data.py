import os
import pandas as pd
import xml.etree.ElementTree as ET

def get_vent(xml_file):
    tree = ET.parse(xml_file)
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

# Ruta de la carpeta con los archivos XML
xml_folder_path = 'D:/Bases_De_Datos/Proyecto_ECG/PF12RED-main/5_163XML'

# Ruta destino para los archivos CSV
csv_output_path = 'D:/Bases_De_Datos/Proyecto_ECG/PF12RED-main/5_153XML_csv'



# Obtener una lista de nombres de archivos XML en la carpeta
archivos_xml = [archivo for archivo in os.listdir(xml_folder_path) if archivo.lower().endswith('.xml')]

# Procesar cada archivo XML y guardar como CSV
for xml_file in archivos_xml:
    df_ventriculos = get_vent(os.path.join(xml_folder_path, xml_file))
    csv_file_name = os.path.splitext(xml_file)[0] + '.csv'
    csv_file_path = os.path.join(csv_output_path, csv_file_name)
    df_ventriculos.to_csv(csv_file_path, index=False)

print("Archivos CSV generados correctamente.")
