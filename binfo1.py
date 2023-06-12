#!/usr/bin/python3
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

cnts = pd.read_csv('read-counts.txt', sep='\t', comment='#', index_col=0)
cnts.head()

cnts['clip_enrichment'] = cnts['eCLIP_H_RBFOX2XPT.bam'] / cnts['eCLIP_control_H_RBFOX2XPT.bam']
cnts['transcr_change'] = cnts['shRNA_KD_RBFOX2.bam'] / cnts['shRNA_control_RBFOX2.bam']
cnts.head(n=20)

cnts_excluded = cnts[(cnts['eCLIP_H_RBFOX2XPT.bam'] >= 30) & (cnts['eCLIP_control_H_RBFOX2XPT.bam'] >= 30) & (cnts['shRNA_KD_RBFOX2.bam'] >= 30) & (cnts['shRNA_control_RBFOX2.bam'] >= 30)].copy()
cnts_excluded.head(n=20)

fig, ax = plt.subplots(1, 1, figsize=(5, 5))
ax.scatter(np.log2(cnts_excluded['clip_enrichment']), 
           np.log2(cnts_excluded['transcr_change']), 
           s=1, c='#000000', alpha=0.15)

ax.set_title('Correlation between CLIP enrichment and \nRNA level upon RBFOX2 knockdown')
ax.set_xlabel('RBFOX2 CLIP Enrichment (log$_2$)')
ax.set_ylabel('mRNA abundance change upon RBFOX2 knockdown (log$_2$)')

r, p = stats.pearsonr(np.log2(cnts_excluded['clip_enrichment']), np.log2(cnts_excluded['transcr_change']))
ax.annotate('r = {:.2f}'.format(r), xy=(0.8, 0.05), xycoords='axes fraction')

#plt.show()
plt.savefig('CLIP_enrichment_and_Transcription.png')

# >> 여기까지 .py file로 만들어서 저장 후 리눅스(Ubuntu) shell에서 실행
# 결과파일 - CLIP_enrichment_and_Transcription.png