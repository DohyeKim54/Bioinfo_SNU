#!/usr/bin/python3
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats


df_local = pd.read_csv('goa_locate.txt', sep='\t')

with open('erase.txt') as f:
    for line in f.readlines():
      if line in df_local.index.to_list():
        df_local.drop(index=line)

df_local.to_csv('goa_locate.txt', sep = '\t')


gene_dict={}
with open('gene_name.txt') as f:
    lines = f.readlines()
    for name in lines:
      gene_dict[name.split('\t')[1].strip()] = name.split('\t')[0].strip()

local_dict={}
with open('goa_locate.txt') as f:
  for line in f.readlines():
    gene_name = line.split('\t')[1]
    gene_locus = line.split('\t')[2]
    if gene_name in list(gene_dict.keys()):
      local_dict[gene_dict[gene_name]]=gene_locus

local_list=[]
for i, items in enumerate(cnts_excluded.iterrows()):
  gene = items[0].split('.')[0]
  if gene in local_dict.keys():
    local = local_dict[gene]
    local_list.append(local)
  else:
    local_list.append('not_in_list')
print(local_list)


cnts_excluded['local']=local_list
print(cnts_excluded)

cnts_localized = cnts_excluded[cnts_excluded.local != 'not_in_list'].copy()
print(cnts_localized)


color_dict = {'integral membrane':'#e32b51', 'cytoplasm':'#50b846', 'nucleus':'#546fb6'}

fig, ax = plt.subplots(1, 1, figsize=(5, 5))

for local in ['integral membrane','cytoplasm','nucleus']:
  cnts_plot=cnts_localized[cnts_localized['local']==local]
  ax.scatter(np.log2(cnts_plot['clip_enrichment']), 
            np.log2(cnts_plot['transcr_change']), 
            s=1, alpha=0.15,
            c=color_dict[local], label=local)

ax.set_title('Correlation between CLIP enrichment and \nRNA level upon RBFOX2 knockdown')
ax.set_xlabel('RBFOX2 CLIP Enrichment (log$_2$)')
ax.set_ylabel('mRNA abundance change upon RBFOX2 knockdown (log$_2$)')

r, p = stats.pearsonr(np.log2(cnts_localized['clip_enrichment']), np.log2(cnts_localized['transcr_change']))
ax.annotate('r = {:.2f}'.format(r), xy=(0.8, 0.05), xycoords='axes fraction')
ax.legend(markerscale=3, loc='lower left', fontsize=6)

#plt.show()
plt.savefig('CLIP_enrichment_localization.png')

# >> 여기까지 .py file로 만들어서 저장 후 리눅스(Ubuntu) shell에서 실행
# 결과파일 - CLIP_enrichment_localization.png 
# database 추가 전 결과 파일 (integral membrane localization 없음) = CLIP_enrichment_localization_before.png