from typing import Union
import pandas as pd
from fuzzywuzzy import process

# def get_filtered_population(provincia: Union[str, None], municipio: Union[str, None], barrio: Union[str, None]):
#     # Load the Excel file
#     df = pd.read_excel('app/data/POBLACION_NSC.xlsx')
    
#     # Filter the DataFrame based on the provided parameters
#     if provincia:
#         df = df[df['PROVINCIA'] == provincia]
#     if municipio:
#         df = df[df['MUNICIPIO'] == municipio]
#     if barrio:
#         df = df[df['BARRIO'] == barrio]
    
#     if not df.empty:
#         total_population = df['TOTAL'].sum()
#         return {"provincia": provincia, "municipio": municipio, "barrio": barrio, "total_population": total_population}
#     else:
#         return {"error": "No matching records found"}
    


def get_filtered_population(provincia: Union[str, None], municipio: Union[str, None], barrio: Union[str, None]):
    # Load the Excel file
    df = pd.read_excel('app/data/POBLACION_NSC.xlsx')

    
    # Function to get the best match for a given value in a column
    def get_best_match(value, column):
        choices = df[column].unique()
        best_match, score = process.extractOne(value, choices)
        return best_match if score > 80 else None  # Adjust the threshold as needed
    
# Filter the DataFrame based on the provided parameters
    if provincia:
        best_match = get_best_match(provincia, 'PROVINCIA')
        if best_match:
            df = df[df['PROVINCIA'] == best_match]
        else:
            return {"error": f"No matching records found for provincia: {provincia}"}
    
    if municipio:
        best_match = get_best_match(municipio, 'MUNICIPIO')
        if best_match:
            df = df[df['MUNICIPIO'] == best_match]
        else:
            return {"error": f"No matching records found for municipio: {municipio}"}
    
    if barrio:
        best_match = get_best_match(barrio, 'BARRIO')
        if best_match:
            df = df[df['BARRIO'] == best_match]
        else:
            return {"error": f"No matching records found for barrio: {barrio}"}
    
    if not df.empty:
        # print(df['TOTAL'])
        total_population = df['TOTAL'].sum()
        # Convert numpy.int64 to int
        total_population = int(total_population)
        return {"provincia": provincia, "municipio": municipio, "barrio": barrio, "total_population": total_population}
    else:
        return {"error": "No matching records found"}