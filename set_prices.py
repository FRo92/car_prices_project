import pandas as pd 
import numpy as np
import pickle
import argparse

# cargamos la tasación del SII

def set_price(brand,model,year,km):
    tasacion = pd.read_excel("../proyecto_final/liv2022.xlsx",header=13)

    filename = f"regression_{model.lower()}"
    loaded_model = pickle.load(open(f"./models/{filename}.sav", 'rb'))
    antiguedad = 2022-year
    km_miles = km/1000
    price = loaded_model.coef_[0]*antiguedad+loaded_model.coef_[1]*km_miles+loaded_model.intercept_
    rangos = [round((price-price*0.1)*1000000,0), round((price+price*0.1)*1000000,2)]
    price = int(round(price*1000000,0))
    model = model.upper()
    try:
        tasacion_vehiculo = int(tasacion.query("Año == @year and Modelo ==@model ")[["TASACIÓN 2022"]].median().values[0])
    except:
        tasacion_vehiculo = f"no hay tasación fiscal para el año {year}"

    #return print(f"el precio estimado para un {brand.upper()}-{model} de esas características se encentra dentro del rango ${rangos[0]} y rango  ${rangos[1]} y su tasación es ${tasacion_vehiculo}")
    return print(f"El precio estimado para un 🚗{brand.upper()}-{model} de esas características es: \n💸 ${price}\nY su tasación fiscal es: \n💸 ${tasacion_vehiculo}")
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='set car prices 🚗')
    parser.add_argument('-brand', type=str,
                        help='marca del auto',required=True)
    parser.add_argument('-model', type=str,
                        help='modelo del auto',required=True)
    parser.add_argument('-year', type=int,
                        help='año del auto formato YYYY',required=True)     
    parser.add_argument('-km', type=int,
                        help='kilometraje del auto',required=True)                 
    args = parser.parse_args()    
    set_price(args.brand,args.model,args.year,args.km)                                       