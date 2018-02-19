# coding: utf-8
import pandas as pd
import numpy as np
import itertools as it
import scipy
from scipy.stats import pearsonr
from scipy.stats import spearmanr
from scipy import stats
orig9k_bioplex2_hygeo_bioid_hygeo_boldt_hygeo_treiber_df = pd.read_csv("/project/kdrew/data/protein_complex_maps/complex_map2/orig9k_bioplex2_hygeo_bioid_hygeo_boldt_apms_hygeo_treiber_hygeo.featmat")
orig9k_bioplex2_hygeo_bioid_hygeo_boldt_hygeo_treiber_df = orig9k_bioplex2_hygeo_bioid_hygeo_boldt_hygeo_treiber_df.set_index("Unnamed: 0")
youn_hygeo_gt4_df = pd.read_csv("/stor/work/Marcotte/project/kdrew/data/youn_bioid/youn_bioid_AvgSpec4_prey_pairs_pvalcorr_logchoose.feat")
youn_hygeo_gt2_df = pd.read_csv("/stor/work/Marcotte/project/kdrew/data/youn_bioid/youn_bioid_AvgSpec2_prey_pairs_pvalcorr_logchoose.feat")
youn_hygeo_df = pd.read_csv("/stor/work/Marcotte/project/kdrew/data/youn_bioid/youn_bioid_prey_pairs_pvalcorr_logchoose.feat")
youn_df = pd.read_csv("/project/kdrew/data/youn_bioid/youn_bioid_mmc2-5_SAINT_ID3105_wgeneids.csv")
youn_df.head()
youn_hygeo_gt4_hygeo_geneid_pairs = youn_hygeo_gt4_df[['gene_id1','gene_id2']].values
youn_hygeo_gt2_hygeo_geneid_pairs = youn_hygeo_gt2_df[['gene_id1','gene_id2']].values
youn_hygeo_hygeo_geneid_pairs = youn_hygeo_df[['gene_id1','gene_id2']].values
youn_geneid_pairs = youn_df[['gene_ids','prey_gene_ids']].values
youn_hygeo_gt4_geneid_pairs_strsort = [str(sorted([str(x[0]),str(x[1])])) for x in youn_hygeo_gt4_hygeo_geneid_pairs] 
youn_hygeo_gt2_geneid_pairs_strsort = [str(sorted([str(x[0]),str(x[1])])) for x in youn_hygeo_gt2_hygeo_geneid_pairs]
youn_hygeo_geneid_pairs_strsort = [str(sorted([str(x[0]),str(x[1])])) for x in youn_hygeo_hygeo_geneid_pairs]
youn_hygeo_gt4_df['geneids_str_order'] = youn_hygeo_gt4_geneid_pairs_strsort
youn_hygeo_gt2_df['geneids_str_order'] = youn_hygeo_gt2_geneid_pairs_strsort
youn_hygeo_df['geneids_str_order'] = youn_hygeo_geneid_pairs_strsort
youn_geneid_pairs_strsort = [str(sorted([str(x[0]),str(x[1])])) for x in youn_geneid_pairs]
youn_df['geneids_str_order'] = youn_geneid_pairs_strsort
youn_hygeo_gt4_df = youn_hygeo_gt4_df.set_index("geneids_str_order")
youn_hygeo_gt2_df = youn_hygeo_gt2_df.set_index("geneids_str_order")
youn_hygeo_df = youn_hygeo_df.set_index("geneids_str_order")
youn_df = youn_df.set_index("geneids_str_order")
youn_hygeo_gt4_gb_df = youn_hygeo_gt4_df.groupby(youn_hygeo_gt4_df.index).first()
youn_hygeo_gt2_gb_df = youn_hygeo_gt2_df.groupby(youn_hygeo_gt2_df.index).first()
youn_hygeo_gb_df = youn_hygeo_df.groupby(youn_hygeo_df.index).first()
youn_gb_df = youn_df.groupby(youn_df.index).first()
orig9k_bioplex2_hygeo_bioid_hygeo_boldt_hygeo_treiber_youn_df = orig9k_bioplex2_hygeo_bioid_hygeo_boldt_hygeo_treiber_df.join(youn_df, how="outer", rsuffix="_youn")
orig9k_bioplex2_hygeo_bioid_hygeo_boldt_hygeo_treiber_youn_hygeo_df = orig9k_bioplex2_hygeo_bioid_hygeo_boldt_hygeo_treiber_youn_df.join(youn_hygeo_df, how="outer", rsuffix="_youn_hygeo")
orig9k_bioplex2_hygeo_bioid_hygeo_boldt_hygeo_treiber_youn_hygeo_gt2_df = orig9k_bioplex2_hygeo_bioid_hygeo_boldt_hygeo_treiber_youn_hygeo_df.join(youn_hygeo_gt2_df, how="outer", rsuffix="_youn_hygeo_gt2")
orig9k_bioplex2_hygeo_bioid_hygeo_boldt_hygeo_treiber_youn_hygeo_gt2_gt4_df = orig9k_bioplex2_hygeo_bioid_hygeo_boldt_hygeo_treiber_youn_hygeo_gt2_df.join(youn_hygeo_gt4_df, how="outer", rsuffix="_youn_hygeo_gt4")
orig9k_bioplex2_hygeo_bioid_hygeo_boldt_hygeo_treiber_youn_hygeo_gt2_gt4_df.to_csv("/project/kdrew/data/protein_complex_maps/complex_map2/orig9k_bioplex2_hygeo_bioid_hygeo_boldt_apms_hygeo_treiber_hygeo_youn_hygeo.featmat")
get_ipython().magic(u'save humap2_create_featmap6 1:40')
cols = """Ce_1111_poisson,Ce_1111_wcc,Ce_1111_apex,Ce_1111_pq_euc,Ce_6mg_1203_poisson,Ce_6mg_1203_wcc,Ce_6mg_1203_apex,Ce_6mg_1203_pq_euc,Ce_BNF_wan_60_1209_poisson,Ce_BNF_wan_60_1209_wcc,Ce_BNF_wan_60_1209_apex,Ce_BNF_wan_60_1209_pq_euc,Ce_CRF_wan_60_1209_poisson,Ce_CRF_wan_60_1209_wcc,Ce_CRF_wan_60_1209_apex,Ce_CRF_wan_60_1209_pq_euc,Ce_beadsB_wan_60_1208_poisson,Ce_beadsB_wan_60_1208_wcc,Ce_beadsB_wan_60_1208_apex,Ce_beadsB_wan_60_1208_pq_euc,Ce_beadsC_wan_60_1209_poisson,Ce_beadsC_wan_60_1209_wcc,Ce_beadsC_wan_60_1209_apex,Ce_beadsC_wan_60_1209_pq_euc,Ce_beadsL_1206_poisson,Ce_beadsL_1206_wcc,Ce_beadsL_1206_apex,Ce_beadsL_1206_pq_euc,Ce_beadsN_wan_60_1208_poisson,Ce_beadsN_wan_60_1208_wcc,Ce_beadsN_wan_60_1208_apex,Ce_beadsN_wan_60_1208_pq_euc,Ce_beadsR_wan_60_1209_poisson,Ce_beadsR_wan_60_1209_wcc,Ce_beadsR_wan_60_1209_apex,Ce_beadsR_wan_60_1209_pq_euc,Ce_beadsflow_1206_poisson,Ce_beadsflow_1206_wcc,Ce_beadsflow_1206_apex,Ce_beadsflow_1206_pq_euc,Ce_ups_1206_poisson,Ce_ups_1206_wcc,Ce_ups_1206_apex,Ce_ups_1206_pq_euc,Dm_1107_DSL2_poisson,Dm_1107_DSL2_wcc,Dm_1107_DSL2_apex,Dm_1107_DSL2_pq_euc,Dm_1107_Dem_poisson,Dm_1107_Dem_wcc,Dm_1107_Dem_apex,Dm_1107_Dem_pq_euc,Dm_1201_Dem_poisson,Dm_1201_Dem_wcc,Dm_1201_Dem_apex,Dm_1201_Dem_pq_euc,Dm_SL2_wan_110_1208_poisson,Dm_SL2_wan_110_1208_wcc,Dm_SL2_wan_110_1208_apex,Dm_SL2_wan_110_1208_pq_euc,Hs_CB660_1105_poisson,Hs_CB660_1105_wcc,Hs_CB660_1105_apex,Hs_CB660_1105_pq_euc,Hs_G166_1104_poisson,Hs_G166_1104_wcc,Hs_G166_1104_apex,Hs_G166_1104_pq_euc,Hs_G166_1105_poisson,Hs_G166_1105_wcc,Hs_G166_1105_apex,Hs_G166_1105_pq_euc,Hs_hekN_1108_poisson,Hs_hekN_1108_wcc,Hs_hekN_1108_apex,Hs_hekN_1108_pq_euc,Hs_hekN_1201_poisson,Hs_hekN_1201_wcc,Hs_hekN_1201_apex,Hs_hekN_1201_pq_euc,Hs_hekN_ph_hcw120_1_poisson,Hs_hekN_ph_hcw120_1_wcc,Hs_hekN_ph_hcw120_1_apex,Hs_hekN_ph_hcw120_1_pq_euc,Hs_hekN_ph_hcw120_2_poisson,Hs_hekN_ph_hcw120_2_wcc,Hs_hekN_ph_hcw120_2_apex,Hs_hekN_ph_hcw120_2_pq_euc,Hs_hek_kinase95_poisson,Hs_hek_kinase95_wcc,Hs_hek_kinase95_apex,Hs_hek_kinase95_pq_euc,Hs_hek_wan_membraneopioid72_poisson,Hs_hek_wan_membraneopioid72_wcc,Hs_hek_wan_membraneopioid72_apex,Hs_hek_wan_membraneopioid72_pq_euc,Hs_helaC_mar_SGF_poisson,Hs_helaC_mar_SGF_wcc,Hs_helaC_mar_SGF_apex,Hs_helaC_mar_SGF_pq_euc,Hs_helaC_mar_ief3_10_poisson,Hs_helaC_mar_ief3_10_wcc,Hs_helaC_mar_ief3_10_apex,Hs_helaC_mar_ief3_10_pq_euc,Hs_helaC_mar_ief5_8_poisson,Hs_helaC_mar_ief5_8_wcc,Hs_helaC_mar_ief5_8_apex,Hs_helaC_mar_ief5_8_pq_euc,Hs_helaC_ph_tcs269_1_poisson,Hs_helaC_ph_tcs269_1_wcc,Hs_helaC_ph_tcs269_1_apex,Hs_helaC_ph_tcs269_1_pq_euc,Hs_helaC_ph_tcs269_2_poisson,Hs_helaC_ph_tcs269_2_wcc,Hs_helaC_ph_tcs269_2_apex,Hs_helaC_ph_tcs269_2_pq_euc,Hs_helaC_ph_wax43_poisson,Hs_helaC_ph_wax43_wcc,Hs_helaC_ph_wax43_apex,Hs_helaC_ph_wax43_pq_euc,Hs_helaN_1003_poisson,Hs_helaN_1003_wcc,Hs_helaN_1003_apex,Hs_helaN_1003_pq_euc,Hs_helaN_1010_poisson,Hs_helaN_1010_wcc,Hs_helaN_1010_apex,Hs_helaN_1010_pq_euc,Hs_helaN_mar_SGF_poisson,Hs_helaN_mar_SGF_wcc,Hs_helaN_mar_SGF_apex,Hs_helaN_mar_SGF_pq_euc,Hs_helaN_mar_ief3_10_poisson,Hs_helaN_mar_ief3_10_wcc,Hs_helaN_mar_ief3_10_apex,Hs_helaN_mar_ief3_10_pq_euc,Hs_helaN_mar_ief5_8_poisson,Hs_helaN_mar_ief5_8_wcc,Hs_helaN_mar_ief5_8_apex,Hs_helaN_mar_ief5_8_pq_euc,Hs_helaN_ph_hcw120_1_poisson,Hs_helaN_ph_hcw120_1_wcc,Hs_helaN_ph_hcw120_1_apex,Hs_helaN_ph_hcw120_1_pq_euc,Hs_helaN_ph_hcw120_2_poisson,Hs_helaN_ph_hcw120_2_wcc,Hs_helaN_ph_hcw120_2_apex,Hs_helaN_ph_hcw120_2_pq_euc,Hs_helaN_ph_saf48_poisson,Hs_helaN_ph_saf48_wcc,Hs_helaN_ph_saf48_apex,Hs_helaN_ph_saf48_pq_euc,Hs_helaN_ph_tcs375_P1_poisson,Hs_helaN_ph_tcs375_P1_wcc,Hs_helaN_ph_tcs375_P1_apex,Hs_helaN_ph_tcs375_P1_pq_euc,Hs_helaN_ph_tcs375_P2_poisson,Hs_helaN_ph_tcs375_P2_wcc,Hs_helaN_ph_tcs375_P2_apex,Hs_helaN_ph_tcs375_P2_pq_euc,Hs_helaN_ph_tcs375_P3_poisson,Hs_helaN_ph_tcs375_P3_wcc,Hs_helaN_ph_tcs375_P3_apex,Hs_helaN_ph_tcs375_P3_pq_euc,Hs_wan_aguhplc108_1204_poisson,Hs_wan_aguhplc108_1204_wcc,Hs_wan_aguhplc108_1204_apex,Hs_wan_aguhplc108_1204_pq_euc,Hs_wan_shuhplc94_1206_poisson,Hs_wan_shuhplc94_1206_wcc,Hs_wan_shuhplc94_1206_apex,Hs_wan_shuhplc94_1206_pq_euc,Mm_1106_poisson,Mm_1106_wcc,Mm_1106_apex,Mm_1106_pq_euc,Mm_1201_poisson,Mm_1201_wcc,Mm_1201_apex,Mm_1201_pq_euc,Sp_1103_Egg_poisson,Sp_1103_Egg_wcc,Sp_1103_Egg_apex,Sp_1103_Egg_pq_euc,Sp_1108_2ce_poisson,Sp_1108_2ce_wcc,Sp_1108_2ce_apex,Sp_1108_2ce_pq_euc,Sp_1108_BL_poisson,Sp_1108_BL_wcc,Sp_1108_BL_apex,Sp_1108_BL_pq_euc,Sp_1109_PF5_poisson,Sp_1109_PF5_wcc,Sp_1109_PF5_apex,Sp_1109_PF5_pq_euc,Sp_1109_UNF_poisson,Sp_1109_UNF_wcc,Sp_1109_UNF_apex,Sp_1109_UNF_pq_euc,Sp_60_121010_poisson,Sp_60_121010_wcc,Sp_60_121010_apex,Sp_60_121010_pq_euc,Sp_beadsALF_60_121014_poisson,Sp_beadsALF_60_121014_wcc,Sp_beadsALF_60_121014_apex,Sp_beadsALF_60_121014_pq_euc,Sp_beadsBNF_73_1201119_poisson,Sp_beadsBNF_73_1201119_wcc,Sp_beadsBNF_73_1201119_apex,Sp_beadsBNF_73_1201119_pq_euc,Sp_beadsL_60_121125_poisson,Sp_beadsL_60_121125_wcc,Sp_beadsL_60_121125_apex,Sp_beadsL_60_121125_pq_euc,Sp_iex_60_121019_poisson,Sp_iex_60_121019_wcc,Sp_iex_60_121019_apex,Sp_iex_60_121019_pq_euc,ext_Dm_guru,ext_Hs_malo,entropy_orig9k,zscore_orig9k,nwdscore_orig9k,plate_zscore_orig9k,uPeps_orig9k,ratio_orig9k,total_psms_orig9k,ratioTotalPSMs_orig9k,UtoTratio_orig9k,neg_ln_pval,pair_count,prey.bait.correlation,valid.values,log10.prey.bait.ratio,log10.prey.bait.expression.ratio,hein_neg_ln_pval,hein_pair_count,ave_apsm,nwdscore_bioplex2,zscore_bioplex2,plate_zscore_bioplex2,entropy_bioplex2,uPeps_bioplex2,ratio_bioplex2,total_psms_bioplex2,ratioTotalPSMs_bioplex2,UtoTratio_bioplex2,neg_ln_pval_bioplex2_Z4,pair_count_bioplex2_Z4,neg_ln_pval_bioplex2_Z2,pair_count_bioplex2_Z2,AvgSpec,AvgP,MaxP,Fold_Change,BFDR,AvgSpec_nonciliated_bioid,AvgP_nonciliated_bioid,MaxP_nonciliated_bioid,Fold_Change_nonciliated_bioid,BFDR_nonciliated_bioid,neg_ln_pval_cilium_hygeo,pair_count_cilium_hygeo,neg_ln_pval_cilium_hygeo_avgspec2,pair_count_cilium_hygeo_avgspec2,neg_ln_pval_cilium_hygeo_avgspec4,pair_count_cilium_hygeo_avgspec4,SAij,Sij,Sji,Mij,neg_ln_pval_boldt_apms_hygeo,pair_count_boldt_apms_hygeo,neg_ln_pval_boldt_apms_hygeo_gt4,pair_count_boldt_apms_hygeo_gt4,neg_ln_pval_treiber_hygeo_gt4,pair_count_treiber_hygeo_gt4""".split(',')
cols
cols.append('AvgSpec_youn')
cols.append('AvgP_youn')
cols.append('MaxP_youn')
cols.append('FoldChange')
cols.append('BFDR_youn')
cols.append('neg_ln_pval_youn_hygeo')
cols.append('pair_count_youn_hygeo')
cols.append('neg_ln_pval_youn_hygeo_gt2')
cols.append('pair_count_youn_hygeo_gt2')
cols.append('neg_ln_pval_youn_hygeo_gt4')
cols.append('pair_count_youn_hygeo_gt4')
orig9k_bioplex2_hygeo_bioid_hygeo_boldt_hygeo_treiber_youn_hygeo_gt2_gt4_trim_df = orig9k_bioplex2_hygeo_bioid_hygeo_boldt_hygeo_treiber_youn_hygeo_gt2_gt4_df[cols]
orig9k_bioplex2_hygeo_bioid_hygeo_boldt_hygeo_treiber_youn_hygeo_gt2_gt4_df = None
orig9k_bioplex2_hygeo_bioid_hygeo_boldt_hygeo_treiber_df = None
orig9k_bioplex2_hygeo_bioid_hygeo_boldt_hygeo_treiber_youn_df = None
orig9k_bioplex2_hygeo_bioid_hygeo_boldt_hygeo_treiber_youn_hygeo_df = None
orig9k_bioplex2_hygeo_bioid_hygeo_boldt_hygeo_treiber_youn_hygeo_gt2_df = None
orig9k_bioplex2_hygeo_bioid_hygeo_boldt_hygeo_treiber_youn_hygeo_gt2_gt4_trim_df.columns
geneids = [eval(x)[0] for x in orig9k_bioplex2_hygeo_bioid_hygeo_boldt_hygeo_treiber_youn_hygeo_gt2_gt4_trim_df.index]
geneids2 = [eval(x)[1] for x in orig9k_bioplex2_hygeo_bioid_hygeo_boldt_hygeo_treiber_youn_hygeo_gt2_gt4_trim_df.index]
orig9k_bioplex2_hygeo_bioid_hygeo_boldt_hygeo_treiber_youn_hygeo_gt2_gt4_trim_df['id1'] = geneids
orig9k_bioplex2_hygeo_bioid_hygeo_boldt_hygeo_treiber_youn_hygeo_gt2_gt4_trim_df['id2'] = geneids2
colswids = orig9k_bioplex2_hygeo_bioid_hygeo_boldt_hygeo_treiber_youn_hygeo_gt2_gt4_trim_df.columns
orig9k_bioplex2_hygeo_bioid_hygeo_boldt_hygeo_treiber_youn_hygeo_gt2_gt4_trim_df = orig9k_bioplex2_hygeo_bioid_hygeo_boldt_hygeo_treiber_youn_hygeo_gt2_gt4_trim_df[list(colswids)[-2:] + list(colswids)[:-2]]
orig9k_bioplex2_hygeo_bioid_hygeo_boldt_hygeo_treiber_youn_hygeo_gt2_gt4_trim_df.head()
orig9k_bioplex2_hygeo_bioid_hygeo_boldt_hygeo_treiber_youn_hygeo_gt2_gt4_trim_df.to_csv("/stor/work/Marcotte/project/kdrew/data/protein_complex_maps/complex_map2/orig9k_bioplex2_hygeo_bioid_hygeo_boldt_hygeo_treiber_hygeo_youn_hygeo_trimCols.featmat",index=False)
