import json
import sys

import pandas as pd

import pathway_assessor_module as pa

work_dir = sys.argv[1]

meta = json.load(open(f'{work_dir}/meta.json', 'r'))
database = meta['database']

expression_df = pd.read_csv(f'{work_dir}/input.tsv', sep='\t', index_col=0)

meta['input_shape'] = expression_df.shape

act_scores = pa.geometric(expression_table=expression_df,
                          db=database,
                          ascending=True,
                          rank_method='max')

json.dump(meta, open(f'{work_dir}/meta.json', 'w'))

act_scores.to_csv(f'{work_dir}/activation_scores.tsv', sep='\t')

sup_scores = pa.geometric(expression_table=expression_df,
                          db=database,
                          ascending=False,
                          rank_method='min')


sup_scores.to_csv(f'{work_dir}/suppression_scores.tsv', sep='\t')
