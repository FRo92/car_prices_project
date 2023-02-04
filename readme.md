#### Estimador de Precios de Vehículos

### Consideraciones
Este modelo es aplicable a los vehículos más vendidos en Chile desde 2020, y son los siguientes:
* Hyundai Accent
* Suzuki Baleno
* Suzuki Swift
* Toyota Hilux
* Toyota Rav 4
* Mitsubishi L200
* Kia Morning
* Kia Rio
* Chevrolet Sail
* Chevrolet Spark
* Nissan Navara
* Nissan NP300
* Nissan Versa
* Chery Tiggo 2,7 y 8
* Maxxus T60
* MG ZS

### 1. Web Scrapping
Primero se hizo una extracción de datos a la sección automotriz de Yapo.cl, esta sección está desarrollada en la carpeta de Web Scrapping Yapo.
Recorrimos todas las páginas con vehículos disponibles para la venta, con el filtro de vehículos, camionetas y 4x4, dejando de lado aquellas unidades catalogadas como "desarme" y solo nos enfocamos en la oferta para la región metropolitana.

### 2. Exploración
Una vez recopilados los datos desde Yapo.cl continuamos con la exploración, donde proponemos análisis de boxplot para identificar tendencias y datos anómalos entre los vehículos más vendidos mencionados al inicio, y también analizamos la oferta por vehículos dentro de la RM.

### 3. Modelamiento
Se entrenó una regresión multivariable para cada modelo más vendido, separando los datos entre training y test. Además de calcular el error porcentual para cada uno y presentar el promedio, este modelamiento está contenido en el archivo "regresion_modelos.ipynb". Cada regresión obtenida fue guardada en una carpeta para su posterior utilización en un código automatizado llamado "set_prices.py", en el siguiente bloque se explicará su ejecución.

Consideraciones: Este modelo se entrenó con datos extraidos desde yapo, además considera vehículos desde el año 2000 y kilometrajes menores a 500.000.

### ¿Cómo ejecutar el código?

Primero se deben instalar las librerías necesarias (se recomienda crear un ambiente seguro) ejecutando el siguiente comando en la terminal (python -v 3.8.10):

````pip install -r requirements.txt
```
Luego, podemos ejecutar el modelo de la siguiente forma:

```make recomendador_precios brand='brand' model='model' year=year km=km
```
Donde 'brand' corresponde a la marca del vehículo, 'model' corresponde al modelo, year es el año de fabricación y km es el kilometraje.

Finalmente el modelo entrega un precio estimado según las características ingresadas y además indica el valor de tasación según el SII.