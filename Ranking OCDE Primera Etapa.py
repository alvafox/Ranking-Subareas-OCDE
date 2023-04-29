#=================================================================================================================
#=============================================Cálculo de RNK OCDE=================================================
#=================================================================================================================
import pandas as pd
#https://stackoverflow.com/questions/30635145/create-multiple-dataframes-in-loop
#===========================================COMITES===============================================================
"101 Matemáticas"
"102 Computación y Ciencias de la informática"
"103 Ciencias Físicas y Astronomía"
"104 Ciencias Químicas"
"105 Ciencias de la Tierra y Medioambientales"
"106 Ciencias Biológicas"
"107 Otras Ciencias Naturales"
"201 Ingeniería Civil"
"202 Ingeniería Eléctrica y Electrónica"
"203 Ingeniería Mecánica"
"204 Ingeniería Química"
"205 Ingeniería de Materiales"
"206 Ingeniería Médica"
"207 Ingeniería Medioambiental"
"208 Biotecnología Medioambiental"
"209 Biotecnología Industrial"
"210 Nanotecnología"
"211 Otras Ingenierías y Tecnologías"
"301 Medicina Básica"
"302 Medicina Clínica"
"303 Ciencias de la Salud"
"401 Agricultura, Silvicultura y Pesca"
"402 Ciencias Animales y de la Leche"
"403 Ciencias Veterinarias"
"405 Otras Ciencias Agrícolas"
"501 Psicología"
"502 Economía y Negocios"
"503 Ciencias de la Educación"
"504 Sociología"
"505 Leyes"
"506 Ciencias Políticas"
"507 Geografía Social y Económica"
"508 Periodismo y Comunicaciones"
"509 Otras Ciencias Sociales"
"601 Historia y Arqueología"
"602 Idiomas y Literatura"
"603 Filosofía, Ética y Religión"
"604 Arte"

# INSTITUCIONES
# Research Council (No Académica)
# National Academy (No Académica)
# Academic System (Ninguna)
# Research Institute (No Académica)
# Academic (Académica)
# Government (No Académica)
# Nonprofit (No Académica)
# Health (No Académica)
# Corporate (No Académica)
# Partnership (No Académica)
# Healthcare System (No Académica)

# Del Academic System, hay que filtrar las siguientes Universidades 202X
# Indian Institute of Technology System (IIT System)
# University of the Philippines System
# University of Quebec
# University Town of Shenzhen
# University of London
# y TODAS las Academic System de USA / las restantes del NINGUNO, deben incorporarse como Académicas
# De las no academicas, sacar todas las de Chile

########################################################################################################################
# Crear las carpetas si no existen
if not os.path.exists("PRODUCTOS/COMPROBACIONES"):
    os.makedirs("PRODUCTOS/COMPROBACIONES")

if not os.path.exists("PRODUCTOS/AJUSTES"):
    os.makedirs("PRODUCTOS/AJUSTES")

if not os.path.exists("PRODUCTOS/RANKINGS/CONSOLIDADOS/"):
    os.makedirs("PRODUCTOS/RANKINGS/CONSOLIDADOS/")

########################################################################################################################
DEFINICIONES = pd.read_csv('Definiciones.csv', sep=";", encoding="UTF-8", decimal=',')
########################################################################################################################

for i in range(0, 39):
        df = pd.read_csv('INSUMOS/' + str(DEFINICIONES["Nombre Descarga EXCEL"][i]) + '.csv', sep=",", encoding="UTF-8", decimal=',')
        df['% Docs Cited'] = df['% Docs Cited'].astype('float64')
        df['Category Normalized Citation Impact'] = df['Category Normalized Citation Impact'].astype('float64')
        df["Sub-área"] = DEFINICIONES["COD SUBAREA"][i]
        df.set_index("Sub-área", inplace=True)
        df = df.iloc[:-10]
        df.to_csv("PRODUCTOS/AJUSTES/" + str(DEFINICIONES["SUBAREA OCDE"][i]) + '.csv', sep=';', encoding='latin-1', index=True, decimal=',')
        exec(str(DEFINICIONES["DF"][i] + ' = df'.format(i)))
        print(df.dtypes)
        print(df)

#==========================================================================================================================
#===================================================TODOS JUNTOS===========================================================
#==========================================================================================================================

TODOS = [Matematicas, Computacion, Fisica, Quimica, Tierra, Biologicas, Otras_naturales, Civil, Electrica, Mecanica,
        Ing_Quimica, Ing_Materiales, Ing_Medica, Ing_Medioambiental, Biotec_Medioambiental, Biotec_Industrial,
        Nanotecnologia, Otras_Ingenierias, Medicina_Basica, Medicina_Clinica, Ciencias_Salud, Agricultura, Ciencias_Animales,
        Ciencias_Veterinarias, Otras_Agricolas, Psicologia, Economia, Educacion, Sociologia, Leyes, Ciencias_Politicas,
        Geografia, Periodismo, Otras_Sociales, Historia, Idiomas, Filosofia, Arte, Otras_Humanidades]

print(TODOS)

#=================================================EXPORTAR A CSV========================================================

CONSOLIDADO = pd.concat(TODOS)
CONSOLIDADO.to_csv("PRODUCTOS/AJUSTES/CONSOLIDADO.csv", sep=';', encoding='latin-1', index=True, decimal=',')

#########################################Determinar Tipos de Ranking por Defecto########################################
Tipo_Rnk_202X = []
Rnk_202X = []
for index, row in CONSOLIDADO.iterrows():
        if row["Organization Type"] != "Academic" and row["Organization Type"] != "Academic System":
                Tipo_Rnk_202X = "2 - Ranking no Académico"
        elif row["Organization Type"] == "Academic System":
                Tipo_Rnk_202X = "3 - Ninguno"
        elif row["Organization Type"] == "Academic":
                Tipo_Rnk_202X = "1 - Ranking Académico"
        Rnk_202X.append(Tipo_Rnk_202X)

CONSOLIDADO["Tipo Ranking 202X (Defecto)"] = Rnk_202X

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

##################################################AJUSTES A PAISES######################################################
#Acá introducir correcciones a paises.
CONSOLIDADO["Country or Region"] = CONSOLIDADO["Country or Region"].replace("CHINA MAINLAND","CHINA")
CONSOLIDADO["Country or Region"] = CONSOLIDADO["Country or Region"].replace("ENGLAND","UNITED KINGDOM")
CONSOLIDADO["Country or Region"] = CONSOLIDADO["Country or Region"].replace("GERMANY (FED REP GER)","GERMANY")
CONSOLIDADO["Country or Region"] = CONSOLIDADO["Country or Region"].replace("NORTHERN IRELAND","UNITED KINGDOM")
CONSOLIDADO["Country or Region"] = CONSOLIDADO["Country or Region"].replace("SCOTLAND","UNITED KINGDOM")
CONSOLIDADO["Country or Region"] = CONSOLIDADO["Country or Region"].replace("WALES","UNITED KINGDOM")

###################################################Exportar a CSV#######################################################

CONSOLIDADO.to_csv("PRODUCTOS/RANKINGS/CONSOLIDADOS/CONSOLIDADO - TIPO RANKING 202X.csv", sep=';', encoding='latin-1', index=True, decimal=',')

########################################################################################################################
#instituciones sin duplicados para realizar la verificación
#NO ACADEMICAS
CONSOLIDADO_DP_NA = CONSOLIDADO.loc[CONSOLIDADO["Tipo Ranking 202X (Defecto)"] == "2 - Ranking no Académico"]
CONSOLIDADO_DP_NA = CONSOLIDADO_DP_NA.drop_duplicates(subset="Name", keep="first")
CONSOLIDADO_DP_NA = CONSOLIDADO_DP_NA.sort_values(by=["Name"], ascending=[True])

CONSOLIDADO_DP_NA.to_csv("PRODUCTOS/COMPROBACIONES/SIN DUPLICADOS (NO ACADEMICAS).csv", sep=';', encoding='latin-1', index=True, decimal=',')

#ACADEMICAS
CONSOLIDADO_DP_AC = CONSOLIDADO.loc[CONSOLIDADO["Tipo Ranking 202X (Defecto)"] == "1 - Ranking Académico"]
CONSOLIDADO_DP_AC = CONSOLIDADO_DP_AC.drop_duplicates(subset="Name", keep="first")
CONSOLIDADO_DP_AC = CONSOLIDADO_DP_AC.sort_values(by=["Name"], ascending=[True])

CONSOLIDADO_DP_AC.to_csv("PRODUCTOS/COMPROBACIONES/SIN DUPLICADOS (ACADEMICAS).csv", sep=';', encoding='latin-1', index=True, decimal=',')

#NINGUNO
CONSOLIDADO_DP_AC = CONSOLIDADO.loc[CONSOLIDADO["Tipo Ranking 202X (Defecto)"] == "3 - Ninguno"]
CONSOLIDADO_DP_AC = CONSOLIDADO_DP_AC.drop_duplicates(subset="Name", keep="first")
CONSOLIDADO_DP_AC = CONSOLIDADO_DP_AC.sort_values(by=["Name"], ascending=[True])

CONSOLIDADO_DP_AC.to_csv("PRODUCTOS/COMPROBACIONES/SIN DUPLICADOS (NINGUNO).csv", sep=';', encoding='latin-1', index=True, decimal=',')

########################################################################################################################

print("Proceso Finalizado")


