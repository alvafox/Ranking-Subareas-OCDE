# =======================================================================================================================
# =================================================Cálculo de RNK OCDE===================================================
# =======================================================================================================================
import pandas as pd
import decimal
from decimal import Decimal as D
context = decimal.getcontext()
context.rounding = decimal.ROUND_HALF_UP
# ===================================================CONSIDERACIONES=====================================================
"SUBAREAS OCDE"
"1.01 Matemáticas"
"1.02 Computación y Ciencias de la informática"
"1.03 Ciencias Físicas y Astronomía"
"1.04 Ciencias Químicas"
"1.05 Ciencias de la Tierra y Medioambientales"
"1.06 Ciencias Biológicas"
"1.07 Otras Ciencias Naturales"
"2.01 Ingeniería Civil"
"2.02 Ingeniería Eléctrica y Electrónica"
"2.03 Ingeniería Mecánica"
"2.04 Ingeniería Química"
"2.05 Ingeniería de Materiales"
"2.06 Ingeniería Médica"
"2.07 Ingeniería Medioambiental"
"2.08 Biotecnología Medioambiental"
"2.09 Biotecnología Industrial"
"2.10 Nanotecnología"
"2.11 Otras Ingenierías y Tecnologías"
"3.01 Medicina Básica"
"3.02 Medicina Clínica"
"3.03 Ciencias de la Salud"
"4.01 Agricultura, Silvicultura y Pesca"
"4.02 Ciencias Animales y de la Leche"
"4.03 Ciencias Veterinarias"
"4.05 Otras Ciencias Agrícolas"
"5.01 Psicología"
"5.02 Economía y Negocios"
"5.03 Ciencias de la Educación"
"5.04 Sociología"
"5.05 Leyes"
"5.06 Ciencias Políticas"
"5.07 Geografía Social y Económica"
"5.08 Periodismo y Comunicaciones"
"5.09 Otras Ciencias Sociales"
"6.01 Historia y Arqueología"
"6.02 Idiomas y Literatura"
"6.03 Filosofía, Ética y Religión"
"6.04 Arte"
"6.05 Otras Humanidades"

#Importar el resultado de la Primera Etapa "CONSOLIDADO - TIPO RANKING 202X.csv"
# Definiciones para nombres dinámicos
########################################################################################################################
DEFINICIONES = pd.read_csv('Definiciones.csv', sep=";", encoding="UTF-8", decimal=',')
########################################################################################################################
Consolidado_AC_NA = pd.read_csv("PRODUCTOS/AJUSTES/CONSOLIDADO - TIPO RANKING 202X.csv", sep=";", encoding="latin-1", decimal=',')
########################################################################################################################

########################################################################################################################
########################################################################################################################
########################################################################################################################
for i in range(0, 39):
    df = Consolidado_AC_NA.loc[Consolidado_AC_NA["Sub-área"] == DEFINICIONES["COD SUBAREA"][i]]
    df.set_index('Sub-área', inplace=True)
    df.reset_index()
    exec(str(DEFINICIONES["DF"][i] + ' = df'.format(i)))
    print(df.dtypes)
    print(df)

################################################## INDICADOR 1 #########################################################

for i in range(0, 39):
    Calculo_Documentos = []
    Calculo_Citas = []
    Multiplicacion = []
    Indicador = []
    df = Consolidado_AC_NA.loc[Consolidado_AC_NA["Sub-área"] == DEFINICIONES["COD SUBAREA"][i]]
    df.set_index('Sub-área', inplace=True)
    df.reset_index()
    for index, row in df.iterrows():
        Calculo_Documentos = row["Web of Science Documents"]
        Calculo_Citas = row["Category Normalized Citation Impact"]
        Multiplicacion = D(str(Calculo_Documentos)) * D(str(Calculo_Citas))
        Indicador.append(Multiplicacion)
    df["Indicador"] = Indicador
    df["Indicador"] = df["Indicador"].astype(float)
    # ordenamiento jerarquico para desempate
    df = df.sort_values(
        by=["Indicador","Web of Science Documents","Category Normalized Citation Impact","Times Cited"],
        ascending=[False,False,False,False])
    df.reset_index()
    print(df.dtypes)
    exec(str(DEFINICIONES["DF"][i] + ' = df'.format(i)))

#Ahora incorporando el indicador
TODOS_1 = [Matematicas, Computacion, Fisica, Quimica, Tierra, Biologicas, Otras_naturales, Civil, Electrica, Mecanica,
        Ing_Quimica, Ing_Materiales, Ing_Medica, Ing_Medioambiental, Biotec_Medioambiental, Biotec_Industrial,
        Nanotecnologia, Otras_Ingenierias, Medicina_Basica, Medicina_Clinica, Ciencias_Salud, Agricultura, Ciencias_Animales,
        Ciencias_Veterinarias, Otras_Agricolas, Psicologia, Economia, Educacion, Sociologia, Leyes, Ciencias_Politicas,
        Geografia, Periodismo, Otras_Sociales, Historia, Idiomas, Filosofia, Arte, Otras_Humanidades]


# Antes hay que filtrar por institución académica y no académica
# -------------------------------------------------FILTROS---------------------------------------------------------------
# -------------------------------------------FILTRO NO ACADEMICA---------------------------------------------------------

for i in range(0, 39):
    df = TODOS_1[i]
    df_NA = df.loc[(df["Tipo Ranking 202X (Definitivo)"] == "2 - Ranking no Académico")]
    df_NA.reset_index()
    df_NA_CH = df_NA.loc[(df_NA["Country or Region"] == "CHILE")]
    if len(df_NA_CH) > 1:
        df_NA = df_NA.loc[~(df_NA["Country or Region"] == "CHILE")]
        df_NA = pd.concat([df_NA, df_NA_CH])
        df_NA = df_NA.iloc[:-len(df_NA_CH) + 1]
    else:
        df_NA = df_NA
    df_NA = df_NA.sort_values(by=["Indicador","Web of Science Documents","Category Normalized Citation Impact","Times Cited"],
        ascending=[False,False,False,False])
    df_NA.reset_index()
    exec(str(DEFINICIONES["DF"][i] + '_NA = df_NA'.format(i)))

# ------------------------------------------------FILTRO ACADEMICA-------------------------------------------------------
for i in range(0, 39):
    df = TODOS_1[i]
    df_AC = df.loc[(df["Tipo Ranking 202X (Definitivo)"] == "1 - Ranking Académico")]
    df_AC.reset_index()
    df_AC_CH = df_AC.loc[(df_AC["Country or Region"] == "CHILE")]
    if len(df_AC_CH) > 1:
        df_AC = df_AC.loc[~(df_AC["Country or Region"] == "CHILE")]
        df_AC = pd.concat([df_AC, df_AC_CH])
        df_AC = df_AC.iloc[:-len(df_AC_CH) + 1]
    else:
        df_AC = df_AC
    df_AC = df_AC.sort_values(by=["Indicador","Web of Science Documents","Category Normalized Citation Impact","Times Cited"],
        ascending=[False,False,False,False])
    df_AC.reset_index()
    exec(str(DEFINICIONES["DF"][i] + '_AC = df_AC'.format(i)))

# ------------------------------------------------ORDENAMIENTO ANID------------------------------------------------------
#Filtradas y ordenadas jerarquicamente (en esta caso sin las chilenas)
TODOS_NA = [Matematicas_NA, Computacion_NA, Fisica_NA, Quimica_NA, Tierra_NA, Biologicas_NA, Otras_naturales_NA, Civil_NA,
            Electrica_NA, Mecanica_NA, Ing_Quimica_NA, Ing_Materiales_NA, Ing_Medica_NA, Ing_Medioambiental_NA,
            Biotec_Medioambiental_NA, Biotec_Industrial_NA, Nanotecnologia_NA, Otras_Ingenierias_NA, Medicina_Basica_NA,
            Medicina_Clinica_NA, Ciencias_Salud_NA, Agricultura_NA, Ciencias_Animales_NA, Ciencias_Veterinarias_NA,
            Otras_Agricolas_NA, Psicologia_NA, Economia_NA, Educacion_NA, Sociologia_NA, Leyes_NA, Ciencias_Politicas_NA,
            Geografia_NA, Periodismo_NA, Otras_Sociales_NA, Historia_NA, Idiomas_NA, Filosofia_NA, Arte_NA, Otras_Humanidades_NA]
# ORDENAMIENTO NO ACADEMICA-----------------------------------------------------------------------------------------------------------

for x in range(0, 39):
    df_ORD_NA = TODOS_NA[x] #Utiliza la lista para llamar a los DF
    Orden = []
    Ordenamiento = []
    for i in range(1, len(df_ORD_NA) + 1):
        Orden = i
        Ordenamiento.append(Orden)
    df_ORD_NA["Ranking_ANID"] = Ordenamiento
    df_ORD_NA["Rank"] = df_ORD_NA["Indicador"].rank(method="dense",ascending=False)
    exec(str(DEFINICIONES["DF"][x] + '_NA = df_ORD_NA'.format(x)))

# ------------------------------------------------ORDENAMIENTO ANID------------------------------------------------------
#Filtradas y ordenadas jerarquicamente (solo con una chilena en ranking)
TODOS_AC = [Matematicas_AC, Computacion_AC, Fisica_AC, Quimica_AC, Tierra_AC, Biologicas_AC, Otras_naturales_AC,
        Civil_AC, Electrica_AC, Mecanica_AC, Ing_Quimica_AC, Ing_Materiales_AC, Ing_Medica_AC, Ing_Medioambiental_AC,
        Biotec_Medioambiental_AC, Biotec_Industrial_AC, Nanotecnologia_AC, Otras_Ingenierias_AC, Medicina_Basica_AC,
        Medicina_Clinica_AC, Ciencias_Salud_AC, Agricultura_AC, Ciencias_Animales_AC, Ciencias_Veterinarias_AC,
        Otras_Agricolas_AC, Psicologia_AC, Economia_AC, Educacion_AC, Sociologia_AC, Leyes_AC, Ciencias_Politicas_AC,
        Geografia_AC, Periodismo_AC, Otras_Sociales_AC, Historia_AC, Idiomas_AC, Filosofia_AC, Arte_AC, Otras_Humanidades_AC]
# ORDENAMIENTO ACADEMICA -------------------------------------------------------------------------------------------------------------

for x in range(0, 39):
    df_ORD_AC = TODOS_AC[x] #Utiliza la lista para llamar a los DF
    Orden = []
    Ordenamiento = []
    for i in range(1, len(df_ORD_AC) + 1):
        Orden = i
        Ordenamiento.append(Orden)
    df_ORD_AC["Ranking_ANID"] = Ordenamiento
    df_ORD_AC["Rank"] = df_ORD_AC["Indicador"].rank(method="dense",ascending=False)
    exec(str(DEFINICIONES["DF"][x] + '_AC = df_ORD_AC'.format(x)))

# ----------------------------------------------------PUNTAJE------------------------------------------------------------
# NO ACADEMICA-----------------------------------------------------------------------------------------------------------

for i in range(0, 39):
    DF_ORD_NA = TODOS_NA[i] #Utiliza la lista para llamar a los DF
    Primera_Chilena_NA = (DF_ORD_NA["Country or Region"].values == "CHILE").argmax() + 1
    Puntaje = []
    Puntaje_ANID = []
    for index, row in DF_ORD_NA.iterrows():
        if row["Ranking_ANID"] <= 50:
            Puntaje = D("5.000")
        elif Primera_Chilena_NA == 1:
            Puntaje = round(D(str(5 - (row["Ranking_ANID"] - 50) * 4 / (len(DF_ORD_NA) - 50))), 3)
        elif (row["Ranking_ANID"] > 50) and (row["Ranking_ANID"] < Primera_Chilena_NA):
            Puntaje = round(D(str(5 - (row["Ranking_ANID"] - 50) * 4 / (Primera_Chilena_NA - 50))), 3)
        else:
            Puntaje = D("1.000")
        Puntaje_ANID.append(Puntaje)
    DF_ORD_NA["Puntaje_ANID"] = Puntaje_ANID
    DF_ORD_NA["Puntaje_ANID"] = DF_ORD_NA["Puntaje_ANID"].astype(float)
    exec(str(DEFINICIONES["DF"][i] + '_NA = DF_ORD_NA'.format(i)))
    DF_ORD_NA.to_csv("PRODUCTOS/RANKINGS/NO ACADEMICOS/" + str(DEFINICIONES["SUBAREA OCDE"][i]) + ' - NA.csv', sep=';', encoding='latin-1',
              index=True, decimal=',')
# ACADEMICA--------------------------------------------------------------------------------------------------------------
for i in range(0, 39):
    DF_ORD_AC = TODOS_AC[i] #Utiliza la lista para llamar a los DF
    Primera_Chilena_AC = (DF_ORD_AC["Country or Region"].values == "CHILE").argmax() + 1
    Puntaje = []
    Puntaje_ANID = []
    for index, row in DF_ORD_AC.iterrows():
        if row["Ranking_ANID"] <= 100:
            Puntaje = D("5.000")
        elif Primera_Chilena_AC == 1:
            Puntaje = round(D(str(5 - (row["Ranking_ANID"] - 100) * 4 / (len(DF_ORD_AC) - 100))), 3)
        elif (row["Ranking_ANID"] > 100) and (row["Ranking_ANID"] < Primera_Chilena_AC):
            Puntaje = round(D(str(5 - (row["Ranking_ANID"] - 100) * 4 / (Primera_Chilena_AC - 100))), 3)
        else:
            Puntaje = D("1.000")
        Puntaje_ANID.append(Puntaje)
    DF_ORD_AC["Puntaje_ANID"] = Puntaje_ANID
    DF_ORD_AC["Puntaje_ANID"] = DF_ORD_AC["Puntaje_ANID"].astype(float)
    exec(str(DEFINICIONES["DF"][i] + '_AC = DF_ORD_AC'.format(i)))
    DF_ORD_AC.to_csv("PRODUCTOS/RANKINGS/ACADEMICOS/" + str(DEFINICIONES["SUBAREA OCDE"][i]) + ' - AC.csv', sep=';',
                  encoding='latin-1', index=True, decimal=',')

# =======================================================================================================================
# ================================================TODOS NO ACADÉMICOS====================================================
# =======================================================================================================================
# Actualiza la lista para concatenarla. Aquí sí se necesitan los DF
TODOS_NA_1 = [Matematicas_NA, Computacion_NA, Fisica_NA, Quimica_NA, Tierra_NA, Biologicas_NA, Otras_naturales_NA, Civil_NA,
            Electrica_NA, Mecanica_NA, Ing_Quimica_NA, Ing_Materiales_NA, Ing_Medica_NA, Ing_Medioambiental_NA,
            Biotec_Medioambiental_NA, Biotec_Industrial_NA, Nanotecnologia_NA, Otras_Ingenierias_NA, Medicina_Basica_NA,
            Medicina_Clinica_NA, Ciencias_Salud_NA, Agricultura_NA, Ciencias_Animales_NA, Ciencias_Veterinarias_NA,
            Otras_Agricolas_NA, Psicologia_NA, Economia_NA, Educacion_NA, Sociologia_NA, Leyes_NA, Ciencias_Politicas_NA,
            Geografia_NA, Periodismo_NA, Otras_Sociales_NA, Historia_NA, Idiomas_NA, Filosofia_NA, Arte_NA, Otras_Humanidades_NA]

Cuenta_NA = [len(Matematicas_NA), len(Computacion_NA), len(Fisica_NA), len(Quimica_NA), len(Tierra_NA), len(Biologicas_NA),
             len(Otras_naturales_NA), len(Civil_NA), len(Electrica_NA), len(Mecanica_NA), len(Ing_Quimica_NA),
             len(Ing_Materiales_NA), len(Ing_Medica_NA), len(Ing_Medioambiental_NA), len(Biotec_Medioambiental_NA),
             len(Biotec_Industrial_NA), len(Nanotecnologia_NA), len(Otras_Ingenierias_NA), len(Medicina_Basica_NA),
             len(Medicina_Clinica_NA), len(Ciencias_Salud_NA), len(Agricultura_NA), len(Ciencias_Animales_NA),
             len(Ciencias_Veterinarias_NA), len(Otras_Agricolas_NA), len(Psicologia_NA), len(Economia_NA),
             len(Educacion_NA), len(Sociologia_NA), len(Leyes_NA), len(Ciencias_Politicas_NA), len(Geografia_NA),
             len(Periodismo_NA), len(Otras_Sociales_NA), len(Historia_NA),len(Idiomas_NA), len(Filosofia_NA),
             len(Arte_NA), len(Otras_Humanidades_NA)]

print(TODOS_NA_1)

# =================================================EXPORTAR A CSV========================================================
# Ahora los está concatenando, por lo que esta llamando al dataframe
CONSOLIDADO_NA = pd.concat(TODOS_NA_1)
CONSOLIDADO_NA["Puntaje_ANID"] = CONSOLIDADO_NA["Puntaje_ANID"].astype(float)
CONSOLIDADO_NA.to_csv("PRODUCTOS/RANKINGS/CONSOLIDADOS/CONSOLIDADO_NA.csv", sep=';', encoding='latin-1', index=True, decimal=',')

# -----------------------------------------------------------------------------------------------------------------------
PRIMERAS_INSTITUCIONES_CL_NA = CONSOLIDADO_NA.loc[CONSOLIDADO_NA["Country or Region"] == "CHILE"]
PRIMERAS_INSTITUCIONES_CL_NA = PRIMERAS_INSTITUCIONES_CL_NA.assign(Cantidad_de_Instituciones=Cuenta_NA)
n150_NA = CONSOLIDADO_NA.loc[CONSOLIDADO_NA["Ranking_ANID"] == 150]
n150_NA.to_csv("PRODUCTOS/RANKINGS/CONSOLIDADOS/listado_150_NA.csv", sep=';', encoding='latin-1', index=True, decimal=',')
PRIMERAS_INSTITUCIONES_CL_NA.to_csv("PRODUCTOS/RANKINGS/CONSOLIDADOS/PRIMERAS_CHILENAS_NA.csv", sep=';', encoding='latin-1', index=True, decimal=',')
# =======================================================================================================================
# ===================================================TODOS ACADÉMICOS====================================================
# =======================================================================================================================
# Actualiza la lista para concatenarla. Aquí sí se necesitan los DF
TODOS_AC_1 = [Matematicas_AC, Computacion_AC, Fisica_AC, Quimica_AC, Tierra_AC, Biologicas_AC, Otras_naturales_AC,
        Civil_AC, Electrica_AC, Mecanica_AC, Ing_Quimica_AC, Ing_Materiales_AC, Ing_Medica_AC, Ing_Medioambiental_AC,
        Biotec_Medioambiental_AC, Biotec_Industrial_AC, Nanotecnologia_AC, Otras_Ingenierias_AC, Medicina_Basica_AC,
        Medicina_Clinica_AC, Ciencias_Salud_AC, Agricultura_AC, Ciencias_Animales_AC, Ciencias_Veterinarias_AC,
        Otras_Agricolas_AC, Psicologia_AC, Economia_AC, Educacion_AC, Sociologia_AC, Leyes_AC, Ciencias_Politicas_AC,
        Geografia_AC, Periodismo_AC, Otras_Sociales_AC, Historia_AC, Idiomas_AC, Filosofia_AC, Arte_AC, Otras_Humanidades_AC]

Cuenta_AC = [len(Matematicas_AC), len(Computacion_AC), len(Fisica_AC), len(Quimica_AC), len(Tierra_AC), len(Biologicas_AC),
             len(Otras_naturales_AC), len(Civil_AC), len(Electrica_AC), len(Mecanica_AC), len(Ing_Quimica_AC), len(Ing_Materiales_AC),
             len(Ing_Medica_AC), len(Ing_Medioambiental_AC), len(Biotec_Medioambiental_AC), len(Biotec_Industrial_AC),
             len(Nanotecnologia_AC), len(Otras_Ingenierias_AC), len(Medicina_Basica_AC), len(Medicina_Clinica_AC),
             len(Ciencias_Salud_AC), len(Agricultura_AC), len(Ciencias_Animales_AC), len(Ciencias_Veterinarias_AC),
             len(Otras_Agricolas_AC), len(Psicologia_AC), len(Economia_AC), len(Educacion_AC), len(Sociologia_AC),
             len(Leyes_AC), len(Ciencias_Politicas_AC), len(Geografia_AC), len(Periodismo_AC), len(Otras_Sociales_AC),
             len(Historia_AC), len(Idiomas_AC), len(Filosofia_AC), len(Arte_AC), len(Otras_Humanidades_AC)]

print(Cuenta_AC)

# =================================================EXPORTAR A CSV========================================================

CONSOLIDADO_AC = pd.concat(TODOS_AC_1)
CONSOLIDADO_AC["Puntaje_ANID"] = CONSOLIDADO_AC["Puntaje_ANID"].astype(float)
CONSOLIDADO_AC.to_csv("PRODUCTOS/RANKINGS/CONSOLIDADOS/CONSOLIDADO_AC.csv", sep=';', encoding='latin-1', index=True, decimal=',')

# ----------------------------------------------------------------------------------------------------------------------
PRIMERAS_INSTITUCIONES_CL_AC = CONSOLIDADO_AC.loc[CONSOLIDADO_AC["Country or Region"] == "CHILE"]
PRIMERAS_INSTITUCIONES_CL_AC = PRIMERAS_INSTITUCIONES_CL_AC.assign(Cantidad_de_Instituciones=Cuenta_AC)
n150_AC = CONSOLIDADO_AC.loc[CONSOLIDADO_AC["Ranking_ANID"] == 150]
n150_AC.to_csv("PRODUCTOS/RANKINGS/CONSOLIDADOS/listado_150_AC.csv", sep=';', encoding='latin-1', index=True, decimal=',')
PRIMERAS_INSTITUCIONES_CL_AC.to_csv("PRODUCTOS/RANKINGS/CONSOLIDADOS/PRIMERAS_CHILENAS_AC.csv", sep=';', encoding='latin-1', index=True, decimal=',')
# =====================================================FIN===============================================================

print("Proceso Finalizado")
