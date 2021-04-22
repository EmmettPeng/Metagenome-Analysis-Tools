#!/bin/python
# -*- encoding: utf-8 -*-

'''
This program is to process the checkm coverage output.
It filters contigs longer than 500bp.
'''

import pandas as pd
import sys

#df = pd.read_csv('contigs_coverage.out', delimiter='\t')
df = pd.read_csv(sys.argv[1],delimiter='\t')
summary = df[['Sequence Id', 'Sequence length (bp)', 'Coverage', 'Mapped reads']]
summary = summary[(summary['Sequence length (bp)']>=500)]
summary = summary.rename(columns={'Sequence Id': 'seq_id','Sequence length (bp)':'seq_len','Coverage':'coverage','Mapped reads':'mapped_reads'})
summary.eval('avg_read_len = coverage * seq_len / mapped_reads', inplace = True)
summary.eval('nt_num = seq_len * coverage', inplace = True)
sum_seq_len, sum_nt_num = summary['seq_len'].sum(), summary['nt_num'].sum()
avg_depth = sum_nt_num/sum_seq_len
print(avg_depth)