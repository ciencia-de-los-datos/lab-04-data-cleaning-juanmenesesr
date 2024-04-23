"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

from datetime import datetime as dt


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    df.drop("Unnamed: 0", axis=1, inplace=True)
    df.dropna(axis=0, inplace=True)

    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].str.lower()

    df.comuna_ciudadano = df.comuna_ciudadano.astype(int)

    def fechas(str_fecha):
        try:
            return dt.strptime(str_fecha, "%d/%m/%Y")
        except ValueError:
            return dt.strptime(str_fecha, "%Y/%m/%d")

    df.fecha_de_beneficio = df.fecha_de_beneficio.apply(fechas)

    df.monto_del_credito = df.monto_del_credito.str.replace("[$, ]", "", regex=True)
    df.monto_del_credito = df.monto_del_credito.str.replace(".00", "", regex=False)
    df.monto_del_credito = df.monto_del_credito.astype(float)

    df.línea_credito = df.línea_credito.str.replace("[-_]", " ", regex=True)
    df.idea_negocio = df.idea_negocio.str.replace("[_-]", " ", regex=True)
    df.barrio = df.barrio.str.replace("[-]", " ", regex=True)
    df.barrio = df.barrio.str.replace("[ ]+", "_", regex=True)
    df.comuna_ciudadano = df.comuna_ciudadano.astype(int)



    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    df.duplicated().sum()

    df.drop_duplicates(inplace=True)


    return df
   
df_cleaned = clean_data()
print(df_cleaned)


conteo_sexos = clean_data()["sexo"].value_counts()

print(conteo_sexos)

