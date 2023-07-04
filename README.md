# TFG: Sistemas de Recomendación
En este repositorio se encuentra el código desarrollado en el trabajo de fin de grado "Análisis de los efectos producidos en la combinación de diferentes fuentes de información en la recomendación de puntos de interés".

En este proyecto se ha desarrollado un framework que trabaja con con los datos de redes sociales basadas en localización para generar recomendaciones y evaluarlas.

- Autor: Beatriz Sicilia Gómez

- Director: Pablo Sánchez Pérez

- Grado en Ingeniería de Telecomunicaciones, ICAI 2023

## Instrucciones de ejecución: 

### Preparación de los datos:
1. Crea una carpeta llamada "datasets" en tu directorio de trabajo de Python.

2. Descarga los archivos de cada enlace y guárdalos en su carpeta individual dentro de "datasets". (A continuación se especifica nombreCarpeta : enlace). 
- foursquare: https://sites.google.com/site/yangdingqi/home/foursquare-dataset
- gowalla: https://snap.stanford.edu/data/loc-gowalla.html
- brightkite: https://snap.stanford.edu/data/loc-brightkite.html

3. Ejecuta los programas dentro de cada carpeta de preprocesado siguiendo el orden indicado.
-Resultado dataProcessingFoursquare: se obtendrán en la subcarpeta "subsets" los conjuntos de entrenamiento, validación y test. 
-Resultado dataProcessingGowalla: se obtendrá un fichero para cada ciudad con los check-ins que serán añadidos a Foursquare. 
-Resultado dataProcessingBrightkite: se obtendrá un fichero para cada ciudad con los check-ins que serán añadidos a Foursquare y Gowalla. 


4. En la carpeta "subsets" exiten 2 programas:
-juntar.py: fusiona los archivos de validación y entrenamiento en un conjunto de entrenamiento completo. 
-merge.py: crea los nuevos conjuntos de entrenamiento que incorporan los datos de Gowalla y Brightkite. 


### Generación de las recomendaciones: 
Llegados a este paso, se contarán con los conjuntos de datos procesados y listos para generar recomendaciones y posteriormente evaluarlas. 

#### Carpeta Clases: 
- funciones.py: Aquí se han agrupado aquellas funciones que se utilizan varias veces durante el código. 
- recomendador_clase.py: Aquí se encuentran todos los recomendadores desarrollados. 
- metrica_user_clase.py: Aquí se encuentra el desarrollo de aquellas métricas que son calculadas para cada usuario (Epc, precisión, recall). 
- metrica_test_clase.py: Aquí se encuentra el desarrollo de las métricas calculadas para todas las recomendaciones (User coverage, Aggregate Diversity). 


#### Carpeta Pruebas: 
- EjemploGeneracionRecomendaciones.py: Se propone un ejemplo de generación de recomendaciones utilizando la clase recomendador.
- EjemploObtencionMetricas.py: Se ejemplifica la obtención de métricas. 



## Notas: 
- En este caso, el análisis se ha centrado en los datos de Foursquare de las ciudades de Nueva York y Tokio. Si se quisiera ampliar este análisis a otras ciudades, únicamente habría que modificar las listas "ciudades_escogidas" y "paises" en las primeras líneas del archivo encontrado en la ruta "dataProcessingFoursquare/cities&pois_1.py". 

- En caso de modificar la ciudad, se debería ejecutar los módulos de preprocesado de datos de Yelp para comprobar si existe alguna equivalencia dentro de este dataset con los datos de Foursquare para esta nueva ciudad. 




