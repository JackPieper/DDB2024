import pandas as pd
import numpy as np


df = pd.read_csv('db/ddb_data_NaN_included.csv', low_memory=False)

non_nan = df.notna().sum()
nan = df.isna().sum()
temp = []
avg_list = {}
mode_list = {}
for i in df.columns:
    print(f'filtered results for {i}: \n values:{non_nan[i]} \n NaN_values:{nan[i]}')
    if non_nan[i] < (nan[i] + non_nan[i])*0.8:
        print(f'{i} has been removed')
        temp.append(i)
    else:
        df[i] = df[i].astype(type(df[i][1]), errors='raise')
        if isinstance(df[i][1], (float, np.float64, np.int64)):
            avg = df[i].mean()
            mode = df[i].mode(dropna=True)
            df[i] = df[i].fillna(avg)
            avg_list[i] = avg
            mode_list[i] = mode
        else:
            df[i] = df[i].str.strip().str.lower().replace(['nan', 'none'], np.nan)
            mode = df[i].mode(dropna=True)
            df[i] = df[i].fillna(mode[0])
        print(f'{i} is usable and has mode: {mode}')
        print(f'{i} variables are of type: {type(df[i][1])}')

df.drop(temp, axis=1, inplace=True)
print(df)
print(avg_list)
print(mode_list)

df.to_csv('db/final_db.csv', index=False)
"""
het is allemaal een beetje chaotisch momenteel omdat het nu nog alleen voor data formatting is.
Alles zit in 1 loop voor om het compact te houden, maar het kan later in een notebook apart.
alle kolommen met meer dan 20% missende waardes worden gelijk verwijdert voor ruimt + die data is nauwelijks betrouwbaar.
Kolommen zijn uniform in datatype. 
alle missende waardes voor de overige kolommen worden gevuld met de modus of het gemiddelde.
index 0 van veel kolommen had type problemen, dus ik heb [1] gebruikt in die instanties. 
Er zijn denk ik nog een paar verbeteringen die kunnen worden gedaan + uitschieters zijn nog niet behandeld.
Maar dat kan donderdag.
hieronder heb ik ook alle variables gezet overblijven na het cleanen voor nu met type ernaast:

unnamed <class 'str'>
stm_sap_meldnr <class 'np.int64'>
stm_mon_nr <class 'numpy.float64'>
stm_sap_meld_ddt <class 'float'>
stm_sap_meldtekst_lang <class 'float'>

stm_sap_meldtekst <class 'float'>
stm_geo_mld <class 'float'>
stm_geo_mld_uit_functiepl <class 'numpy.float64'>
stm_km_van_mld <class 'numpy.float64'>
stm_km_tot_mld <class 'numpy.float64'>

stm_prioriteit <class 'numpy.float64'>
stm_status_melding_sap <class 'float'>
stm_aanngeb_ddt <class 'float'>
stm_oh_pg_gst <class 'float'>
stm_geo_gst <class 'float'>

stm_geo_gst_uit_functiepl <class 'numpy.float64'>
stm_km_van_gst <class 'numpy.float64'>
stm_km_tot_gst <class 'numpy.float64'>
stm_oorz_groep <class 'float'>
stm_oorz_code <class 'numpy.float64'> 

stm_oorz_tkst <class 'float'>
stm_fh_ddt <class 'float'>
stm_fh_status <class 'numpy.float64'>
stm_tao_indicator <class 'str'> 
stm_tao_telling_mutatie <class 'numpy.int64'>

stm_tao_beinvloedbaar_indicator <class 'str'>
stm_evb <class 'float'>
stm_sap_melddatum <class 'float'>
stm_sap_meldtijd <class 'float'>
stm_functiepl_mld <class 'float'>

stm_contractgeb_gst <class 'numpy.float64'>
stm_functiepl_gst <class 'float'>
stm_techn_gst <class 'float'>
stm_aanngeb_dd <class 'float'>
stm_aanngeb_tijd <class 'float'>

stm_aanntpl_tijd <class 'float'>
stm_arbeid <class 'numpy.float64'>
stm_progfh_in_tijd <class 'float'>
stm_progfh_in_invoer_tijd <class 'float'>
stm_progfh_in_duur <class 'float'>

stm_progfh_gw_tijd <class 'float'>
stm_progfh_gw_duur <class 'float'>
stm_progfh_gw_teller <class 'numpy.float64'>
stm_afspr_aanvangdd <class 'float'>
stm_afspr_aanvangtijd <class 'float'>

stm_fh_dd <class 'float'>
stm_fh_tijd <class 'float'>
stm_fh_duur <class 'numpy.float64'>
stm_reactie_duur <class 'numpy.float64'> 
stm_sap_storeindtijd <class 'float'>
"""