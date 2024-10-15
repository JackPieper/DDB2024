import pandas as pd
import numpy as np


df = pd.read_csv('sap_storing_data_hu_project.csv', low_memory=False)

df = df.drop(columns=['stm_sap_mon_meld_ddt', 'stm_mon_begin_ddt', 'stm_mon_toelichting_trdl', 'stm_oh_pg_mld',
                 'stm_scenario_mon', 'stm_mon_nr_status_omschr', 'stm_mon_nr__statuscode', 'stm_mon_nr_status_wijzdd',
                 'stm_aanntpl_ddt', 'stm_objectdl_code_gst', 'stm_objectdl_groep_gst', 'stm_progfh_in_ddt',
                 'stm_progfh_in_invoer_ddt', 'stm_progfh_gw_ddt', 'stm_progfh_gw_lwd_ddt', 'stm_progfh_hz',
                 'stm_veroorz_groep', 'stm_veroorz_code', 'stm_veroorz_tekst_kort', 'stm_effect', 'stm_afspr_aanvangddt',
                 'stm_mon_eind_ddt', 'stm_mon_vhdsincident', 'stm_dir_betrok_tr', 'stm_aangelegd_dd', 'stm_aangelegd_tijd',
                 'stm_mon_begindatum', 'stm_mon_begintijd', 'stm_progfh_gw_datum', 'stm_mon_eind_datum', 'stm_mon_eind_tijd',
                 'stm_controle_dd', 'stm_akkoord_mon_toewijz', 'stm_status_sapnaarmon', 'stm_fact_jn', 'stm_akkoord_melding_jn',
                 'stm_afsluit_ddt', 'stm_afsluit_dd', 'stm_afsluit_tijd', 'stm_rec_toegev_ddt', 'stm_hinderwaarde',
                 'stm_actie', 'stm_standplaats', 'stm_status_gebr', 'stm_wbi_nummer', 'stm_projnr', 'stm_historie_toelichting',
                 'stm_schade_verhaalb_jn', 'stm_schadenr', 'stm_schade_status_ga', 'stm_schade_statusdatum', 'stm_relatiervo_vorig',
                 'stm_relatiervo_volgend', 'stm_relatiervo', 'stm_afspr_func_hersteldd', 'stm_afspr_func_hersteltijd',
                 'stm_sorteerveld', 'stm_rapportage_maand', 'stm_rapportage_jaar', 'stm_x_bron_publ_dt', 'stm_x_bron_bestandsnaam',
                 'stm_x_bron_arch_dt', 'stm_x_actueel_ind', 'stm_x_run_id', 'stm_x_bk', 'stm_x_start_sessie_dt', 'stm_x_vervallen_ind'])

df.to_csv('ddb_data_NaN_included.csv', index=False)

