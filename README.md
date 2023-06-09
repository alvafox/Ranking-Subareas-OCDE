# Ranking-Subareas-OCDE


Ranking por subáreas OCDE en dos etapas: (i) archivo de depuración y asignación de tipo ranking definitivo y (ii) cálculo de los índices y ordenamiento.

Los archivos deben ser descargados desde incites, guardándolos con el "Nombre Descarga EXCEL" en formato csv.

|    | SUBAREA OCDE                                  | Nombre Descarga EXCEL     | DF                    |   COD SUBAREA |
|---:|:----------------------------------------------|:--------------------------|:----------------------|--------------:|
|  0 | 1.01 Matemáticas                              | 101 Matematicas           | Matematicas           |          1.01 |
|  1 | 1.02 Computación y Ciencias de la informática | 102 Computacion           | Computacion           |          1.02 |
|  2 | 1.03 Ciencias Físicas y Astronomía            | 103 Fisica                | Fisica                |          1.03 |
|  3 | 1.04 Ciencias Químicas                        | 104 Quimica               | Quimica               |          1.04 |
|  4 | 1.05 Ciencias de la Tierra y Medioambientales | 105 Tierra                | Tierra                |          1.05 |
|  5 | 1.06 Ciencias Biológicas                      | 106 Biologicas            | Biologicas            |          1.06 |
|  6 | 1.07 Otras Ciencias Naturales                 | 107 Otras naturales       | Otras_naturales       |          1.07 |
|  7 | 2.01 Ingeniería Civil                         | 201 Civil                 | Civil                 |          2.01 |
|  8 | 2.02 Ingeniería Eléctrica y Electrónica       | 202 Electrica             | Electrica             |          2.02 |
|  9 | 2.03 Ingeniería Mecánica                      | 203 Mecanica              | Mecanica              |          2.03 |
| 10 | 2.04 Ingeniería Química                       | 204 Ing Quimica           | Ing_Quimica           |          2.04 |
| 11 | 2.05 Ingeniería de Materiales                 | 205 Ing Materiales        | Ing_Materiales        |          2.05 |
| 12 | 2.06 Ingeniería Médica                        | 206 Ing Medica            | Ing_Medica            |          2.06 |
| 13 | 2.07 Ingeniería Medioambiental                | 207 Ing Medioambiental    | Ing_Medioambiental    |          2.07 |
| 14 | 2.08 Biotecnología Medioambiental             | 208 Biotec Medioambiental | Biotec_Medioambiental |          2.08 |
| 15 | 2.09 Biotecnología Industrial                 | 209 Biotec Industrial     | Biotec_Industrial     |          2.09 |
| 16 | 2.10 Nanotecnología                           | 210 Nanotecnologia        | Nanotecnologia        |          2.1  |
| 17 | 2.11 Otras Ingenierías y Tecnologías          | 211 Otras Ingenierias     | Otras_Ingenierias     |          2.11 |
| 18 | 3.01 Medicina Básica                          | 301 Medicina Basica       | Medicina_Basica       |          3.01 |
| 19 | 3.02 Medicina Clínica                         | 302 Medicina Clinica      | Medicina_Clinica      |          3.02 |
| 20 | 3.03 Ciencias de la Salud                     | 303 Ciencias Salud        | Ciencias_Salud        |          3.03 |
| 21 | 4.01 Agricultura, Silvicultura y Pesca        | 401 Agricultura           | Agricultura           |          4.01 |
| 22 | 4.02 Ciencias Animales y de la Leche          | 402 Ciencias Animales     | Ciencias_Animales     |          4.02 |
| 23 | 4.03 Ciencias Veterinarias                    | 403 Ciencias Veterinarias | Ciencias_Veterinarias |          4.03 |
| 24 | 4.05 Otras Ciencias Agrícolas                 | 405 Otras Agricolas       | Otras_Agricolas       |          4.05 |
| 25 | 5.01 Psicología                               | 501 Psicologia            | Psicologia            |          5.01 |
| 26 | 5.02 Economía y Negocios                      | 502 Economia              | Economia              |          5.02 |
| 27 | 5.03 Ciencias de la Educación                 | 503 Educacion             | Educacion             |          5.03 |
| 28 | 5.04 Sociología                               | 504 Sociologia            | Sociologia            |          5.04 |
| 29 | 5.05 Leyes                                    | 505 Leyes                 | Leyes                 |          5.05 |
| 30 | 5.06 Ciencias Políticas                       | 506 Ciencias Politicas    | Ciencias_Politicas    |          5.06 |
| 31 | 5.07 Geografía Social y Económica             | 507 Geografia             | Geografia             |          5.07 |
| 32 | 5.08 Periodismo y Comunicaciones              | 508 Periodismo            | Periodismo            |          5.08 |
| 33 | 5.09 Otras Ciencias Sociales                  | 509 Otras Sociales        | Otras_Sociales        |          5.09 |
| 34 | 6.01 Historia y Arqueología                   | 601 Historia              | Historia              |          6.01 |
| 35 | 6.02 Idiomas y Literatura                     | 602 Idiomas               | Idiomas               |          6.02 |
| 36 | 6.03 Filosofía, Ética y Religión              | 603 Filosofia             | Filosofia             |          6.03 |
| 37 | 6.04 Arte                                     | 604 Arte                  | Arte                  |          6.04 |
| 38 | 6.05 Otras Humanidades                        | 605 Otras Humanidades     | Otras_Humanidades     |          6.05 |




# **1 - Primera Etapa**


Posterior a la descarga y almacenamiento de los insumos en la carpeta "INSUMOS", se debe considerar que las instituciones vienen clasificadas por defecto mediante la etiqueta presente en la columna "INSTITUCIONES". Para el cálculo hay que crear una nueva columna que las identifique correctamente, para evitar que instituciones no académicas alteren el ranking definitivo que se publicará. 

La clasificación se que llevará a cabo está detallada mediante la columna "Tipo de Institución". El primer script "Ranking OCDE Primera Etapa.py" hará este proceso, pero hay que editar el siguiente ciclo para que la clasificación sea la correcta. 


|    | INSTITUCIONES      | Tipo de Institución   |
|---:|:-------------------|:----------------------|
|  0 | Research Council   | No Académica          |
|  1 | National Academy   | No Académica          |
|  2 | Academic System    | Ninguna               |
|  3 | Research Institute | No Académica          |
|  4 | Academic           | Académica             |
|  5 | Government         | No Académica          |
|  6 | Nonprofit          | No Académica          |
|  7 | Health             | No Académica          |
|  8 | Corporate          | No Académica          |
|  9 | Partnership        | No Académica          |
| 10 | Healthcare System  | No Académica          |


Es importante revisar bien este ciclo, puesto que en la segunda etapa esta clasificacion es un insumo que determina a qué ranking pertenece cada institución académica. Hay que considerar que año a año aparecen nuevas instituciones que podrian no necesariamente ser académicas, por lo que hay que revisar los insumos. Este trabajo debe ser mediante cuidadosa revisión antes de pasar a ajecutar el script "Ranking OCDE Segunda Etapa.py". 

```
######################################### Determinar Tipos de Ranking DEFINITIVOS ########################################
rnk_202X_def = []
Tipo_Rnk_202X_def = []
for index, row in CONSOLIDADO.iterrows():
        if row["Tipo Ranking 202X (Defecto)"] == "2 - Ranking no Académico" and row["Country or Region"] == "CHILE":
                rnk_202X_def = "3 - Ninguno"
        elif row["Name"] == "European Southern Observatory" or row["Name"] == 'University of Rizal System':
                rnk_202X_def = "3 - Ninguno"
        elif row["Name"] == 'Colombo North Teaching Hospital' or \
                row["Name"] == 'Servicio Nacional de Aprendizaje' or \
                row["Name"] == 'UERM Memorial Medical Center':
                rnk_202X_def = "2 - Ranking no Académico"
        elif row["Tipo Ranking 202X (Defecto)"] == "3 - Ninguno" and\
                row["Country or Region"] != "USA" and\
                row["Name"] != "Indian Institute of Technology System (IIT System)" and \
                row["Name"] != "Indian Institute of Management (IIM System)" and \
                row["Name"] != "National Institute of Technology (NIT System)" and \
                row["Name"] != "University of the Philippines System" and\
                row["Name"] != "University of Quebec" and\
                row["Name"] != "University Town of Shenzhen" and \
                row["Name"] != 'UDICE-French Research Universities' and \
                row["Name"] != 'Mindanao State University System' and \
                row["Name"] != "University of London":
                rnk_202X_def = "1 - Ranking Académico"
        else:
                rnk_202X_def = row["Tipo Ranking 202X (Defecto)"]
        Tipo_Rnk_202X_def.append(rnk_202X_def)

CONSOLIDADO["Tipo Ranking 202X (Definitivo)"] = Tipo_Rnk_202X_def
```

# **2 - Segunda Etapa**


Ejecutar el archivo Ranking OCDE Segunda Etapa.py, que mediante iteraciones llevara a cabo la producción de todas las planillas independientes. Asimismo, también logrará la consolidación de toda la información en un excel que servirá para verificar la información.

El script, al igual que el primero, usará un archivo llamado 'Definiciones.csv'. Este archivo contiene los nombres con los cuales se guardaron los insumos, los nombres de los DataFrames y el nombre con el cual se exportarán los rankings definitivos de manera individual. 

```
DEFINICIONES = pd.read_csv('Definiciones.csv', sep=";", encoding="UTF-8", decimal=',')
```

Notar que el script "Ranking OCDE Segunda Etapa.py" utilizará como insumo uno de los productos del script "Ranking OCDE Primera Etapa.py". En este archivo esta consolidada toda la información. 

```
Consolidado_AC_NA = pd.read_csv("PRODUCTOS/AJUSTES/CONSOLIDADO - TIPO RANKING 202X.csv", sep=";", encoding="latin-1", decimal=',')
```
