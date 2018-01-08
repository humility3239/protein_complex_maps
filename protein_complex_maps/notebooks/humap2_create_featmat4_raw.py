# coding: utf-8
import pandas as pd
import numpy as np
import itertools as it
import scipy
from scipy.stats import pearsonr
from scipy.stats import spearmanr
from scipy import stats
boldt_apms_fname = "/stor/work/Marcotte/project/kdrew/data/boldt_apms/BoldtAPMS_socioaffinities.featmat
boldt_apms_fname = "/stor/work/Marcotte/project/kdrew/data/boldt_apms/BoldtAPMS_socioaffinities.featmat"
boldt_apms_df = pd.read_csv(boldt_apms_fname)
boldt_apms_df.head()
orig9k_bioplex2_hygeo_bioid_hygeo_avgspec2_4_df = pd.read_csv("/project/kdrew/data/protein_complex_maps/v35_features/corum_split/v35_revisit/revisitTrain_fromHopper/orig9k_bioplex2_hygeo_bioid_hygeo.featmat")
orig9k_bioplex2_hygeo_bioid_hygeo_avgspec2_4_df.head()
orig9k_bioplex2_hygeo_bioid_hygeo_avgspec2_4_df = orig9k_bioplex2_hygeo_bioid_hygeo_avgspec2_4_df.set_index("Unnamed: 0")
orig9k_bioplex2_hygeo_bioid_hygeo_avgspec2_4_df.head()
boldt_apms_df.head()
boldt_apms_df = boldt_apms_df.set_index("geneids_str_order")
len(boldt_apms_df)
boldt_apms_df = boldt_apms_df.groupby(boldt_apms_df.index).first()
len(boldt_apms_df)
boldt_apms_df = pd.read_csv(boldt_apms_fname)
boldt_apms_df.head()
boldt_apms_df = boldt_apms_df.set_index("geneids_str_order")
len(boldt_apms_df)
boldt_apms_rmdup_df = boldt_apms_df.groupby(boldt_apms_df.index).first()
len(boldt_apms_rmdup_df)
boldt_apms_df = pd.read_csv(boldt_apms_fname)
boldt_apms_df = boldt_apms_df.set_index("geneids_str_order")
len(boldt_apms_df)
boldt_apms_rmdup_df = boldt_apms_df.groupby(boldt_apms_df.index).first()
len(boldt_apms_rmdup_df)
orig9k_bioplex2_hygeo_bioid_hygeo_avgspec2_4_boldt_apms_df = orig9k_bioplex2_hygeo_bioid_hygeo_avgspec2_4_df.join(boldt_apms_rmdup_df, how="outer", rsuffix="_boldt_apms")
orig9k_bioplex2_hygeo_bioid_hygeo_avgspec2_4_boldt_apms_df
orig9k_bioplex2_hygeo_bioid_hygeo_avgspec2_4_boldt_apms_df.query("gene_id_boldt_apms == gene_id_boldt_apms").head()
orig9k_bioplex2_hygeo_bioid_hygeo_avgspec2_4_boldt_apms_df.query("gene_id_boldt_apms == geneid_boldt_apms").head()
orig9k_bioplex2_hygeo_bioid_hygeo_avgspec2_4_boldt_apms_df.query("geneid_boldt_apms == geneid_boldt_apms").head()
get_ipython().magic(u'save humap2_create_featmat4_raw 1:37')
boldt_apms_hypergeo_df = pd.read_csv("/stor/work/Marcotte/project/kdrew/data/boldt_apms/BoldtAPMS_percentile_20180104_prey_pairs_pvalcorr_logchoose.feat")
boldt_apms_hypergeo_gt4_df = pd.read_csv("/stor/work/Marcotte/project/kdrew/data/boldt_apms/BoldtAPMS_percentile_gt4_20180104_prey_pairs_pvalcorr_logchoose.feat")
boldt_apms_hypergeo_df.head()
boldt_apms_hypergeo_gt4_df.head()
boldt_apms_hygeo_geneid_pairs = boldt_apms_hypergeo_df[['gene_id1','gene_id2']].values 
boldt_apms_hygeo_gt4_geneid_pairs = boldt_apms_hypergeo_gt4_df[['gene_id1','gene_id2']].values
boldt_apms_hygeo_geneid_pairs_strsort = [str(sorted([str(x[0]),str(x[1])])) for x in boldt_apms_hygeo_geneid_pairs]
boldt_apms_hygeo_gt4_geneid_pairs_strsort = [str(sorted([str(x[0]),str(x[1])])) for x in boldt_apms_hygeo_gt4_geneid_pairs]
boldt_apms_hypergeo_df['geneids_str_order'] = boldt_apms_hygeo_geneid_pairs_strsort
boldt_apms_hypergeo_gt4_df['geneids_str_order'] = boldt_apms_hygeo_gt4_geneid_pairs_strsort
boldt_apms_hypergeo_df = boldt_apms_hypergeo_df.set_index("geneids_str_order")
boldt_apms_hypergeo_gt4_df = boldt_apms_hypergeo_gt4_df.set_index("geneids_str_order")
boldt_apms_hypergeo_gb_df = boldt_apms_hypergeo_df.groupby(boldt_apms_hypergeo_df.index).first()
boldt_apms_hypergeo_gt4_gb_df = boldt_apms_hypergeo_gt4_df.groupby(boldt_apms_hypergeo_gt4_df.index).first()
orig9k_bioplex2_hygeo_bioid_hygeo_avgspec2_4_boldt_apms_hypergeo_df = orig9k_bioplex2_hygeo_bioid_hygeo_avgspec2_4_boldt_apms_df.join(boldt_apms_hypergeo_gb_df, how="outer", rsuffix="_boldt_apms_hygeo")
orig9k_bioplex2_hygeo_bioid_hygeo_avgspec2_4_boldt_apms_hypergeo_gt4_df = orig9k_bioplex2_hygeo_bioid_hygeo_avgspec2_4_boldt_apms_hypergeo_df.join(boldt_apms_hypergeo_gt4_gb_df, how="outer", rsuffix="_boldt_apms_hygeo_gt4")
orig9k_bioplex2_hygeo_bioid_hygeo_avgspec2_4_boldt_apms_hypergeo_gt4_df.to_csv("/project/kdrew/data/protein_complex_maps/v35_features/corum_split/v35_revisit/revisitTrain_fromHopper/orig9k_bioplex2_hygeo_bioid_hygeo_boldt_apms_hygeo.featmat")
