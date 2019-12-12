echo "Loading OrthogroupIDs"
python scripts/load_ortho.py --orthogroup_file static/data/all_OrthogroupIDs.txt
#Then load rest. Since Orthogroup IDs already exist and don't have to be created, the rest goes faster

echo "Loading clusters"
#Each orthogroup belongs in multiple clusters.
python scripts/load_clusters.py --cluster_table static/data/panplant_clusters.csv

echo "Load orthogroup annotation"
python scripts/load_orthoannot.py --annotation_file static/data/orthogroup_annotations.txt

echo "Load CF-MS scores"
#gunzip static/data/allplants_feature_matrix_missing1.unscaled.top100.edges.top100k.gz
python scripts/load_scores.py --score_file static/data/allplants_feature_matrix_missing1.unscaled.top100.edges.fdr70

echo "Load Orthogroup Protein conversion"
#gunzip static/data/complete_orthology_w_atnums.csv
python scripts/load_prot.py --conversion_file static/data/complete_orthogroup_protID_mapping.csv
