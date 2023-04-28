import pandas as pd
from functools import reduce

Consolidado_AC = pd.read_csv("PRODUCTOS/RANKINGS/CONSOLIDADOS/CONSOLIDADO_AC.csv", sep=";", encoding="latin-1", decimal=',')
Consolidado_NA = pd.read_csv("PRODUCTOS/RANKINGS/CONSOLIDADOS/CONSOLIDADO_NA.csv", sep=";", encoding="latin-1", decimal=',')
OCDE = pd.read_csv("OCDE.csv", sep=";", encoding="latin-1", decimal=',')

OCDE = OCDE.rename(columns={"COD SUB AREA OCDE": "Sub-área"})


data_frames_AC = [Consolidado_AC, OCDE]
df_merged_AC = reduce(lambda left,right: pd.merge(left,right,on=["Sub-área"],how='outer'), data_frames_AC)
df_merged_AC = df_merged_AC.rename(columns={"AREA OCDE": "ÁREA OCDE", "SUB AREA OCDE": "SUB-ÁREA OCDE"})

data_frames_NA = [Consolidado_NA, OCDE]
df_merged_NA = reduce(lambda left,right: pd.merge(left,right,on=["Sub-área"],how='outer'), data_frames_NA)
df_merged_NA = df_merged_NA.rename(columns={"AREA OCDE": "ÁREA OCDE", "SUB AREA OCDE": "SUB-ÁREA OCDE"})

df_merged_AC.to_csv("PRODUCTOS/RANKINGS/CONSOLIDADOS/POWER BI/CONSOLIDADO_AC (POWER BI).csv", sep=';', encoding='latin-1', index=False, decimal=',')

df_merged_NA.to_csv("PRODUCTOS/RANKINGS/CONSOLIDADOS/POWER BI/CONSOLIDADO_NA (POWER BI).csv", sep=';', encoding='latin-1', index=False, decimal=',')