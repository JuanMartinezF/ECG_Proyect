"""
Despues de haber extraido la información de los ventriculos con el codifgo
carac.py; este codigo lo que hace es tomar todos los archivos de la carpeta 'datanoclean'
y hacerle el tratamiento de limpieza a cada archivo y rembrandolo ademas que llevandolo a
su nueva ubicacion 'data_clean' donde los datos ya estan limpios

"""


import pandas as pd
import os
#from main import  data_for_clean, path_data_clean, path_data



def clean_data(route):


    #df_data = [archivo for archivo in os.listdir(route) if archivo.lower().endswith('.csv')]

    dataframes = []
    

    #II,III,aVR,aVL,aVF,V1,V2,V3,V4,V5,V6'
    for file in archivios_csv:
        
        ruta_completa = os.path.join(path_data_for_clean, file)
        df_data_all = pd.read_csv(ruta_completa)       
        df_data_all['I'] = df_data_all['I'].replace('["""]','', regex = True)
        df_data_all['II'] = df_data_all['II'].replace('["""]','', regex = True)
        df_data_all['III'] = df_data_all['III'].replace('["""]','', regex = True)
        df_data_all['aVR'] = df_data_all['aVR'].replace('["""]','', regex = True)
        df_data_all['aVL'] = df_data_all['aVL'].replace('["""]','', regex = True)
        df_data_all['aVF'] = df_data_all['aVF'].replace('["""]','', regex = True)
        df_data_all['V1'] = df_data_all['V1'].replace('["""]','', regex = True)
        df_data_all['V2'] = df_data_all['V2'].replace('["""]','', regex = True)
        df_data_all['V3'] = df_data_all['V3'].replace('["""]','', regex = True)
        df_data_all['V4'] = df_data_all['V4'].replace('["""]','', regex = True)
        df_data_all['V5'] = df_data_all['V5'].replace('["""]','', regex = True)
        df_data_all['V6'] = df_data_all['V6'].replace('["""]','', regex = True)
    dataframes.append(df_data_all)
    
    df_cleaned = pd.concat(dataframes, ignore_index = True)
    return df_cleaned


path_out_clean = 'D:/Bases_De_Datos/Proyecto_ECG/PF12RED-main/data_clean'

path_data_for_clean = 'D:/Bases_De_Datos/Proyecto_ECG/PF12RED-main/datanotclean'

archivios_csv = [file_cvs for file_cvs in os.listdir(path_data_for_clean) if file_cvs.lower().endswith('.csv')]
print (archivios_csv)

for cvs_file in archivios_csv:
    openroute = clean_data(os.path.join(path_data_for_clean, cvs_file))
    csv_file_name = os.path.splitext(cvs_file)[0] + '_clean.csv'
    csv_file_path = os.path.join(path_out_clean, csv_file_name)
    openroute.to_csv(csv_file_path, index=False)

print("Archivos CSV limpios y generados correctamente.")